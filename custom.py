from __future__ import absolute_import

import errno
import itertools
import json
import logging
import os
import re
import shlex
import subprocess

import jinja2
import six
import yaml

import markdown
from markdown.extensions import Extension
from markdown.extensions.toc import slugify
from markdown.extensions import fenced_code
from markdown import inlinepatterns
from markdown import treeprocessors
from markdown.util import etree

import mkdocs.config as _ # work around for mkdocs import cycle
from mkdocs.plugins import BasePlugin
from mkdocs.nav import Page, Header

from guild import guildfile

log = logging.getLogger("mkdocs")

nav_pages = []
nav_pages_index = None

class NavResolvePlugin(BasePlugin):

    def on_nav(self, nav, config):
        """Process nav items.

        We use page meta for nav title and other config settings so we
        need to read the page source. To avoid re-reading we disable
        the read_source function.
        """
        globals()["nav_pages"] = []
        globals()["nav_pages_index"] = None
        for item in nav:
            self._ensure_loaded(item, config)
        return nav

    def _ensure_loaded(self, item, config):
        if isinstance(item, Header):
            for item in item.children:
                self._ensure_loaded(item, config)
        elif isinstance(item, Page):
            item.read_source(config)
            item.read_source = lambda **_kw: None
            nav_pages.append(item)

class FixTocProcessor(treeprocessors.Treeprocessor):

    def run(self, doc):
        for toc in self._iter_toc(doc):
            self._fix_toc(toc)

    @staticmethod
    def _iter_toc(root):
        for el in root.iter():
            if el.get("class") == "toc":
                yield el

    def _fix_toc(self, toc):
        self._fix_tree(toc)
        self._ul_to_ol(toc)

    @staticmethod
    def _fix_tree(toc):
        children = list(toc)
        if len(children) != 1 or children[0].tag != "ul":
            raise AssertionError(etree.tostring(toc))
        ul = children[0]
        toc.tag = "ol"
        toc.remove(ul)
        items = list(ul)
        if len(items) == 1:
            item1 = items[0]
            item1_children = list(item1)
            if (len(item1_children) == 1 and
                item1_children[0].tag == "a"):
                items = []
            elif (len(item1_children) == 2 and
                item1_children[0].tag == "a" and
                item1_children[1].tag == "ul"):
                items = list(item1_children[1])
            else:
                raise AssertionError(etree.tostring(item1))
        toc.extend(items)

    @staticmethod
    def _ul_to_ol(toc):
        for item in toc.iter():
            if item.tag == "ul":
                item.tag = "ol"

class FixToc(Extension):
    """Reformats toc elements.

    Changes to toc:

    - Outer div is replaced with ol + "toc" class

    - If there's a single level 1 entry, that entry is removed end
      its child entries are promoted to level 1

    To illustrate, we'll configure markdown with TocExtension and our
    extension:

    >>> md = markdown.Markdown(extensions=["toc", FixToc()])

    Here's a simple document with a toc in the format we use in this
    site:

    >>> print(md.convert("[TOC]\\n# 1\\n## 1_1\\n## 1_2"))
    <ol class="toc">
    <li><a href="#1_1">1_1</a></li>
    <li><a href="#1_2">1_2</a></li>
    </ol>
    <h1 id="1">1</h1>
    <h2 id="1_1">1_1</h2>
    <h2 id="1_2">1_2</h2>

    Here's a doc with two toc levels:

    >>> print(md.convert("[TOC]\\n# 1\\n## 1_1\\n### 1_1_1"))
    <ol class="toc">
    <li><a href="#1_1">1_1</a><ol>
    <li><a href="#1_1_1">1_1_1</a></li>
    </ol>
    </li>
    </ol>
    <h1 id="1">1</h1>
    <h2 id="1_1">1_1</h2>
    <h3 id="1_1_1">1_1_1</h3>

    A toc with one heading:

    >>> print(md.convert("# 1\\n\\n[TOC]"))
    <h1 id="1">1</h1>
    <ol class="toc">
    </ol>

    A toc with no headings:

    >>> print(md.convert("[TOC]"))
    <ol class="toc">
    </ol>

    """

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add("fix_toc", FixTocProcessor(md), "_end")

class DefIdProcessor(treeprocessors.Treeprocessor):

    def run(self, doc):
        for dt in doc.iter("dt"):
            if dt.text:
                dt.set("id", _slugify(dt.text))

def _slugify(s):
    return slugify(six.text_type(s), "-")

class DefinitionId(Extension):
    """Adds ids to definition terms.

    With ids, definition terms can be referenced within a page using
    hashes.

    Ids are generated using the toc extension's slugify function using
    "-" as the separator.

    To illustrate, let's configure markdown with DefinitionList and
    our extension:

    >>> md = markdown.Markdown(extensions=["def_list", DefinitionId()])

    Here's a definition list:

    >>> print(md.convert("foo\\n: Overused example\\n\\nbar baz\\n: See foo"))
    <dl>
    <dt id="foo">foo</dt>
    <dd>Overused example</dd>
    <dt id="bar-baz">bar baz</dt>
    <dd>See foo</dd>
    </dl>

    """

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add("def_id", DefIdProcessor(md), "_end")

class ClassifyProcessor(treeprocessors.Treeprocessor):

    def __init__(self, md, tags, class_):
        super(ClassifyProcessor, self).__init__(md)
        self.tags = tags
        self.class_ = class_

    def run(self, doc):
        for el in doc.iter():
            if not el.get("class") and el.tag in self.tags:
                el.set("class", self.class_)

class Classify(Extension):
    """Add a class to tags.

    This is used to style elements created from markdown.

    >>> md = markdown.Markdown(extensions=[Classify(tags=['ul', 'ol'])])

    >>> print(md.convert("- a\\n- b"))
    <ul class="md">
    <li>a</li>
    <li>b</li>
    </ul>

    >>> print(md.convert("1. a\\n2. b"))
    <ol class="md">
    <li>a</li>
    <li>b</li>
    </ol>

    """

    def __init__(self, tags, **kw):
        super(Classify, self).__init__()
        self.tags = tags
        self.class_ = kw.get("class", "md")

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add(
            "classify",
            ClassifyProcessor(md, self.tags, self.class_),
            "_end")

class LinkTemplate(object):

    def __init__(self, config):
        self._text_pattern = self._pattern(config, 'text_pattern')
        self._link_pattern = self._pattern(config, 'link_pattern')
        self._text = config.get("text")
        self._href = config.get("href")
        self._class = config.get("class")
        self._arg_maps = config.get("arg_maps", [])
        self._attrs = config

    @staticmethod
    def _pattern(config, key):
        try:
            pattern = config[key]
        except KeyError:
            return None
        else:
            return re.compile(pattern + "$", re.DOTALL)

    def try_apply(self, link):
        unset = object()
        text_m = (
            self._text_pattern.match(link.text or "")
            if self._text_pattern
            else unset)
        link_m = (
            self._link_pattern.match(link.get("href", ""))
            if self._link_pattern
            else unset)
        if text_m is not None and link_m is not None:
            m_args = None
            if text_m is not unset:
                m_args = text_m.groups()
            if link_m is not unset:
                m_args = (m_args or ()) + link_m.groups()
            if m_args is not None:
                args = self._format_args(m_args)
                self._apply_text(args, link)
                self._apply_href(args, link)
                self._apply_class(args, link)
                self._apply_attrs(("target",), args, link)

    def _format_args(self, args):
        for arg, arg_map in self._zip_longest(args, self._arg_maps):
            mapped = arg_map.get(arg, arg) if arg_map else arg
            args += (mapped,)
        return args + ("",) * 10

    @staticmethod
    def _zip_longest(a, b):
        try:
            zip_longest = itertools.zip_longest
        except AttributeError:
            return map(None, a, b)
        else:
            return zip_longest(a, b)

    def _apply_text(self, args, link):
        if self._text and (not link.text or self._text_pattern):
            link.text = self._text.format(*args).strip()

    def _apply_href(self, args, link):
        if self._href and (not link.get("href") or self._link_pattern):
            link.set("href", self._href.format(*args).strip())

    def _apply_class(self, args, link):
        if self._class:
            cur = link.get("class")
            formatted = self._class.format(*args).strip()
            link.set("class", " ".join((cur, formatted)) if cur else formatted)

    def _apply_attrs(self, attrs, args, link):
        for name in attrs:
            try:
                val = self._attrs[name]
            except KeyError:
                pass
            else:
                link.set(name, val.format(*args).strip())

class LinkProcessor(treeprocessors.Treeprocessor):

    def __init__(self, md, templates):
        super(LinkProcessor, self).__init__(md)
        self._templates = [LinkTemplate(t) for t in templates]

    def run(self, doc):
        for link in doc.iter("a"):
            for t in self._templates:
                if t.try_apply(link):
                    break

class Link(Extension):
    """Extends markdown links using simple templates.

    Templates are specified as a list of attributes:

    >>> templates = []

    Templates match links on their text and link attributes:

        [text](link)

    Patterns are configued as regular expressions in the
    `text_pattern` and `link_pattern` attributes:

    >>> simple_template = {
    ...   "text_pattern": r"\$text",
    ...   "link_pattern": r"\$link"
    ... }
    >>> templates.append(simple_template)

    At least one pattern is required. If both are specified, both must
    match a link for the template to apply.

    Patterns may include regular expression groups to capture values
    from the link text and link attributes. Captured values are
    referred to as *template arguments*. Argument order is preserved
    based on the captured group order starting with link text followed
    by the link attribute.

    >>> arg_template = {
    ...   "text_pattern": r"\$text (.+)",
    ...   "link_pattern": r"\$link ([^ ]+) ([^ ]+)"
    ... }
    >>> templates.append(arg_template)

    In this example, template arguments would be presented as three
    values: the one captured text arg followed by the two captured
    link args.

    When a template matches a link, template attributes are applied to
    the link. Template attributes may include:

     - text
     - href
     - class
     - target

    >>> simple_template.update({
    ...   "text": "a simple link",
    ...   "href": "simple.html"
    ... })

    Attribute values may Python's advanced string formatting (PEP
    3101) to include placeholders for argument values. Arguments
    applied in order using Python's string `format` method.

    >>> arg_template.update({
    ...   "text": "Go to {0}",
    ...   "href": "{1}",
    ...   "class": "{2}"
    ... })

    If a template provides `text` but does not provide `text_pattern`
    a special rule applies: the links original text value takes
    precedence over the template's. Here's an example that uses
    `link_pattern` to match and provides `text`:

    >>> link_template = {
    ...   "link_pattern": "link\.html",
    ...   "text": "My link"
    ... }
    >>> templates.append(link_template)

    In this case, `text` will be used only if the link text is empty,
    otherwise the link text will be unaltered. This allows templates
    to provide default text values that are used when the link text is
    not provided.

    The `target` attribute may be used to specify the link's
    target. Here's a template that uses a pattern in the link text to
    implement a link that opens in a new window/tab:

    >>> ext_link_template = {
    ...   "text_pattern": r"(.+?) ->",
    ...   "text": "{}",
    ...   "class": "ext",
    ...   "target": "_blank"
    ... }
    >>> templates.append(ext_link_template)

    Templates may also provide an `arg_maps` list of dicts, which map
    user-provided arg values to template-defined values. Items in the
    arg maps list correspond to the positional arguments defined in
    the templates.

    Mapped arguments are appended to the list of arguments used for
    formatting in the order corresponding to their position in the
    `arg_maps` list. For example, if there is a single arg map, a
    single additional mapped argument will be appended to the argument
    list. If there are two maps, two additional arguments will be
    appended, and so on.

    Here's an example of a template that maps the first (an only)
    argument and uses the mapped value as its text while using the
    original value as its href attribute.

    >>> arg_maps_template = {
    ...   "link_pattern": "mapped:(.+?)",
    ...   "href": "{0}",
    ...   "text": "{1}",
    ...   "arg_maps": [{ "a": "A", "b": "B", "c": "C" }]
    ... }
    >>> templates.append(arg_maps_template)

    Let's initialize markdown with our extension and sample templates:

    >>> md = markdown.Markdown(extensions=[Link(templates)])

    In the case of the simple template, we have to match on both text
    and link because both patterns are provided:

    >>> print(md.convert("[$text]($link)"))
    <p><a href="simple.html">a simple link</a></p>

    If either does not match, the template isn't applied:

    >>> print(md.convert("[text]($link)"))
    <p><a href="$link">text</a></p>

    >>> print(md.convert("[$text](link)"))
    <p><a href="link">$text</a></p>

    The argument template also uses both text and links to match:

    >>> print(md.convert("[$text Foo]($link foo bar)"))
    <p><a class="bar" href="foo">Go to Foo</a></p>

    The link template can be used with text:

    >>> print(md.convert("[click here](link.html)"))
    <p><a href="link.html">click here</a></p>

    It can also be used without text, in which case the template text
    is used:

    >>> print(md.convert("[](link.html)"))
    <p><a href="link.html">My link</a></p>

    Here's an example of using a text pattern to implement an external
    link (i.e. a link that opens in a new tab/window):

    >>> print(md.convert("[Open ->](external.html)"))
    <p><a class="ext" href="external.html" target="_blank">Open</a></p>

    Argument maps are applied to user-provided arguments:

    >>> print(md.convert("[](mapped:a)"))
    <p><a href="a">A</a></p>

    """

    def __init__(self, templates):
        super(Link, self).__init__()
        self._templates = templates

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add(
            "custom_link",
            LinkProcessor(md, self._templates),
            ">inline")

class PagesIndex(object):

    def __init__(self):
        assert nav_pages, "nav_resolve plugin is required"
        self._by_tag = {}
        for page in nav_pages:
            for tag in self._page_tags(page):
                self._by_tag.setdefault(tag, []).append(page)

    @staticmethod
    def _page_tags(page):
        return [s.strip() for s in page.meta.get("tags", "").split(",")]

    def iter_pages(self, url_prefix, tag):
        for page in self._by_tag.get(tag, []):
            if page.abs_url.startswith(url_prefix):
                yield page

class CategoriesProcessor(treeprocessors.Treeprocessor):

    def run(self, doc):
        if nav_pages_index is None:
            log.info("Generating nav pages index")
            globals()["nav_pages_index"] = PagesIndex()
        for ul in doc.iter("ul"):
            if self._is_category_list(ul):
                self._apply_category_list(ul, nav_pages_index)

    @staticmethod
    def _is_category_list(ul):
        link = ul.find("li/a")
        return link is not None and link.get("href", "").startswith("category")

    def _apply_category_list(self, ul, index):
        links = ul.findall("li/a")
        ul.clear()
        ul.set("class", "categorized-view")
        categories = {}
        for link in links:
            cat_info = self._try_cat_info(link)
            if not cat_info:
                continue
            url_prefix, cat_tag, cat_title = cat_info
            li = etree.Element("li")
            ul.append(li)
            if cat_title:
                h5 = etree.Element("h5")
                li.append(h5)
                h5.text = cat_title
            for page in index.iter_pages(url_prefix, cat_tag):
                a = etree.Element("a")
                li.append(a)
                a.text = page.meta.get("overview_title") or page.title
                a.set("href", page.abs_url)

    @staticmethod
    def _try_cat_info(link):
        href = link.get("href", "")
        if not href.startswith("category:"):
            return None
        parts = href[9:].split("#", 1)
        if len(parts) != 2:
            log.warning("invalid category URL '%s' (missing hash)", href)
            return None
        return parts + [link.text]

class Categories(Extension):
    """Generates a categorized view."""

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add("categories", CategoriesProcessor(md), ">inline")

class BacktickPattern(inlinepatterns.BacktickPattern):

    def __init__(self):
        super(BacktickPattern, self).__init__(inlinepatterns.BACKTICK_RE)

    def handleMatch(self, m):
        el = super(BacktickPattern, self).handleMatch(m)
        if m.group(4) and m.group(3) == "``":
            el.set("class", "lit")
        return el

class Backtick(Extension):
    """Replaces default backtick support with an extended version.

    Guild distinguishes between single and double backticks. Single
    backticks are used for literal text while double backticks are
    used for code samples.

    The extension preserves the use of code tags as per the markdown
    specification but adds the class 'lit' (literal) to code tags
    generated from double backticks.

    To illustrate, we'll initialize markdown with the extension:

    >>> md = markdown.Markdown(extensions=[Backtick()])

    Here are the two code version:

    >>> print(md.convert("`term`"))
    <p><code>term</code></p>

    >>> print(md.convert("``code sample``"))
    <p><code class="lit">code sample</code></p>

    """

    def extendMarkdown(self, md, _globals):
        md.inlinePatterns["backtick"] = BacktickPattern()

class RefProcessor(treeprocessors.Treeprocessor):

    def run(self, doc):
        for link in doc.iter("a"):
            href = link.get("href", "")
            if href.startswith("ref:"):
                ref = href[4:]
                link.set("href", "#" + ref)
                link.set("class", "ref")
                target = doc.find("*[@id='{}']".format(ref))
                if target is not None:
                    link.text = self._el_text(target)

    @staticmethod
    def _el_text(el):
        return etree.tostring(el, method="text").strip().decode("UTF-8")

class Ref(Extension):
    """Replaces link text with a referenced target text.

    References are specified using a link in the format:

        ref:REF

    where REF is the ID of an element on the same page.

    The plugin will replace the link text with that of the target
    element. It will also add the 'ref' class to the link for optional
    styling.

    This plugin is designed to work in conjunction with the toc
    plugin, which assigns id slugs to headers.

    >>> md = markdown.Markdown(extensions=["toc", Ref()])

    Here's a basic example of a reference:

    >>> print(md.convert("[](ref:hello)\\n## hello"))
    <p><a class="ref" href="#hello">hello</a></p>
    <h2 id="hello">hello</h2>

    Target text is stripped of its markup:

    >>> print(md.convert("[](ref:hello-there)\\n## hello *there*"))
    <p><a class="ref" href="#hello-there">hello there</a></p>
    <h2 id="hello-there">hello <em>there</em></h2>

    """

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add("ref", RefProcessor(md), "_end")

class FigureProcessor(treeprocessors.Treeprocessor):

    def run(self, root):
        prev = None
        for el in root:
            if (el.tag == "p" and
                el.text and el.text.startswith("^ ") and
                prev is not None):
                self._apply_figure(prev, el, root)
            self.run(el)
            prev = el

    @staticmethod
    def _apply_figure(target, caption, parent):
        for i, el in zip(range(len(parent)), parent):
            if el is target:
                parent.remove(target)
                parent.remove(caption)
                figure = etree.Element("figure")
                parent.insert(i, figure)
                figure.append(target)
                figure.append(caption)
                caption.tag = "figcaption"
                caption.text = caption.text[2:]
                break
        else:
            raise AssertionError()

class Figure(Extension):
    """Support HTML figure element with captions.

    Figures are designated by adding a caption below the figure
    content. Captions must occur as a separate block and on a single
    line starting with "^ ". For example, to create a figure for an
    image:

        ![](img.png)

        ^ A sample image

    Let's configure markdown with our extension:

    >>> md = markdown.Markdown(extensions=["tables", Figure()])

    We can use a caption to create a figure containing an image:

    >>> print(md.convert("![](img.png)\\n\\n^ A sample image"))
    <figure><p><img alt="" src="img.png" /></p>
    <figcaption>A sample image</figcaption>
    </figure>

    Here's a table figure:

    >>> print(md.convert("a | b\\n--- | ---\\nc | d\\n\\n^ A sample image"))
    <figure><table>
    <thead>
    <tr>
    <th>a</th>
    <th>b</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>c</td>
    <td>d</td>
    </tr>
    </tbody>
    </table>
    <figcaption>A sample image</figcaption>
    </figure>

    """

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add("figure", FigureProcessor(md), "_end")

class FencedCodeProcessor(fenced_code.FencedBlockPreprocessor):

    LANG_TAG = ' class="language-%s"'

class FencedCode(Extension):

    def extendMarkdown(self, md, _globals):
        md.preprocessors["fenced_code_block"] = FencedCodeProcessor(md)

class CmdHelpContext(object):

    def __init__(self, cmd_help):
        self._cmd_url_base = self._init_cmd_url_base(cmd_help)

    @staticmethod
    def _init_cmd_url_base(cmd_help):
        prog = cmd_help["usage"]["prog"]
        cmd_path = prog.split(" ")[1:]
        return "/docs/commands/{}".format("-".join(cmd_path))

    def cmd_url(self, cmd):
        return self._cmd_url_base + "-{}-cmd/".format(cmd)

class CmdHelpProcessor(treeprocessors.Treeprocessor):

    _marker_re = re.compile(r"\[CMD-HELP (.+?)\]$")

    def __init__(self, md, src_path):
        super(CmdHelpProcessor, self).__init__(md)
        self._src_path = src_path
        env = jinja2.Environment(loader=jinja2.FileSystemLoader("src"))
        env.filters.update({
            "format_text": self._format_text_filter,
            "cmd_url": self._cmd_url_filter,
        })
        self._md = markdown.Markdown(extensions=[
            Backtick(),
            AutoUrl(),
            CmdHelpUrl(),
        ])
        self._template = env.get_template("cmd-help.html")

    def _format_text_filter(self, text):
        if text == "Show this message and exit.":
            return "Show command help and exit."
        else:
            return self._md.convert(text)

    def _cmd_url_filter(self, cmd, ctx):
        cmd_name = cmd["term"].split(", ")[0]
        return ctx.cmd_url(cmd_name)

    def run(self, root):
        for el in root:
            if el.tag == "p":
                m = self._marker_re.match(el.text or "")
                if m:
                    self._handle_cmd(m.group(1), el, root)

    def _handle_cmd(self, cmd, target, parent):
        cmd_help = self._get_cmd_help(cmd)
        ctx = CmdHelpContext(cmd_help)
        rendered = self._template.render(cmd=cmd_help, ctx=ctx)
        help_el = etree.fromstring(rendered)
        _replace_el(parent, target, help_el)

    def _get_cmd_help(self, cmd):
        cmd_help = self._get_cached_cmd_help(cmd)
        if cmd_help is None:
            log.info("Generating help for '%s' command", cmd)
            args = ["guild"] + shlex.split(cmd) + ["--help"]
            env = {"GUILD_HELP_JSON": "1"}
            env.update(os.environ)
            out = subprocess.check_output(args, env=env)
            cmd_help = json.loads(out.decode("UTF-8"))
            self._cache_cmd_help(cmd, cmd_help)
        return cmd_help

    def _get_cached_cmd_help(self, cmd):
        cache_path = self._cached_cmd_help_filename(cmd)
        if not os.path.exists(cache_path):
            return None
        src_path = self._cmd_source(cmd)
        if os.path.getmtime(src_path) > os.path.getmtime(cache_path):
            return None
        return json.load(open(cache_path, "r"))

    @staticmethod
    def _cached_cmd_help_filename(cmd):
        basename = cmd.replace(" ", "-")
        return "/tmp/guild-ai-cmd-help/{}.json".format(basename)

    def _cmd_source(self, cmd):
        basename = re.sub(r"[ \-]", "_", cmd)
        patterns = [
            os.path.join(self._src_path, "{}.py"),
            os.path.join(self._src_path, "{}_.py"),
        ]
        for p in patterns:
            path = p.format(basename)
            if os.path.exists(path):
                return path
        raise AssertionError(cmd)

    def _cache_cmd_help(self, cmd, cmd_help):
        path = self._cached_cmd_help_filename(cmd)
        path_dir = os.path.dirname(path)
        try:
            os.makedirs(path_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        json.dump(cmd_help, open(path, "w"))

def _replace_el(parent, target_el, new_el):
    for i, el in zip(range(len(parent)), parent):
        if el is target_el:
            parent.remove(target_el)
            parent.insert(i, new_el)
            break
    else:
        raise AssertionError()

class CmdHelp(Extension):
    """Replaces [CMD-HELP <cmd>] with formatted Guild command help.
    """

    def __init__(self, src_path):
        self._src_path = src_path

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add(
            "cmd-help",
            CmdHelpProcessor(md, self._src_path),
            "_end")

class PkgHelpProcessor(treeprocessors.Treeprocessor):

    _marker_re = re.compile(r"\[PKG-HELP (.+?)\]$")

    def __init__(self, md, src_path):
        super(PkgHelpProcessor, self).__init__(md)
        self._src_path = src_path
        env = jinja2.Environment(loader=jinja2.FileSystemLoader("src"))
        env.filters.update({
            "slugify": _slugify,
            "format_desc": self._format_desc,
            "format_reference": self._format_reference,
            "format_resource_source": self._format_resource_source,
            "public": self._public,
        })
        self._template = env.get_template("pkg-help.html")

    @staticmethod
    def _format_desc(desc):
        if desc and desc[-1] != ".":
            desc = desc + "."
        return desc

    @staticmethod
    def _format_reference(url):
        patterns = [
            (r"https://arxiv.org/abs/(.*)$",
             "arXiv: {}"),
            (r"https://github.com/([^/]+)/([^/]+)/blob/[^/]+/(.+)$",
             "GitHub: {}/{}/{}"),
        ]
        for pattern, repl in patterns:
            m = re.match(pattern, url)
            if m:
                return repl.format(*m.groups())
        return url

    @staticmethod
    def _public(items):
        return [item for item in items if not getattr(item, "private", False)]

    def _format_resource_source(self, source):
        if source.uri.startswith("operation:"):
            return self._format_op_source(source.uri[10:], source)
        elif source.uri.startswith("file:"):
            return self._format_file_source(source.uri[5:])
        else:
            return self._format_url_source(source.uri)

    def _format_op_source(self, spec, source):
        ops = [op.strip() for op in spec.split(",")]
        if len(ops) == 1:
            return (
                '<code class="lit">{}</code> from {} operation'.format(
                    ", ".join(source.select),
                    self._op_link(ops[0], source)))
        else:
            comma_list = ", ".join([
                self._op_link(op, source) for op in ops[:-1]
            ])
            last = self._op_link(ops[-1], source)
            return (
                '<code class="lit">{}</code> from {} or {} operations'.format(
                    source.select, comma_list, last))

    @staticmethod
    def _op_link(op, source):
        model_slug = _slugify(source.resdef.modeldef.name)
        op_parts = op.split(":", 1)
        if len(op_parts) == 2:
            op_name = op_parts[1]
        else:
            op_name = op_parts[0]
        op_slug = _slugify(op_name)
        target = "{}-{}".format(model_slug, op_slug)
        return '<a href="#{}">{}</a>'.format(target, op)

    @staticmethod
    def _format_file_source(path):
        return '<code class="lit">{}</code>'.format(path)

    @staticmethod
    def _format_url_source(url):
        patterns = [
            (r"https://raw.githubusercontent.com/([^/]+)/([^/]+)/[^/]+/(.+)$",
             "https://raw.githubusercontent.com/{}/{}/.../{}"),
        ]
        for pattern, repl in patterns:
            m = re.search(pattern, url)
            if m:
                text = repl.format(*m.groups())
                break
        else:
            text = url
        return (
            '<a href="{}" class="ext" target="_blank">{}</a>'.format(
                url, text))

    def run(self, root):
        for el in root:
            if el.tag == "p":
                m = self._marker_re.match(el.text or "")
                if m:
                    self._handle_pkg(m.group(1), el, root)

    def _handle_pkg(self, path, target, parent):
        pkg = self._get_pkg(path)
        models = self._get_models(path)
        rendered = self._template.render(models=models, pkg=pkg)
        try:
            help_el = etree.fromstring(rendered)
        except Exception:
            for i, line in enumerate(rendered.split("\n")):
                print("%4i: %s" % (i + 1, line))
            raise
        _replace_el(parent, target, help_el)

    def _get_models(self, path):
        gf = guildfile.from_dir(os.path.join(self._src_path, path))
        return [gf.models[name] for name in sorted(gf.models)]

    def _get_pkg(self, path):
        pkg_dir = os.path.join(self._src_path, path)
        gf = guildfile.from_dir(pkg_dir)
        if not gf.package:
            raise AssertionError("no package in {}".format(gf.src))
        return gf.package

class PkgHelp(Extension):
    """Replaces [PKG-HELP <cmd>] with formatted model help.
    """

    def __init__(self, src_path):
        self._src_path = src_path

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add(
            "pkg-help",
            PkgHelpProcessor(md, self._src_path),
            "_end")

class UrlPattern(inlinepatterns.Pattern):
    """Adapted from markdown-urlize.

    https://github.com/r0wb0t/markdown-urlize/blob/master/mdx_urlize.py
    """

    def handleMatch(self, m):
        url = m.group(2)
        if url.startswith("<"):
            url = url[1:-1]
        text = url
        if not url.split("://")[0] in ("http", "https", "ftp"):
            if "@" in url and not "/" in url:
                url = "mailto:" + url
            else:
                url = "http://" + url
        el = markdown.util.etree.Element("a")
        el.set("href", url)
        el.text = markdown.util.AtomicString(text)
        return el

class AutoUrl(markdown.Extension):
    """Converts URLs into links.

    Adapted from markdown-urlize.

    https://github.com/r0wb0t/markdown-urlize/blob/master/mdx_urlize.py

    >>> md = markdown.Markdown(extensions=[AutoUrl()])

    Various URLs:

    >>> print(md.convert("http://food.com"))
    <p><a href="http://food.com">http://food.com</a></p>

    >>> print(md.convert("https://food.com/#bar"))
    <p><a href="https://food.com/#bar">https://food.com/#bar</a></p>

    """

    def extendMarkdown(self, md, _globals):
        link_pattern = "(%s)" % "|".join([
            r"<(?:f|ht)tps?://[^>]*>",
            r"\b(?:f|ht)tps?://[^)<>\s]+[^.,)<>\s]",
            r"\bwww\.[^)<>\s]+[^.,)<>\s]",
            r"[^(<\s]+\.(?:com|net|org)\b",
        ])
        md.inlinePatterns["auto-link"] = UrlPattern(link_pattern, md)

class CmdHelpUrlProcessor(treeprocessors.Treeprocessor):

    cmd_re = re.compile(r"guild\s(.+?)\s--help")

    def run(self, root):
        for el in root.iter("code"):
            m = self.cmd_re.match(el.text or "")
            if m:
                el.tag = "a"
                el.set("class", "cmd")
                cmd = " ".join(m.groups())
                el.text = cmd
                href = "/docs/commands/{}-cmd/".format(cmd.replace(" ", "-"))
                el.set("href", href)

class CmdHelpUrl(Extension):
    """Creates links to help commands.

    Links are checked within `<code>` blocks for the form `guild
    CMD --help`.

    Let's configure markdown with our extension along with the backtick
    extension to support inline code syntax (``...``).

    >>> md = markdown.Markdown(extensions=[Backtick(), CmdHelpUrl()])

    A link to `run` help:

    >>> print(md.convert("``guild run --help``"))
    <p><a class="cmd" href="/docs/commands/run-cmd/">run</a></p>

    A link to `runs rm` help:

    >>> print(md.convert("``guild runs rm --help``"))
    <p><a class="cmd" href="/docs/commands/runs-rm-cmd/">runs rm</a></p>

    """

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add("cmd-help-url", CmdHelpUrlProcessor(md), "_end")

class MoveToc(Extension):
    """Moves toc processor to end position.
    """

    def extendMarkdown(self, md, _globals):
        toc = md.treeprocessors.pop("toc")
        md.treeprocessors.add("toc", toc, "_end")

class DeflistToTableProcessor(treeprocessors.Treeprocessor):

    def run(self, root):
        for dl in root.iter("dl"):
            self._dl_to_table(dl)

    def _dl_to_table(self, dl):
        dl.tag = "div"
        dl.set("class", "dl")
        rows = []
        dl_children = iter(list(dl))
        while True:
            try:
                dt = next(dl_children)
                dd = next(dl_children)
            except StopIteration:
                break
            dl.remove(dt)
            dl.remove(dd)
            rows.append(self._def_row(dt, dd))
        dl.extend(rows)

    @staticmethod
    def _def_row(dt, dd):
        row = etree.Element("div")
        row.set("class", "row")
        row.append(dt)
        row.append(dd)
        dt.tag = "div"
        dt.set("class", "dt col col-sm-4 col-lg-3")
        dd.tag = "div"
        dd.set("class", "dd col col-sm-8 col-lg-9")
        return row

    def _dl_to_table_old(self, dl):
        dl.tag = "table"
        dl.set("class", "table dl")
        rows = []
        dl_children = iter(list(dl))
        while True:
            try:
                dt = next(dl_children)
                dd = next(dl_children)
            except StopIteration:
                break
            dl.remove(dt)
            dl.remove(dd)
            rows.append(self._def_row(dt, dd))
        dl.extend(rows)

    @staticmethod
    def _def_row_old(dt, dd):
        row = etree.Element("tr")
        row.append(dt)
        row.append(dd)
        dt.tag = "td"
        dt.set("class", "dt")
        dd.tag = "td"
        dd.set("class", "dd")
        return row

class DeflistToTable(Extension):
    """Converts deflists to tables.

    Adds "dl", "dt", and "dd" classes to the table and two td elements
    respectively.

    To illustrate we'll configure markdown with both the "def_list"
    extension and our extension.

    >>> md = markdown.Markdown(extensions=["def_list", DeflistToTable()])

    Here's a single term list:

    >>> print(md.convert("term1\\n: term1 def"))
    <table class="table dl">
    <tr><td class="dt">term1</td>
    <td class="dd">term1 def</td>
    </tr></table>

    Two terms:

    >>> print(md.convert("term1\\n: term1 def\\n\\nterm2\\n: term2 def"))
    <table class="table dl">
    <tr><td class="dt">term1</td>
    <td class="dd">term1 def</td>
    </tr><tr><td class="dt">term2</td>
    <td class="dd">term2 def</td>
    </tr></table>

    """

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add(
            "deflist-to-table",
            DeflistToTableProcessor(md),
            "_end")

class Serve(BasePlugin):

    def on_serve(self, server, config):
        builder = self._builder_func(server)
        def task(ignore=None):
            if ignore is not None:
                ignore = self._ignore_func(ignore)
            return {
                "func": builder,
                "ignore": ignore,
                "delay": None
            }
        server.watcher._tasks = {
            "mkdocs.yml": task(),
            "pages": task(),
            "src": task([r"\.scss$", "\.map$"])
        }

    @staticmethod
    def _builder_func(server):
        assert len(server.watcher._tasks)
        task0 = list(server.watcher._tasks.values())[0]
        builder = task0["func"]
        assert builder.__name__ == "builder"
        return builder

    @staticmethod
    def _ignore_func(patterns):
        patterns = [re.compile(p) for p in patterns]
        def ignore(path):
            return any((p.search(path) for p in patterns))
        return ignore

def test():
    import doctest
    import sys
    failed, _count = doctest.testmod(
        optionflags=(
            doctest.REPORT_ONLY_FIRST_FAILURE |
            doctest.NORMALIZE_WHITESPACE))
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    test()

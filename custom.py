from __future__ import absolute_import

import re
import shlex

from markdown.extensions import Extension
from markdown.extensions.toc import slugify
from markdown import inlinepatterns
from markdown import treeprocessors
from markdown.util import etree

import mkdocs.config as _ # work around for mkdocs import cycle

from mkdocs.plugins import BasePlugin
from mkdocs.nav import Page, Header

class NavResolvePlugin(BasePlugin):

    def on_nav(self, nav, config):
        """Process nav items

        We use page meta for nav title and other config settings so we
        need to read the page source. To avoid re-reading we disable
        the read_source function.
        """
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
        children = toc.getchildren()
        if len(children) != 1 or children[0].tag != "ul":
            raise AssertionError(etree.tostring(toc))
        ul = children[0]
        toc.tag = "ol"
        toc.remove(ul)
        items = ul.getchildren()
        if len(items) == 1:
            item1 = items[0]
            item1_children = item1.getchildren()
            if (len(item1_children) != 2 or
                item1_children[0].tag != "a" or
                item1_children[1].tag != "ul"):
                raise AssertionError(etree.tostring(item1))
            items = item1_children[1].getchildren()
        toc.extend(items)

    @staticmethod
    def _ul_to_ol(toc):
        for item in toc.iter():
            if item.tag == "ul":
                item.tag = "ol"

class FixToc(Extension):
    """Reformats toc elements

    Changes to toc:

    - Outer div is replaced by ol with "toc" class

    - If there's a single level 1 entry, that entry is removed end
      its child entries are promoted to level 1

    To illustrate, we'll configure markdown with TocExtension and our
    extension:

    >>> import markdown
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

    """

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add("fix_toc", FixTocProcessor(md), "_end")

class DefIdProcessor(treeprocessors.Treeprocessor):

    def run(self, doc):
        for dt in doc.iter("dt"):
            dt.set("id", slugify(dt.text, "-"))

class DefinitionId(Extension):
    """Adds ids to definition terms

    With ids, definition terms can be referenced within a page using
    hashes.

    Ids are generated using the toc extension's slugify function using
    "-" as the separator.

    To illustrate, let's configure markdown with DefinitionList and
    our extension:

    >>> import markdown
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

class TagListProcessor(treeprocessors.Treeprocessor):

    def run(self, doc):
        for el in doc.iter():
            if el.tag in ["ul", "ol"] and not el.get("class"):
                el.set("class", el.tag)

class TagList(Extension):
    """Adds 'ul' and 'ol' classes to ul and ol elements respectively

    This is used to style unordered and ordered lists.

    To illustrate, we'll configure markdown with our extension:

    >>> import markdown
    >>> md = markdown.Markdown(extensions=[TagList()])

    >>> print(md.convert("- a\\n- b"))
    <ul class="ul">
    <li>a</li>
    <li>b</li>
    </ul>

    >>> print(md.convert("1. a\\n2. b"))
    <ol class="ol">
    <li>a</li>
    <li>b</li>
    </ol>

    """

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add("tag_list", TagListProcessor(md), "_end")

class LinkTemplate(object):

    def __init__(self, config):
        self._text_pattern = self._pattern(config, 'text_pattern')
        self._link_pattern = self._pattern(config, 'link_pattern')
        self._text = config.get("text")
        self._href = config.get("href")
        self._class = config.get("class")
        self._attrs = config

    @staticmethod
    def _pattern(config, key):
        try:
            pattern = config[key]
        except KeyError:
            return None
        else:
            return re.compile(pattern + "$")

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
            args = None
            if text_m is not unset:
                args = text_m.groups()
            if link_m is not unset:
                args = (args or ()) + link_m.groups()
            if args is not None:
                padded_args = args + ("",) * 10
                self._apply_text(padded_args, link)
                self._apply_href(padded_args, link)
                self._apply_class(padded_args, link)
                self._apply_attrs(("target",), padded_args, link)

    def _apply_text(self, args, link):
        if self._text and (not link.text or self._text_pattern):
            link.text = self._text.format(*args)

    def _apply_href(self, args, link):
        if self._href and (not link.get("href") or self._link_pattern):
            link.set("href", self._href.format(*args))

    def _apply_class(self, args, link):
        if self._class:
            cur = link.get("class")
            formatted = self._class.format(*args)
            link.set("class", " ".join((cur, formatted)) if cur else formatted)

    def _apply_attrs(self, attrs, args, link):
        for name in attrs:
            try:
                val = self._attrs[name]
            except KeyError:
                pass
            else:
                link.set(name, val.format(*args))

class LinkProcessor(treeprocessors.Treeprocessor):

    def __init__(self, md, templates):
        super(LinkProcessor, self).__init__(md)
        self._templates = [LinkTemplate(t) for t in templates]

    def run(self, doc):
        for link in doc.iter("a"):
            for t in self._templates:
                t.try_apply(link)

    def _try_apply_alias(self, link):
        href = link.get("href")
        m = self.alias_pattern.match(href)
        if m:
            try:
                alias = self.aliases[m.group(1)]
            except KeyError:
                pass
            else:
                args = shlex.split(m.group(2))
                padded_args = args + [""] * 10
                self._apply_alias(link, alias, padded_args)

    def _apply_alias(self, link, alias, args):
        self._try_apply_href(link, alias, args)
        self._try_apply_class(link, alias, args)
        if not link.text:
            self._try_apply_text(link, alias, args)

    @staticmethod
    def _try_apply_href(link, alias, args):
        try:
            template = alias["href"]
        except KeyError:
            pass
        else:
            link.set("href", template.format(*args))

    @staticmethod
    def _try_apply_class(link, alias, args):
        try:
            template = alias["class"]
        except KeyError:
            pass
        else:
            cur_class = link.get("class", "")
            new_class = template.format(*args)
            cls = cur_class + " " + new_class if cur_class else new_class
            link.set("class", cls)

    @staticmethod
    def _try_apply_text(link, alias, args):
        try:
            template = alias["text"]
        except KeyError:
            pass
        else:
            link.text = template.format(*args)

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

    Let's initialize markdown with our extension and sample templates:

    >>> import markdown
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

    """

    def __init__(self, templates):
        super(Link, self).__init__()
        self._templates = templates

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add(
            "custom_link",
            LinkProcessor(md, self._templates),
            ">inline")

def test():
    import doctest
    import sys
    failed, _count = doctest.testmod(
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    test()

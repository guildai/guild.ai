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

class ExtLinkProcessor(treeprocessors.Treeprocessor):

    def run(self, doc):
        for link in doc.iter("a"):
            if link.text and link.text.endswith("->"):
                link.text = link.text[:-2].rstrip()
                cls = link.get("class")
                cls = cls + " ext" if cls else "ext"
                link.set("class", cls)
                link.set("target", "_blank")

class ExternalLink(Extension):
    """Modifies link syntax to support external links

    An external link is opened in a new window using target="_blank"
    and includes an "ext" class on the anchor element.

    External links are denoted by adding "->" to the end of the link
    text. This approach is compatible with other markdown processors.

    To illustrate, we'll configure markdown with our extension:

    >>> import markdown
    >>> md = markdown.Markdown(extensions=[ExternalLink()])

    Here's an external link:

    >>> print(md.convert("[Link ->](#)"))
    <p><a class="ext" href="#" target="_blank">Link</a></p>

    The default behavior is applied for non-external links:

    >>> print(md.convert("[Link](#)"))
    <p><a href="#">Link</a></p>

    Below are some edge case tests.

    Space not included before marker:

    >>> print(md.convert("[Link->](#)"))
    <p><a class="ext" href="#" target="_blank">Link</a></p>

    Text spans multiple lines:

    >>> print(md.convert("[Line 1\\nLine 2 ->](#)"))
    <p><a class="ext" href="#" target="_blank">Line 1
    Line 2</a></p>
    """

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add("external_link", ExtLinkProcessor(md), "_end")

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

class LinkAliasProcessor(treeprocessors.Treeprocessor):

    alias_pattern = re.compile(r"\$([^ ]+) ?(.*)$")

    def __init__(self, md, aliases):
        super(LinkAliasProcessor, self).__init__(md)
        self.aliases = aliases

    def run(self, doc):
        for link in doc.iter("a"):
            self._try_apply_alias(link)

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
    def _try_apply_text(link, alias, args):
        try:
            template = alias["text"]
        except KeyError:
            pass
        else:
            link.text = template.format(*args)

class LinkAlias(Extension):
    """Provides aliases for links

    Link aliases are provided as link URLs in standard Markdown
    links. Aliases are in the format:

        '$' + NAME ( + ' ' + ARG)*

    Examples:

        [link text]($my-alias)
        [link text]($my-alias arg1 arg2)

    Aliases are configured using a dict of alias names to alias
    config. An alias config consists of two optional template strings:
    'href' and 'text'. Templates are used to generate values for
    respective link href and text properties. Templates use Python's
    advanced string formatting (PEP 3101).

    Example config:

        {"my-alias": {"href": "/foo/{}", "text": "My alias"}

    If provided, the 'href' template is used to generate the href
    attribute for the link, given the alias arguments.

    If the link does not have a text value (e.g. markdown is
    "[](...)") and the 'text' template is provided, it is similarly
    used generate the link text value.

    Alias arguments are used to format values and are passed in the
    order specified in the alias link. If there aren't enough
    alias arguments for the template, empty strings are used.

    To illustrate, we'll configure markdown with LinkAlias and some
    sample aliases.

    >>> import markdown
    >>> aliases = {
    ...   "foo": {"href": "/foo#{}", "text": "Foo {}"},
    ...   "bar": {"href": "/bar/{0}/{1}", "text": "{2}"}
    ... }
    >>> md = markdown.Markdown(extensions=[LinkAlias(**aliases)])

    We can now use '$foo' as a link alias:

    >>> print(md.convert("[foo]($foo)"))
    <p><a href="/foo#">foo</a></p>

    In this case no arguments were provided and so empty strings where
    used to format the href attribute.

    Here's $foo with an argument:

    >>> print(md.convert("[foo]($foo a)"))
    <p><a href="/foo#a">foo</a></p>

    Arguments that aren't used by the template are ignored:

    >>> print(md.convert("[foo]($foo a b)"))
    <p><a href="/foo#a">foo</a></p>

    The bar alias uses position arguments for both link text and href.

    >>> print(md.convert("[]($bar a b Bar)"))
    <p><a href="/bar/a/b">Bar</a></p>

    If the link contains text, it is preserved:

    >>> print(md.convert("[My bar]($bar a b Bar)"))
    <p><a href="/bar/a/b">My bar</a></p>

    In this case, the third argument can be omitted as it's not used:

    >>> print(md.convert("[My bar]($bar a b)"))
    <p><a href="/bar/a/b">My bar</a></p>

    """

    def __init__(self, *args, **kw):
        self.aliases = kw
        super(LinkAlias, self).__init__(*args)

    def extendMarkdown(self, md, _globals):
        md.treeprocessors.add(
            "link_alias",
            LinkAliasProcessor(md, self.aliases),
            ">inline")

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

def test():
    import doctest
    import sys
    failed, _count = doctest.testmod(
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    test()

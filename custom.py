from __future__ import absolute_import

import re

from markdown.extensions import Extension
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

class ExtLinkPattern(inlinepatterns.LinkPattern):

    def __init__(self, md):
        super(ExtLinkPattern, self).__init__(inlinepatterns.LINK_RE, md)

    def handleMatch(self, m):
        el = super(ExtLinkPattern, self).handleMatch(m)
        if el.text.endswith("->"):
            el.text = el.text[:-2].rstrip()
            el.set("target", "_blank")
            el.set("class", "ext")
        return el

class ExternalLinks(Extension):
    """Modifies link syntax to support external links

    An external link is opened in a new window using target="_blank"
    and includes an "ext" class on the anchor element.

    External links are denoted by adding "->" to the end of the link
    text. This approach is compatible with other markdown processors.

    To illustrate, we'll configure markdown with our extension:

    >>> import markdown
    >>> md = markdown.Markdown(extensions=[ExternalLinks()])

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
        md.inlinePatterns["link"] = ExtLinkPattern(md)

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

    To illustrate, we'll configure markdown with the TocExtension and
    our extension:

    >>> import markdown
    >>> from markdown.extensions.toc import TocExtension
    >>> md = markdown.Markdown(extensions=[TocExtension(), FixToc()])

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

def test():
    import doctest
    import sys
    failed, _count = doctest.testmod(
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    test()

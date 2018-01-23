from __future__ import absolute_import

import re

from markdown.extensions import Extension
from markdown import inlinepatterns

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
        self._pattern = re.compile(r"(.*?[^ ]) ?->$")

    def handleMatch(self, m):
        el = super(ExtLinkPattern, self).handleMatch(m)
        m = self._pattern.match(el.text)
        if m:
            el.text = m.group(1)
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

    >>> md.convert("[Link ->](/link)")
    u'<p><a class="ext" href="/link" target="_blank">Link</a></p>'

    The default behavior is applied for non-external links:

    >>> md.convert("[Link](/link)")
    u'<p><a href="/link">Link</a></p>'
    """

    def extendMarkdown(self, md, _globals):
        md.inlinePatterns["link"] = ExtLinkPattern(md)

def test():
    import doctest
    import sys
    failed, _count = doctest.testmod(
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    test()

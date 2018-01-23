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

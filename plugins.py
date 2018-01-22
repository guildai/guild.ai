from mkdocs.plugins import BasePlugin

class NavResolvePlugin(BasePlugin):

    def on_nav(self, nav, config):
        """Process nav items

        We use page meta for nav title and other config settings so we
        need to read the page source. To avoid re-reading we disable
        the read_source function.
        """
        for page in nav:
            page.read_source(config)
            page.read_source = lambda **_kw: None
        return nav

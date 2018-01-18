<template>
  <div id="root">
    <site-header />
    <site-main class="main" />
    <site-footer />
  </div>
</template>

<script>
import SiteFooter from '~/components/site-footer.vue';
import SiteHeader from '~/components/site-header.vue';
import SiteMain from '~/components/site-main.vue';

export default {
  components: {
    SiteFooter,
    SiteHeader,
    SiteMain
  },

  head() {
    let canonical = `https://nuxtjs.org${this.$route.path}`;
    if (this.$store.state.locale !== 'en') {
      canonical = `https://${this.$store.state.locale}.nuxtjs.org${this.$route.path}`;
    }
    let link = [
      { rel: 'canonical', href: canonical },
      { rel: 'alternate', hreflang: 'en', href: `https://nuxtjs.org${this.$route.path}` }
    ];
    link.forEach((l) => {
      if (l.href.slice(-1) !== '/') {
        l.href = l.href + '/';
      }
    });
    return {
      htmlAttrs: {
        lang: this.$store.state.locale
      },
      link
    };
  },

  watch: {
    $route: 'hideMenus'
  },

  computed: {
    visible() {
      return this.$store.state.visibleHeader;
    }
  },

  methods: {
    hideMenus() {
      this.$store.commit('setFalse', 'mobileMenuOpen');
      this.$store.commit('setFalse', 'visibleAffix');
    }
  }
};
</script>

<style lang="scss" scoped>
$mobile-break: 48em;

.main {
  flex: 1;
  margin-top: 60px;

  @media (min-width: $mobile-break) {
    margin-top: 80px;
  }
}
</style>

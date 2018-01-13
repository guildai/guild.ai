<template>
  <div id="root">
    <site-header />
    <site-main class="main" />
    <site-footer />
  </div>
</template>

<!--
<navbar />
  <div>
    <navbar />
    <div :class="{'App--hidden': visible}">
      <nuxt />
      <site-footer />
    </div>
  </div>

-->

<script>
import SiteFooter from '~/components/site-footer.vue'
import SiteHeader from '~/components/site-header.vue'
import SiteMain from '~/components/site-main.vue'

export default {
  components: {
    SiteFooter,
    SiteHeader,
    SiteMain
  },

  head() {
    let canonical = `https://nuxtjs.org${this.$route.path}`
    if (this.$store.state.locale !== 'en') {
      canonical = `https://${this.$store.state.locale}.nuxtjs.org${this.$route.path}`
    }
    let link = [
      { rel: 'canonical', href: canonical },
      { rel: 'alternate', hreflang: 'en', href: `https://nuxtjs.org${this.$route.path}` }
    ]
    link.forEach((l) => {
      if (l.href.slice(-1) !== '/') {
        l.href = l.href + '/'
      }
    })
    return {
      htmlAttrs: {
        lang: this.$store.state.locale
      },
      link
    }
  },

  watch: {
    $route: 'setStore'
  },

  computed: {
    visible() {
      return this.$store.state.visibleHeader
    }
  },

  methods: {
    setStore() {
      if (this.$store.state.visibleHeader) {
        this.$store.commit('toggle', 'visibleHeader')
      }
      if (this.$store.state.visibleAffix) {
        this.$store.commit('toggle', 'visibleAffix')
      }
    }
  }
}
</script>

<style lang="scss" scoped>

.main {
  flex: 1;
}
</style>

<!--

.App {
  &--hidden {
    display: none;
    @media (min-width: 992px) {
      display: block;
    }
  }
}
</style>
-->

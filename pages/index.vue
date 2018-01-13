<template>
  <div>
    <section class="Landscape">
      <h2 class="Landscape__Title">
        {{ $store.state.lang.homepage.title }}
      </h2>
      <ul class="Landscape__List">
        <li class="Landscape__List__Item">
          <nuxt-link class="button button--green" to="/guide/installation">
            {{ $store.state.lang.links.get_started }}
          </nuxt-link>
        </li>
        <li class="Landscape__List__Item">
          <a class="button button--grey" href="https://github.com/nuxt/nuxt.js" target="_blank">
            {{ $store.state.lang.links.github }} ({{ $store.state.ghVersion }})
          </a>
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
import NuxtLogo from '~/components/VueToNuxtLogo.vue'
import NuxtFooter from '~/components/Footer.vue'

export default {
  components: {
    NuxtLogo,
    NuxtFooter
  },
  head() {
    return {
      title: this.$store.state.lang.homepage.meta.title,
      meta: [
        { name: 'description', hid: 'description', content: this.$store.state.lang.homepage.meta.description },
        // Open Grapg
        { name: 'og:title', content: this.$store.state.lang.homepage.meta.title },
        { name: 'og:description', content: this.$store.state.lang.homepage.meta.description },
        { name: 'og:type', content: 'website' },
        { name: 'og:url', content: 'https://nuxtjs.org' },
        { name: 'og:image', content: 'https://i.imgur.com/PzEm5j2.png' },
        // Twitter Card
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@guild_ai' },
        { name: 'twitter:title', content: this.$store.state.lang.homepage.meta.title },
        { name: 'twitter:description', content: this.$store.state.lang.homepage.meta.description },
        { name: 'twitter:image', content: 'https://i.imgur.com/PzEm5j2.png' },
        { name: 'twitter:image:alt', content: 'Nuxt.js Logo' }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.Landscape
{
  text-align: center;
  @media (min-width: 992px) {

  }
  &__Title {
    font-weight: 300;
    font-size: 45px;
    line-height: normal;
    color: #526488;
    word-spacing: 5px;
    @media (min-width: 992px) {
      font-size: 60px;
    }
  }
  &__List {
    list-style: none;
    margin: 0;
    padding: 0;
    &__Item {
      display: inline-block;
      padding: 15px;
      padding-bottom: 0;
    }
  }
}
</style>

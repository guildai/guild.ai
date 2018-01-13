<template>
  <div class="toolbar">
    <nuxt-link to="/">
      <img class="logo" src="~/static/logo_nav.svg" alt="Guild AI" />
    </nuxt-link>
    <site-nav :class="navClass" />
    <div class="actions">
      <i :class="toggleClass" @click="toggle" />
    </div>
  </div>
</template>

<script>
import SiteNav from './site-nav.vue';

export default {
  components: {
    SiteNav
  },

  computed: {
    navClass() {
      return this.$store.state.mobileMenuOpen ? 'nav' : 'nav hidden';
    },

    toggleClass() {
      return this.$store.state.mobileMenuOpen
        ? 'mdi mdi-close toggle'
        : 'mdi mdi-menu toggle';
    }
  },

  methods: {
    toggle() {
      this.$store.commit('toggle', 'mobileMenuOpen');
    }
  }
};
</script>

<style lang="scss" scoped>
$mobile-break: 48em;

.toolbar  {
  display: flex;
  align-items: center;
  color: #fff;

  .logo {
    height: 32px;
    margin-top: 9px;

    @media (min-width: $mobile-break) {
      height: 40px;
    }
  }

  .nav {
    &.hidden {
      display: none;
      @media (min-width: $mobile-break) {
        display: inherit;
      }
    }
  }

  .actions {
    display: flex;
    flex: 1;
    justify-content: flex-end;

    .toggle {
      font-size: 29px;

      @media (min-width: $mobile-break) {
        display: none;
      }
    }
  }
}
</style>

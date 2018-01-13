<template>
  <div class="nav">
    <site-search
      :class="searchClass"
      @focus="searching = true"
      @blur="searching = false" />
    <site-menu :class="menuClass" />
    <site-links class="links nav-item" />
  </div>
</template>

<script>
import SiteLinks from './site-links.vue';
import SiteMenu from './site-menu.vue';
import SiteSearch from './site-search.vue';

export default {
  components: {
    SiteLinks,
    SiteMenu,
    SiteSearch
  },

  data() {
    return {
      searching: false
    };
  },

  computed: {
    menuClass() {
      return this.searching
        ? ' menu nav-item'
        : 'menu nav-item expanded';
    },

    searchClass() {
      return this.searching
        ? 'search nav-item expanded'
        : 'search nav-item';
    }
  }
};
</script>

<style lang="scss" scoped>
$mobile-break: 48em;

.nav {
  display: block;
  position: fixed;
  z-index: 995;
  top: 60px;
  left: 0;
  right: 0;
  bottom: 0;
  overflow-y: auto;
  color: rgba(#000, 0.87);
  background-color: #fff;

  @media (min-width: $mobile-break) {
    position: inherit;
    color: inherit;
    background-color: inherit;
    display: flex;
    width: 100%;

    .nav-item {
      margin-left: 15px;
    }

    .expanded {
      flex: 1;
    }

    .menu {
      order: 1;
    }

    .search {
      order: 2;
    }

    .links {
      order: 3;
    }
  }
}
</style>

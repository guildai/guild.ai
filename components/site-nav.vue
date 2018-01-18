<template>
  <div class="nav">
    <div :class="'spacer ' + searchingClass" />
    <site-search
      :class="'search nav-item ' + searchingClass"
      @focus="searching = true"
      @blur="searching = false" />
    <site-menu :class="'menu nav-item ' + searchingClass" />
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
    searchingClass() {
      return this.searching ? 'searching' : '';
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
      margin-left: 30px;
    }

    .spacer {
      order: 1;
      flex: 1;
    }

    .spacer.searching {
      _flex: 0;
    }

    .menu {
      order: 2;
    }

    .menu.searching {
      display: none;
      _flex: 1;
    }

    .search {
      order: 3;
    }

    .search.searching {
      min-width: 640px;
      _flex: 1;
    }

    .links {
      order: 4;
    }
  }
}
</style>

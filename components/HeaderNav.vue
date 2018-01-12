<template>
  <nav class="Nav" :class="{'Nav--hidden': !visible}">
    <div :class="{'Nav__Spacer search': search, 'Nav__Spacer' : !search}" />
    <div :class="{'Nav__Search search': search, 'Nav__Search' : !search}">
      <nuxt-header-nav-search @focus="search = true" @blur="search = false" />
    </div>
    <div class="Nav__Menu">
      <nuxt-header-nav-menu />
    </div>
    <div class="Nav__Links">
      <a href="https://github.com/guildai/guild" target="_blank" class="Nav__Links__Item"
         :title="$store.state.lang.tooltips.github_repo">
        <i class="mdi mdi-github-circle"></i>
      </a>
    </div>
  </nav>
</template>

<script>
import NuxtHeaderNavSearch from '~/components/HeaderNavSearch.vue'
import NuxtHeaderNavMenu from '~/components/HeaderNavMenu.vue'
import NuxtHeaderNavLang from '~/components/HeaderNavLang.vue'

export default {
  data() {
    return {
      search: false
    }
  },
  computed: {
    visible() { return this.$store.state.visibleHeader }
  },
  components: {
    NuxtHeaderNavSearch,
    NuxtHeaderNavMenu,
    NuxtHeaderNavLang
  }
}
</script>

<style lang="scss" scoped>
.Nav {
  display: block;
  position: fixed;
  z-index: 995;
  top: 60px;
  left: 0;
  right: 0;
  bottom: 0;
  overflow-y: auto;
  @media (min-width: 991px) {
    display: flex;
    flex: 1;
    top: 0;
    flex-wrap: nowrap;
    overflow-y: visible;
    position: relative;
  }
  &--hidden {
    display: none;
    @media (min-width: 991px) {
      display: flex;
    }
  }
  &__Spacer {
    width: 100%;
    display: flex;
    height: 0;
    @media (min-width: 991px) {
      flex: 1;
      order: 2;
      transition: flex 300ms linear;
    }
    &.search {
      @media (min-width: 991px) {
        flex: 0;
      }
    }
  }
  &__Search {
    width: 100%;
    height: 60px;
    display: flex;
    border-bottom: 1px solid #dbdfe1;
    @media (min-width: 991px) {
      flex: 0;
      order: 3;
      height: 79px;
      min-width: 240px;
      border-bottom: none;
      transition: flex 300ms linear;
    }
    &.search {
      @media (min-width: 991px) {
        flex: 1;
      }
    }
  }
  &__Menu {
    width: 100%;
    display: flex;
    border-bottom: 1px solid #dbdfe1;
    @media (min-width: 991px) {
      flex: 0;
      order: 1;
      height: 79px;
      border-bottom: none;
    }
  }
  &__Links {
    width: 100%;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 15px;
    @media (min-width: 991px) {
      flex: 0;
      order: 4;
      height: 79px;
      color: #fff;
      fill: #fff;
    }
    &__Item {
      font-size: 32px;
      color: rgba(0,0,0,0.87);
      @media (min-width: 991px) {
        color: #fff;
      }
    }
  }
}
</style>

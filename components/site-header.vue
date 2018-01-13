<style lang="scss" scoped>
$mobile-break: 48em;

header {
  height: 60px;
  background-color: #3949AB;
  padding: 0 15px;
  display: flex;
  align-items: center;

  @media (min-width: $mobile-break) {
    height: 80px;
    padding: 0 30px;
  }
}
</style>

<template>
  <header>
    <page-content>
      <site-toolbar />
    </page-content>
  </header>

  <!--
  <header class="Header">
    <nuxt-link class="Header__Logo" to="/">
      <img class="Header__Logo__Img" src="~static/logo_nav.svg" alt="Guild AI" />
      <h1 class="Header__Logo__Text">Guild AI</h1>
    </nuxt-link>
    <div class="Header__Toggler">
      <div class="Header__Toggler__Button" @click="toggle">
        <div :class="{'icon menu': !visible, 'icon close': visible}"></div>
      </div>
    </div>
    <nuxt-header-nav />
  </header>
  -->
</template>

<script>
import PageContent from './page-content.vue';
import SiteToolbar from './site-toolbar.vue';

export default {
  components: {
    PageContent,
    SiteToolbar
  }
};
</script>


<!--
<script>
import NuxtHeaderNav from '~/components/HeaderNav.vue'

export default {
  computed: {
    visible() { return this.$store.state.visibleHeader }
  },
  methods: {
    toggle() { this.$store.commit('toggle', 'visibleHeader') }
  },
  components: {
    NuxtHeaderNav
  }
}
</script>

<style lang="scss" scoped>
.Header {
  top: 0;
  width: 100%;
  height: 60px;
  z-index: 995;
  padding: 0 15px;
  display: flex;
  flex-direction: row;
  background-color: #3949AB;
  @media (min-width: 991px) {
    height: 80px;
    padding: 0 30px;
  }
  &__Logo {
    display: flex;
    align-items: center;
    margin-left: -15px;
    padding: 0 15px;
    &__Img {
      height: 32px;
      @media (min-width: 991px) {
        height: 40px;
      }
    }
    &__Text {
      margin: 0;
      width: 0;
      overflow: hidden;
    }
  }
  &__Toggler {
    display: flex;
    flex: 1;
    align-items: center;
    justify-content: flex-end;
    @media (min-width: 991px) {
      display: none;
    }
    &__Button {
      display: flex;
      width: 25px;
      height: 20px;
      cursor: pointer;
    }
    &__Button .icon {
      color: #fff;
    }
  }
}
</style>
-->

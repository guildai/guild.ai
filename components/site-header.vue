<template>
  <header>
    <page-content>
      <site-toolbar />
    </page-content>
  </header>
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

<style lang="scss" scoped>
$mobile-break: 48em;

header {
  position: fixed;
  width: calc(100% - 30px);
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

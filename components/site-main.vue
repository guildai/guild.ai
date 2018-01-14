<style lang="scss" scoped>
</style>

<template>
  <div class="main">
    <page-content>
      <nuxt />
    </page-content>
  </div>
</template>

<script>
import PageContent from './page-content.vue';

export default {
  components: {
    PageContent
  }
};
</script>

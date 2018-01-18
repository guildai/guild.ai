<template>
  <page-content>
    <div class="page-wrapper">
      <nuxt />
    </div>
  </page-content>
</template>

<script>
import PageContent from './page-content.vue';

export default {
  components: {
    PageContent
  }
};
</script>

<style lang="scss" scoped>
.page-wrapper {
  padding: 15px;
}
</style>

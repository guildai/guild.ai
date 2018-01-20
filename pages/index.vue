<template>
  <div>
    <div class="row">
      <div class="tagline col-sm-6">
        Essential tools for TensorFlow model development and reuse
      </div>
      <div class="col-sm-6">
        {some graphic here}
      </div>
    </div>
    <div class="row">
      <div class="col-sm-4">
        Feature 1
      </div>
      <div class="col-sm-4">
        Feature 2
      </div>
      <div class="col-sm-4">
        Feature 3
      </div>
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: this.$store.state.lang.homepage.meta.title
    };
  }
};
</script>

<style lang="scss" scoped>
.tagline {
  font-size: 42px;
  font-weight: 400;
  line-height: 1.5;
  padding: 30px 30px 0 0;
}
</style>

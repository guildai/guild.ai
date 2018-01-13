<template>
  <div class="page-content">
    <div class="content-wrapper">
      <div class="content-slot">
        <slot />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.page-content {
  width: 100%;

  .content-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
  }

  .content-slot {
    flex: 1;
    max-width: 1400px;
  }
}
</style>

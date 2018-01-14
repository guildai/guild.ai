<template>
  <div class="links">
    <ul>
      <li>
        <a v-for="link in socialLinks" target="_blank" :href="link.link">
          <i :class="'mdi mdi-' + link.icon" />
        </a>
      </li>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
</style>

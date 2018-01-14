<template>
  <div class="menu">
    <ul>
      <li>
        <nuxt-link to="/install">
          {{ $store.state.lang.links.install }}
        </nuxt-link>
      </li>
      <li>
        <nuxt-link to="/docs">
          {{ $store.state.lang.links.docs }}
        </nuxt-link>
      </li>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
.menu {
  ul {
    width: 100%;
    margin: 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    list-style: none;
    justify-content: space-between;

    li {
      width: 100%;
      border-bottom: 1px solid #ddd;

      a {
        width: 100%;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: rgba(#000, 0.87);
      }
    }
  }
}
</style>

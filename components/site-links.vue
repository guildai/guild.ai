<template>
  <div class="links">
    <ul>
      <li>
        <a v-for="link in $store.state.lang.externalLinks" target="_blank" :href="link.link">
          <i :class="'mdi mdi-' + link.icon" />
        </a>
      </li>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
$mobile-break: 48em;

.links {
  ul {
    width: 100%;
    height: 60px;
    margin: 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    list-style: none;
    align-items: center;
    justify-content: center;

    li {

      a {
        text-decoration: none;
        color: rgba(#000, 0.87);
        font-size: 24px;

        @media (min-width: $mobile-break) {
          color: #fff;
          font-size: 28px;
        }
      }
    }
  }
}
</style>

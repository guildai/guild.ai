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
      <li>
        <nuxt-link to="/packages">
          {{ $store.state.lang.links.packages }}
        </nuxt-link>
      </li>
      <li>
        <nuxt-link to="/support">
          {{ $store.state.lang.links.support }}
        </nuxt-link>
      </li>
      <li>
        <nuxt-link to="/about">
          {{ $store.state.lang.links.about }}
        </nuxt-link>
      </li>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
$mobile-break: 48em;

.menu {
  ul {
    width: 100%;
    margin: 0;
    padding: 0;
    list-style: none;

    @media (min-width: $mobile-break) {
      display: flex;
    }

    li {
      border-bottom: 1px solid #ddd;

      @media (min-width: $mobile-break) {
        border-bottom: none;
        margin: 0 15px;

        &:first-child {
          _margin-left: 0px;
        }
      }

      a {
        width: 100%;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: rgba(#000, 0.87);

        @media (min-width: $mobile-break) {
          font-size: 20px;
          color: #fff;
        }
      }
    }
  }
}
</style>

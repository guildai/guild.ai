<template>
  <ul class="Menu">
    <li class="Menu__Item">
      <nuxt-link class="Menu__Item__Link" to="/install">
        {{ $store.state.lang.links.install }}
      </nuxt-link>
    </li>
    <li class="Menu__Item">
      <nuxt-link class="Menu__Item__Link" to="/guide">
        {{ $store.state.lang.links.guide }}
      </nuxt-link>
    </li>
    <li class="Menu__Item">
      <nuxt-link class="Menu__Item__Link" to="/api">
        {{ $store.state.lang.links.api }}
      </nuxt-link>
    </li>
    <li class="Menu__Item">
      <nuxt-link class="Menu__Item__Link" to="/examples">
        {{ $store.state.lang.links.examples }}
      </nuxt-link>
    </li>
    <li class="Menu__Item">
      <nuxt-link class="Menu__Item__Link" to="/faq">
        {{ $store.state.lang.links.faq }}
      </nuxt-link>
    </li>
  </ul>
</nav>
</template>

<script>
import NuxtHeaderNavMenuDropdown from '~/components/HeaderNavMenuDropdown.vue'

export default {
  components: {
    NuxtHeaderNavMenuDropdown
  }
}
</script>

<style lang="scss" scoped>
.Menu
{
  width: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  justify-content: space-between;
  @media (min-width: 991px)
  {
    flex: 1;
    flex-wrap: nowrap;
    padding: 0 15px;
  }
  &__Item
  {
    width: 100%;
    display: flex;
    border-bottom: 1px solid #dbdfe1;
    @media (min-width: 991px)
    {
      border-bottom: none;
    }
    &:last-child
    {
      border-bottom: none;
    }
    &__Link
    {
      height: 60px;
      display: flex;
      width: 100%;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      text-decoration: none;
      letter-spacing: 0.5px;
      color: rgba(0,0,0,0.87);
      padding: 0 15px;
      &:hover
      {
        opacity: 0.67;
      }
      @media (min-width: 991px)
      {
        height: 79px;
        color: #fff;
      }
    }
    .nuxt-link-active, .nuxt-link-active:hover
    {
      color: #41b883;
    }
  }
}
</style>

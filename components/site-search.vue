<template>
  <div class="search">
    <input
      type="text"
      ref="search"
      id="guildai-search"
      :placeholder="$store.state.lang.text.search"
      @focus="$emit('focus')"
      @blur="$emit('blur')"
      @keyup.esc="clear" />
  </div>
</template>

<script>
export default {
  methods: {
    clear() {
      this.$refs.search.value = '';
      this.$refs.search.blur();
    }
  }
};
</script>

<style lang="scss" scoped>
$mobile-break: 48em;
$transition-time: 250ms;

.search {
  display: flex;
  align-items: center;

  input {
    height: 60px;
    padding: 0 15px;
    border: none;
    border-bottom: 1px solid #ddd;
    display: block;
    width: calc(100% - 30px);

    &::placeholder {
      color: rgba(#000, 0.4);
    }

    @media (min-width: $mobile-break) {
      height: 42px;
      color: #fff;
      background-color: rgba(#000, 0.26);
      border: none;
      border-radius: 2px;
      transition:
        background-color $transition-time,
        color $transition-time;

      &::placeholder {
        color: rgba(#fff, 0.6);
        transition:
          background-color $transition-time,
          color $transition-time;
      }

      &:focus {
        background-color: #fff;
        color: rgba(#000, 0.87);

        &::placeholder {
          color: rgba(#000, 0.4);
        }
      }
    }
  }
}
</style>

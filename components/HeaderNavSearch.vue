<template>
  <div class="Search">
    <input class="Search__Input" type="text" name="search" id="algolia" required :placeholder="$store.state.lang.text.search" />
  </div>
</template>

<script>
let scriptInjected = false
let callbacks = []
let onScriptLoaded = (cb) => callbacks.push(cb)
let scriptLoaded = () => callbacks.forEach((cb) => cb())

export default {
  mounted() {
    onScriptLoaded(() => this.addInstantSearch())
    if (scriptInjected) return
    // Load JS
    const script = document.createElement('script')
    script.setAttribute('type', 'text/javascript')
    script.setAttribute('src', '//cdn.jsdelivr.net/docsearch.js/2/docsearch.min.js')
    document.getElementsByTagName('body')[0].appendChild(script)
    script.onload = scriptLoaded
    // Load CSS
    var link = document.createElement('link')
    link.setAttribute('rel', 'stylesheet')
    link.setAttribute('type', 'text/css')
    link.setAttribute('href', 'https://cdn.jsdelivr.net/docsearch.js/2/docsearch.min.css')
    document.getElementsByTagName('body')[0].appendChild(link)
    scriptInjected = true
  },
  methods: {
    addInstantSearch() {
      window.docsearch({
        apiKey: process.env.docSearchApiKey,
        indexName: 'nuxtjs',
        inputSelector: '#algolia',
        algoliaOptions: { 'facetFilters': [`tags:${this.$store.state.locale}`] },
        debug: true // Set debug to true if you want to inspect the dropdown
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.Search {
  width: 100%;
  height: 100%;
  position: relative;
  &__Input {
    width: 100%;
    display: block;
    border: none;
    font-weight: 400;
    height: 60px;
    font-size: 16px;
    padding: 0 15px;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #dbdfe1;
    &:focus,
    &:visited,
    &:active {
      border-bottom: 1px solid #dbdfe1;
    }
    @media (min-width: 991px) {
      height: 42px;
      margin-top: 19px;
      background-color: rgba(0,0,0,0.26);
      color: #fff;
      padding: 0 15px;
      border-radius: 2px;
      border-bottom: none;
      transition:
        background-color .25s cubic-bezier(.1,.7,.1,1),
        color .25s cubic-bezier(.1,.7,.1,1);
      &:hover {
        background-color: rgba(255,255,255,0.1);
      }
      &:focus,
      &:visited,
      &:active {
        background-color: #fff;
        color: rgba(0,0,0,0.87);
      }
      &::placeholder {
        color: rgba(255,255,255,0.75);
      }
      ::-ms-input-placeholder {
        color: rgba(255,255,255,0.75);
      }
      &:focus::placeholder {
        color: rgba(0,0,0,0.87);
      }
      &:focus::-ms-input-placeholder {
        color: rgba(0,0,0,0.87);
      }
    }
  }
}
</style>

<style>
.Search .algolia-autocomplete .ds-dropdown-menu {
  min-width: inherit;
  max-width: inherit;
  margin: 6px 10px;
  width: calc(100% - 20px);
  @media (min-width: 991px) {
    margin: 6px 0;
    width: 100%;
  }
}

.Search .algolia-autocomplete.algolia-autocomplete-right .ds-dropdown-menu:before {
  left: 24px;
}

.Search .algolia-autocomplete.algolia-autocomplete-left .ds-dropdown-menu:before {
  left: 24px;
}

.Search .algolia-autocomplete {
  @media (min-width: 991px) {
    height: 42px;
  }
}
</style>

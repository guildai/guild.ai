<template>
  <div class="root">
    <h1>{{ attrs.title }}</h1>
    <html-parser :content="body" />
  </div>
</template>

<script>
import axios from 'axios';
import HtmlParser from '~/components/HtmlParser.vue';

export default {
  async asyncData({ route, store, error }) {
    let data = {
      attrs: {},
      body: '',
      docLink: ''
    };
    const slug = route.params.slug;
    const path = `/${store.state.lang.iso}/${slug}`;
    let res;
    try {
      res = await axios.get(store.state.apiURI + path);
    } catch (err) {
      if (err.response.status !== 404) {
        return error({
          statusCode: 500,
          message: store.state.lang.text.an_error_occured
        });
      }
      return error({
        statusCode: 404,
        message: store.state.lang.text.api_page_not_found
      });
    }
    data.attrs = res.data.attrs;
    data.body = res.data.body;
    data.docLink = `https://github.com/nuxt/docs/blob/master${path}.md`;
    if (!data.attrs.title) {
      // eslint-disable-line no-console
      console.error(`[${path}] ${store.state.lang.text.please_define_title}.`);
    }
    if (!data.attrs.description) {
      // eslint-disable-line no-console
      console.error(`[${path}] ${store.state.lang.text.please_define_description}.`);
    }
    return data;
  },
  scrollToTop: true,
  head() {
    return {
      title: this.attrs.title,
      titleTemplate: '%s - Guild AI',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.attrs.description
        }
      ]
    };
  },
  components: {
    HtmlParser
  }
};
</script>

<style lang="scss" scoped>
.root {
  h1 {
    margin: 0;
    font-size: 42px;
    font-weight: 300;
  }
}
</style>

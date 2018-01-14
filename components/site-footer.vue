<template>
  <footer>
    <div class="top">
      <page-content>
      </page-content>
    </div>
    <div class="bottom">
      <page-content>
        <div class="row">
          <div class="copyright col-xs-10">
            Copyright &copy; 2017-2018 TensorHub, Inc.
          </div>
          <div class="social-links col-xs-2 end-xs">
            <a
              v-for="link in $store.state.lang.externalLinks"
              target="_blank"
              :href="link.link">
              <i :class="'mdi mdi-' + link.icon" />
            </a>
          </div>
        </div>
      </page-content>
    </div>
  </footer>
</template>

<script>
import PageContent from './page-content.vue';

export default {
  components: {
    PageContent
  }
};
</script>

<style lang="scss" scoped>
$mobile-break: 48em;

footer {

  .top {
    height: 90px;
    background-color: #424242;
  }

  .bottom {
    padding: 7px 15px;
    background-color: #212121;
    color: rgba(#fff, 0.67);
    font-size: 14px;

    @media (min-width: $mobile-break) {
      padding: 10px 30px;
    }

    .copyright {
    }

    .social-links a {
      color: rgba(#fff, 0.87);
      font-size: 24px;
      line-height: 24px;
    }
  }
}
</style>

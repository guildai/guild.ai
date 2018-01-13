<template>
  <footer>
    <div class="top row">
    </div>
    <div class="bottom row">
      <div class="copyright col-xs-12 col-sm-6">
        Copyright &copy; 2017-2018 TensorHub, Inc.
      </div>
      <div class="social-links col-xs-12 col-sm-6 end-sm">
        <a v-for="link in socialLinks" target="_blank" :href="link.link">
          <i :class="'mdi mdi-' + link.icon" />
        </a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      socialLinks: [
        {
          icon: 'github-circle',
          link: 'https://github.com/guildai/guild'
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
footer {

  .top {
    height: 90px;
    background-color: #424242;
  }

  .bottom {
    padding: 7px 15px;
    background-color: #212121;
    display: flex;
    align-items: center;
    color: rgba(#fff, 0.67);
    font-size: 14px;

    @media (min-width: 992px) {
      padding: 10px 30px;
    }

    .copyright {
      _flex: 1;
    }

    .social-links a {
      color: rgba(#fff, 0.87);
      font-size: 24px;
    }
  }
}
</style>

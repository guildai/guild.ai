<template>
  <div>
    <h1>Guild AI home page!</h1>

    <p>Lorem ipsum dolor sit amet, consectetur adipiscing
    elit. Praesent sagittis elit et magna sollicitudin, in venenatis
    nunc posuere. Maecenas non dui magna. Quisque convallis enim
    feugiat ornare tincidunt. Mauris tempor nec mi in dictum. Etiam
    fermentum molestie metus, quis volutpat nisi vestibulum
    vel. Mauris et urna neque. Curabitur eget lectus metus. Nullam
    porta congue mauris id dapibus. Proin consequat velit vel ante
    tincidunt auctor. Vivamus aliquet tempus lobortis.</p>

    <p>Cras consectetur dignissim porttitor. In risus nibh, sagittis
    eget mauris a, dictum scelerisque lorem. Mauris euismod varius
    accumsan. Vestibulum velit mauris, ultrices id consectetur id,
    pellentesque ac mi. Class aptent taciti sociosqu ad litora
    torquent per conubia nostra, per inceptos himenaeos. Nullam
    tincidunt sem interdum mauris aliquet semper. Nam pharetra odio
    risus, dictum fringilla purus sodales eget.</p>

    <p>Praesent vitae lacus quis magna ornare elementum. Pellentesque
    venenatis turpis non nibh tincidunt blandit. Curabitur eget magna
    gravida, rhoncus ante nec, egestas ipsum. Suspendisse quis urna
    vitae diam vestibulum laoreet. Ut posuere nulla nec egestas
    pretium. In enim justo, fermentum ut suscipit laoreet, ullamcorper
    quis quam. Cras ornare felis ut velit imperdiet pulvinar. Nullam
    orci ex, pulvinar nec sem eu, dignissim fermentum mauris. Donec
    orci orci, bibendum sit amet commodo in, finibus non felis. Aenean
    pulvinar, ipsum scelerisque eleifend aliquam, orci magna rutrum
    urna, sed bibendum nulla turpis sed velit. Curabitur sed nunc nec
    turpis interdum placerat. Aenean et tincidunt odio. Quisque
    blandit ipsum ut libero sodales imperdiet.</p>

    <p>Nulla nec purus sed eros suscipit iaculis vitae quis elit. Nam
    nec pellentesque enim. In dapibus facilisis felis, nec vulputate
    diam placerat vel. Quisque accumsan dolor nec mauris blandit
    hendrerit. In sagittis, velit et dictum pharetra, metus massa
    porta urna, sit amet molestie lorem orci ac nunc. Quisque in
    dignissim diam. Quisque consequat ultrices ligula, quis
    consectetur eros finibus nec. Fusce imperdiet convallis nisl ut
    porttitor. Nullam non sem metus. Etiam eu lobortis massa, a
    euismod tellus.</p>

    <p>Aenean ac metus velit. Sed tincidunt, justo sit amet
    ullamcorper varius, dolor ipsum maximus erat, ac lobortis massa
    quam a ante. Donec scelerisque posuere leo, non facilisis tellus
    tincidunt sit amet. Nullam in sodales libero. Aenean ex lectus,
    tincidunt eget risus sit amet, pretium sollicitudin
    lorem. Curabitur nec ultrices ligula, eget fermentum mi. Quisque
    ante odio, tristique in magna in, consectetur auctor
    sapien. Integer sit amet urna neque. Pellentesque habitant morbi
    tristique senectus et netus et malesuada fames ac turpis
    egestas. Vivamus neque nulla, pretium at iaculis ac, rutrum sed
    nunc. Proin fringilla lacus eget erat auctor sodales.</p>

  </div>
</template>

<script>
import NuxtLogo from '~/components/VueToNuxtLogo.vue';

export default {
  components: {
    NuxtLogo
  },
  head() {
    return {
      title: this.$store.state.lang.homepage.meta.title,
      meta: [
        { name: 'description', hid: 'description', content: this.$store.state.lang.homepage.meta.description },
        // Open Graph
        { name: 'og:title', content: this.$store.state.lang.homepage.meta.title },
        { name: 'og:description', content: this.$store.state.lang.homepage.meta.description },
        { name: 'og:type', content: 'website' },
        { name: 'og:url', content: 'https://nuxtjs.org' },
        { name: 'og:image', content: 'https://i.imgur.com/PzEm5j2.png' },
        // Twitter Card
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@guild_ai' },
        { name: 'twitter:title', content: this.$store.state.lang.homepage.meta.title },
        { name: 'twitter:description', content: this.$store.state.lang.homepage.meta.description },
        { name: 'twitter:image', content: 'https://i.imgur.com/PzEm5j2.png' },
        { name: 'twitter:image:alt', content: 'Nuxt.js Logo' }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
</style>

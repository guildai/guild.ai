import axios from 'axios';
import Vuex from 'vuex';

const store = () => new Vuex.Store({
  state: {
    docVersion: '',
    ghVersion: '',
    mobileMenuOpen: false,
    visibleAffix: false,
    apiURI: 'https://docs.api.guild.ai',
    locale: 'en',
    lang: {},
    menu: {}
  },

  mutations: {
    toggle(state, key) {
      state[key] = !state[key];
    },

    setFalse(state, key) {
      state[key] = false;
    },

    setApiURI(state, apiURI) {
      state.apiURI = apiURI;
    },

    setDocVersion(state, docVersion) {
      state.docVersion = docVersion;
    },

    setGhVersion(state, ghVersion) {
      state.ghVersion = ghVersion;
    },

    setLocale(state, locale) {
      state.locale = locale;
    },

    setLang(state, lang) {
      state.lang = lang;
    },

    setMenu(state, menu) {
      state.menu = menu;
    }
  },

  actions: {
    async nuxtServerInit({ state, commit }, { isDev, req, redirect }) {
      if (isDev) {
        commit('setApiURI', 'http://localhost:4000');
      }
      const hostParts = (req.headers.host || '').replace('.org', '').split('.');
      if (hostParts.length === 2) {
        if (hostParts[0] === 'www') {
          return redirect(301, 'https://nuxtjs.org' + req.url);
        }
        commit('setLocale', hostParts[0]);
      }

      const resReleases = await axios(state.apiURI + '/releases');
      commit('setGhVersion', resReleases.data[0].name);

      const resLang = await axios(state.apiURI + '/lang/' + state.locale);
      commit('setLang', resLang.data);
      commit('setDocVersion', resLang.data.docVersion);

      const resMenu = await axios(state.apiURI + '/menu/' + state.locale);
      commit('setMenu', resMenu.data);
    }
  }
});

export default store;

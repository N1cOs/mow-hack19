import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    score: 0,
    persons: []
  },
  mutations: {
    addPoint: (state) => {
      state.score++;
    },
    addPerson: (state, payload) => {
      state.persons.push(payload);
    }
  },
  actions: {
  },
  modules: {
  },
});

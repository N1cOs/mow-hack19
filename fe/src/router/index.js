import Vue from 'vue';
import VueRouter from 'vue-router';
import StartScreen from '../views/StartScreen';
import GameScreen from '../views/GameScreen';
import FinalScreen from '../views/FinalScreen';
import HistorySreen from '../views/HistoryScreen';
import store from '../store/index';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'start',
    component: StartScreen,
  },
  {
    path: '/game',
    name: 'game',
    component: GameScreen,
  },
  {
    path: '/final',
    name: 'final',
    component: FinalScreen,
  },
  {
    path: '/history',
    name: 'history',
    component: HistorySreen
  }
];

const router = new VueRouter({
  // mode:'history',
  routes
});

const clearStore = () => {
  store.state.score = 0;
  store.state.persons = [];
};

router.beforeEach((to, from, next) => {
  if (router.resolve(to.path).route.name === 'game') {
    store.commit('setToInitial');
    next()
  }

  next();
});

export default router;

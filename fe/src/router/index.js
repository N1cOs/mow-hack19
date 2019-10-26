import Vue from 'vue';
import VueRouter from 'vue-router';
import StartScreen from '../views/start/StartScreen';
import GameScreen from '../views/game/GameScreen';
import FinalScreen from '../views/final/FinalScreen';

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
  }
];

const router = new VueRouter({
  routes,
});

export default router;

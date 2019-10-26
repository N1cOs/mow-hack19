import Vue from 'vue';
import VueRouter from 'vue-router';
import StartScreen from '../views/StartScreen';
import GameScreen from '../views/GameScreen';
import FinalScreen from '../views/FinalScreen';

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
];

const router = new VueRouter({
  routes,
});

export default router;

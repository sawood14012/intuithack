// eslint-disable-next-line
import Vue from 'vue';
import './plugins/vuetify';
import Vuesax from 'vuesax';
import 'vuesax/dist/vuesax.css';
import 'material-icons/iconfont/material-icons.css';
import VueFire from 'vuefire';
import App from './App.vue';
import router from './router';
import store from './store';
import './registerServiceWorker';


Vue.use(Vuesax);
Vue.use(VueFire);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');

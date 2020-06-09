import Vue from 'vue'
import App from './App.vue'

import Amplify, { Auth } from 'aws-amplify';
import awsconfig from './aws-exports';
//build in UI
import '@aws-amplify/ui-vue';
Amplify.configure(awsconfig);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

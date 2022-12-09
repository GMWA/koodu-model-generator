import { createApp } from "vue";
import { createPinia } from "pinia";

import axios from "axios";
import SuperTokens from "supertokens-web-js";
import Session from "supertokens-web-js/recipe/session";

Session.addAxiosInterceptors(axios);

import "./style.css";
import App from "./App.vue";
import router from "./router";

SuperTokens.init({
  appInfo: {
    appName: "modelgenerator",
    apiDomain: "http://localhost:8000"
  },
  recipeList: [Session.init()]
});

const store = createPinia();
const app = createApp(App);
app.use(store);
app.use(router);
app.mount("#app");

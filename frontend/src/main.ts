import { createApp } from "vue";

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

createApp(App).use(router).mount("#app")

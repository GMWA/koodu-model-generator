import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../pages/Dashboard.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => Dashboard
    },
    {
      path: "/auth",
      component: () => import(/* webpackChunkName: "Auth" */ "../pages/users/Auth.vue")
    },
    {
      path: "/auth/callback/:provider",
      name: "authcallback",
      component: () => import(/* webpackChunkName: "Callback" */  "../pages/users/AuthCallback.vue")
    }, 
    {
      path: "/auth/reset-password",
      name: "resetpassword",
      component: () => import(/* webpackChunkName: "Password" */  "../pages/users/ForgotPassword.vue")
    }
  ]
})

export default router;
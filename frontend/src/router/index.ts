import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../pages/Dashboard.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/dasboard",
      name: "dashboard",
      component: () => Dashboard
    },
    {
      path: "/auth",
      name: "authentication",
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
    },
    {
      path: "/",
      name: "projects",
      component: () => import(/* webpackChunkName: "Projects" */  "../pages/Projects.vue")
    },
    {
      path: "/project-details/:id",
      name: "projectdetails",
      component: () => import(/* webpackChunkName: "ProjectDetails" */  "../pages/ProjectDetails.vue")
    },
    {
      path: "/editor",
      name: "editor",
      component: () => import(/* webpackChunkName: "Editor" */  "../pages/Editor.vue")
    },
    {
      path: "/supports",
      name: "supports",
      component: () => import(/* webpackChunkName: "Supports" */  "../pages/Supports.vue")
    },
    {
      path: "/settings",
      name: "settings",
      component: () => import(/* webpackChunkName: "Settingd" */  "../pages/Settings.vue")
    }
  ]
})

export default router;

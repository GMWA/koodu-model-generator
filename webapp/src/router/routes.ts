import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/projects/ProjectListPage.vue') }],
    meta: { requiresAuth: true },
  },
  {
    path: '/auth/login',
    component: () => import('layouts/AuthLayout.vue'),
    children: [{ path: '', name: 'LoginPage', component: () => import('pages/auth/LoginPage.vue') }],
  },
  {
    path: '/auth/registration',
    component: () => import('layouts/AuthLayout.vue'),
    children: [{ path: '', component: () => import('pages/auth/RegistrationPage.vue') }],
  },
  {
    path: '/auth/forgot-password',
    component: () => import('layouts/AuthLayout.vue'),
    children: [{ path: '', component: () => import('pages/auth/ForgotPasswordPage.vue') }],
  },
  {
    path: '/auth/reset-password/:token',
    component: () => import('layouts/AuthLayout.vue'),
    children: [{ path: '', component: () => import('pages/auth/ResetPasswordPage.vue') }],
  },
  {
    path: '/auth/activate-link/:token',
    component: () => import('layouts/AuthLayout.vue'),
    children: [{ path: '', component: () => import('pages/auth/ActivationPage.vue') }],
  },
  {
    path: '/projects',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/projects/ProjectListPage.vue') }],
    meta: { requiresAuth: true },
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;

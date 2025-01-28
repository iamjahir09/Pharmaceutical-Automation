import { createRouter, createWebHistory } from "vue-router";

import LoginPage from "@/views/LoginPage.vue";
import SignupPage from "@/views/SignupPage.vue";
import MainPage from "@/views/MainPage.vue";

const routes = [
  { 
    path: "/", 
    name: "Landing", 
    component: () => window.location.replace("/landing.html"), // Redirect to raw HTML
  },
  { 
    path: "/main-app", 
    name: "MainPage", 
    component: MainPage,
  },
  { path: "/login", name: "Login", component: LoginPage },
  { path: "/signup", name: "Signup", component: SignupPage },
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

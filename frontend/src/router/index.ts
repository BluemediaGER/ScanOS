import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/power',
      name: 'power',
      component: () => import('@/views/PowerView.vue')
    },
    {
      path: '/scan',
      name: 'scan',
      component: () => import('@/views/ScanView.vue')
    }
  ]
})

export default router

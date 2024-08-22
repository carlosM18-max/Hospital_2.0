import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/components/Login.vue'
import RegisterView from '@/components/Register.vue'
import DashboardView from '@/components/Dashboard.vue'
import UserView from '@/components/User.vue'
// 
import RequestView from '@/components/RequestTransplant.vue'
import TableRView from '@/components/TableRequest.vue'
import UpdateRView from '@/components/UpdateRequest.vue'
// 
import OrgansView from '@/components/Organs.vue'
import FooterView from '@/components/Footer.vue'

import OrganDetails from '@/components/Organ_Details.vue'
import OrganForm from '@/components/OrganForm.vue'




import ForgotPasswordView from '@/components/forgot-password.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: UserView
    },
    {
      path: '/forgot-password',
      name: 'forgot-password',
      component: ForgotPasswordView
    },

    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      children:[
        {
          path: '/requestTansplant',
          name: 'requestTransplant',
          component: RequestView
        },
        {
          path: '/TableTransplante',
          name: 'TableTransplante',
          component: TableRView
        },
        {
          path: '/UpdateTransplante',
          name: 'UpdateTransplante',
          component: UpdateRView
        },
        {
          path: '/organos',
          name: 'organos',
          component: OrgansView
        },
        {
          path: '/footer',
          name: 'footer',
          component: FooterView
        },
        {
          path: '/organdetails',
          name: 'organdetails',
          component: OrganDetails
        },
        {
          path: '/organform',
          name: 'organform',
          component: OrganForm
        }
      ]
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router



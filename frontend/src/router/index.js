import Vue from 'vue'
import Router from 'vue-router'

import CalendarModal from '@/components/CalendarModal'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'CalendarModal',
      component: CalendarModal
    }
  ],
  mode: 'history'
})

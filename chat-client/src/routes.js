import Homepage from './pages/Homepage.vue'
import store from './store'

import { createRouter, createWebHistory } from 'vue-router'

const routes = [
	{
		// App.vue
		path: '/',
		components: {
			default: () => import('./pages/Homepage.vue'),
		},
		name: 'Homepage',
		children: [
			{
				path: 'settings',
				components: {
					userinfo: () => import('./components/Userinfo.vue'),
					default: () => import('./pages/Settings.vue'),
				},
			},
			{
				path: 'chat',
				name: 'Chat',
				components: {
					userchat: () => import('./components/MsgList.vue'),
					default: () => import('./pages/PrivateChat.vue'),
				},
				// props: (route) => ({
				// 	id: route.params.otherUser.id,
				// }),
			},
		],
		beforeEnter: (to, from, next) => {
			// ...
			store
				.dispatch('tryAutoLogin', localStorage.getItem('token'))
				.then((loginType) => {
					// console.log(loginType)
					if (loginType) {
						next()
						return
					}
				})
			// 浏览器缓存清空后，返回登录页面
			if (!localStorage.getItem('token')) {
				next('/login')
				return
			}
		},
	},
	{
		path: '/login',
		name: 'Login',
		component: () => import('./pages/Login.vue'),
	},
	{
		path: '/register',
		name: 'Register',
		component: () => import('./pages/Register.vue'),
	},
	{
		path: '/reset-pwd',
		name: 'ResetPwd',
		component: () => import('./pages/ResetPwd.vue'),
	},
	// {
	// 	component: '/register',
	// 	name: Register,
	// },
]

const router = createRouter({
	history: createWebHistory(),
	routes,
})

export default router

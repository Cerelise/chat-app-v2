import Homepage from './pages/Homepage.vue'
import store from './stores/store'

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
			{
				path: 'note',
				components: {
					noteList: () => import('./pages/note/NoteList.vue'),
					default: () => import('./pages/note/NoteDefault.vue'),
					// noteEdit:() => import('./pages/NoteEditView.vue'),
					// default: () => import('./pages/NoteDefault.vue'),
				},
			},
			// 添加笔记
			{
				path: 'note-post',
				components: {
					noteList: () => import('./pages/note/NoteList.vue'),
					default: () => import('./pages/note/NotePostView.vue'),
				},
			},
			// 查看笔记
			{
				path: 'note-view/:id',
				name: 'noteView',
				components: {
					noteList: () => import('./pages/note/NoteList.vue'),
					default: () => import('./pages/note/NotePreview.vue'),
				},
			},
			// 编辑文章
			{
				path: 'note-edit/:id',
				name: 'noteEdit',
				components: {
					noteList: () => import('./pages/note/NoteList.vue'),
					default: () => import('./pages/note/NoteEditView.vue'),
				},
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
	// 	path: '/profile-editing',
	// 	name: 'ProfileEditing',
	// 	component: () => import('./pages/ProfileEditing.vue'),
	// },
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

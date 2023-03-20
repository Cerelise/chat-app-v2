import { createLogger, createStore } from 'vuex'
import axios from 'axios'
import Qs from 'qs'

const HostURL = 'http://127.0.0.1:9000'

export default createStore({
	state: {
		userinfo: {
			avatar: null,
			nickName: null,
			area: null,
			description: null,
			github: null,
			socialSite: null,
			phone: null,
			email: null,
			website: null,
			id: null,
		},
		token: null,
	},
	mutations: {
		saveUserinfo(state, userinfo) {
      state.userinfo = userinfo
      // state.userinfo.avatar = userinfo +'/upload/' +state.userinfo.avatar
      console.log(state.userinfo);
			// console.log(state.userinfo)
		},
		setToken(state, token) {
			state.token = token
			// console.log(state.token)
		},
		// 清空用户登录状态
		clearToken(state) {
			state.token = ''
		},
	},
	actions: {
		// 自动登录
		async tryAutoLogin({ commit }, token) {
			console.log('----action----vuex----自动登录')
			console.log(token)

			let loginType = false

			await axios({
				method: 'post',
				url: HostURL + '/api-chat/userinfo/',
				data: Qs.stringify({
					token: token,
				}),
			}).then((res) => {
				let userinfo = res.data
				console.log(res.data)
				if (userinfo.nickName.length > 0) {
					if (userinfo.nickName != '未登录') {
						userinfo.avatar = HostURL + userinfo.avatar
					}
					loginType = true
				}
				commit('saveUserinfo', userinfo)
			})
			return loginType
		},
		// 退出登录
		async userLogout({ commit }) {
			let token = localStorage.getItem('token')
			await axios({
				url: HostURL + '/api-chat/dchat-logout/',
				method: 'post',
				data: Qs.stringify({
					token,
				}),
			}).then((res) => {
				console.log(res.data)
				// 清除vuex里的token
				commit('clearToken')
				localStorage.removeItem('token')
			})
		},
		// 获取用户信息
		getUserinfo({ commit }, token) {
			console.log('---getUserinfo---')
			console.log(token)
			axios({
				method: 'post',
				url: HostURL + '/api-chat/userinfo/get/',
				data: Qs.stringify({
					token: token,
				}),
			}).then((res) => {
				const result = res.data
				commit('saveUserinfo', result)
				console.log(result)
			})
		},
	},
	modules: {},
})

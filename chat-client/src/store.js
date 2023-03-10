import { createStore } from 'vuex'
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
		},
		token: null,
	},
	mutations: {
		saveUserinfo(state, userinfo) {
			state.userinfo = userinfo
			// console.log(state.userinfo)
		},
		setToken(state, token) {
			state.token = token
			// console.log(state.token)
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
				url: 'http://127.0.0.1:9000/api-chat/userinfo/',
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
	},
	modules: {},
})

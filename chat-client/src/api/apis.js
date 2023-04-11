import axios from 'axios'
// import { useRoute } from 'vue-router'

const base = 'http://127.0.0.1:9000'
// const route = useRoute()

// 用户操作
export const userLogin = (params) => {
	return axios
		.post(`${base}/api-chat/dchat-login/`, params)
		.then((res) => res.data)
}
export const userRegister = (params) => {
	return axios
		.post(`${base}/api-chat/dchat-register/`, params)
		.then((res) => res.data)
}
export const userLogout = (params) => {
	return axios
		.post(`${base}/api-chat/dchat-logout/`, params)
		.then((res) => res.data)
}

// note
export const articleCommit = (params) => {
	return axios
		.post(`${base}/api-note/add-article/`, params)
		.then((res) => res.data)
}

export const articleUpdate = (params) => {
	return axios
		.post(`${base}/api-note/update-article/`, params)
		.then((res) => res.data)
}

export const articleList = (params) => {
	return axios.get(`${base}/api-note/get-userArticle/`, { params: params })
}

// export const articleData = (params) => {
// 	return axios.get(
// 		`${base}/api-note/article/?id=${route.params.id}&userId=${store.userinfo.id}`,
// 		{ params: params }
// 	)
// }

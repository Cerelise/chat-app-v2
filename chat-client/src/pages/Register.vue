<template>
	<div class="flex page">
		<img class="bg" src="http://127.0.0.1:9000/upload/avatar.png" alt="" />
		<div class="register">
			<div class="flex">
				<h1>Cerelise's Channels</h1>
			</div>
			<div class="inputBox">
				<el-input v-model="user.username" class="input" placeholder="用户名" />
			</div>
			<div class="inputBox">
				<el-input
					v-model="user.password"
					class="input"
					type="password"
					placeholder="密码"
					:show-password="true"
				/>
			</div>
			<div class="inputBox">
				<el-input
					v-model="user.repassword"
					class="input"
					type="password"
					placeholder="重复密码"
					:show-password="true"
				/>
			</div>

			<div class="flex-jc-sb inputBox">
				<button @click="register" class="flex reg-button">注册</button>
				<button @click="toLogin" class="flex reg-button">
					已有账号？去登录
				</button>
			</div>
		</div>
	</div>
</template>
<script setup>
// import axios from 'axios'
// import Qs from 'qs'
import { userRegister } from '../api/apis'
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { ElNotification } from 'element-plus'

const user = reactive({
	username: '',
	password: '',
	repassword: '',
})
const store = useStore()
const router = useRouter()

function toLogin() {
	router.push({ name: 'Login' })
}

// function userRegister() {
// 	if (
// 		user.username.length == 0 ||
// 		user.password.length == 0 ||
// 		user.repassword.length == 0
// 	) {
// 		ElNotification({
// 			title: '错误',
// 			message: '表单未填写完整！',
// 			type: 'error',
// 		})
// 		return
// 	}
// 	if (user.password.length < 8) {
// 		ElNotification({
// 			title: '错误',
// 			message: '密码太短！',
// 			type: 'error',
// 		})
// 	}
// 	if (user.password != user.repassword) {
// 		ElNotification({
// 			title: '错误',
// 			message: '两次密码不一致！',
// 			type: 'error',
// 		})
// 	}
// 	// console.log(user)
// 	axios({
// 		method: 'post',
// 		url: 'http://127.0.0.1:9000/api-chat/dchat-register/',
// 		data: Qs.stringify({
// 			username: user.username,
// 			password: user.password,
// 			repassword: user.repassword,
// 		}),
// 	}).then((res) => {
// 		console.log(res.data)
// 		if (res.data == 'this user is exist') {
// 			ElNotification({
// 				title: '错误',
// 				message: '用户名已被注册！',
// 				type: 'error',
// 			})
// 			return
// 		}
// 		store.commit('saveUserinfo', res.data)
// 		ElNotification({
// 			title: '成功',
// 			message: '注册成功！将跳转至登录界面',
// 			type: 'success',
// 		})
// 		router.push({ name: 'Login' })
// 	})
// }

function register() {
	if (
		user.username.length == 0 ||
		user.password.length == 0 ||
		user.repassword.length == 0
	) {
		ElNotification({
			title: '错误',
			message: '表单未填写完整！',
			type: 'error',
		})
		return
	}
	if (user.password.length < 8) {
		ElNotification({
			title: '错误',
			message: '密码太短！',
			type: 'error',
		})
	}
	if (user.password != user.repassword) {
		ElNotification({
			title: '错误',
			message: '两次密码不一致！',
			type: 'error',
		})
	}
	const formData = new FormData()
	formData.append('username', user.username)
	formData.append('password', user.password)
	formData.append('repassword', user.repassword)
	userRegister(formData).then((res) => {
		console.log(res)
		if (res.data == 'this user is exist') {
			ElNotification({
				title: '错误',
				message: '用户名已被注册！',
				type: 'error',
			})
			return
		}
		store.commit('saveUserinfo', res.data)
		ElNotification({
			title: '成功',
			message: '注册成功！将跳转至登录界面',
			type: 'success',
		})
		router.push({ name: 'Login' })
	})
}
</script>

<style scoped>
.page {
	min-height: 100vh;
	border-radius: 15px;
	background: #262335;
	/* box-shadow: 50px -50px 100px #fff, -50px -50px 100px #fff,
		50px 50px 100px #fff, -50px 50px 100px #fff; */
}
.bg {
	max-width: 40vw;
	min-height: 30vh;
	max-height: 60vh;
	margin-right: 5vw;
	border-radius: 15px;
	background: #e0e0e0;
	box-shadow: 50px -50px 100px #34495e, -50px 50px 100px #34495e;
}
.register {
	padding: 60px;
	min-height: 30vh;
	min-width: 30vw;
	max-height: 60vh;
	border-radius: 15px;
	background: #e0e0e060;
	box-shadow: 50px 50px 100px #34495e, -50px -50px 100px #34495e;
}

.inputBox {
	position: relative;
	margin: 50px 0;
}

.input {
	height: 50px;
}

.reg-button {
	width: 200px;
	height: 50px;
	font-size: 22px;
}

button {
	padding: 15px 25px;
	border: unset;
	border-radius: 15px;
	border: solid 2px #6bb4f1;
	color: #6bb4f1;
	z-index: 1;
	position: relative;
	font-weight: 1000;
	font-size: 17px;
	-webkit-box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
	box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
	transition: all 250ms;
	overflow: hidden;
	margin-right: 10px;
}

button::before {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	height: 100%;
	width: 0;
	border-radius: 5px;
	background-color: #6bb4f1;
	z-index: -1;
	-webkit-box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
	box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
	transition: all 250ms;
}

button:hover {
	color: #e8e8e8;
}

button:hover::before {
	width: 100%;
}
</style>

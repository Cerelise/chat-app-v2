<template>
	<div class="flex page">
		<img class="bg" src="http://127.0.0.1:9000/upload/avatar.png" alt="" />
		<div class="login">
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
				<div class="flex flex-jc-fe" style="margin-top: 10px">
					<router-link to="/reset-pwd" class="forgetPwd Link"
						>忘记密码?</router-link
					>
				</div>
			</div>

			<div class="flex-jc-sb inputBox">
				<button @click="toRegister" class="flex loginButton">注册</button>
				<button @click="login" class="flex loginButton">登录</button>
			</div>
		</div>
	</div>
</template>
<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { userLogin } from '../api/apis'
import { ElNotification } from 'element-plus'

const user = reactive({
	username: '',
	password: '',
})
const store = useStore()
const router = useRouter()

function toRegister() {
	router.push({ name: 'Register' })
}

async function login() {
	const formData = new FormData()
	formData.append('username', user.username)
	formData.append('password', user.password)
	await userLogin(formData).then((res) => {
		console.log(res) // token
		if (res == 'user none') {
			ElNotification({
				title: '错误',
				message: '用户名不存在！',
				type: 'error',
			})
			return
		}
		if (res == 'pwd arr') {
			ElNotification({
				title: '错误',
				message: '密码错误！',
				type: 'error',
			})
			return
		}
		localStorage.setItem('token', res)
		store.commit('setToken', res)
		ElNotification({
			title: '成功',
			message: '登录成功',
			type: 'success',
		})
		router.push({ name: 'Homepage' })
	})
}

// function userLogin() {
// 	const formData = new FormData()
// 	formData.append('username', user.username)
// 	formData.append('password', user.password)
// 	console.log(user)
// 	store.dispatch('userLogin', formData)
// 	router.replace({ path: '/' })
// }
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
.login {
	padding: 60px;
	min-height: 30vh;
	min-width: 30vw;
	max-height: 60vh;
	border-radius: 15px;
	background: #e0e0e060;
	box-shadow: 50px 50px 100px #34495e, -50px -50px 100px #34495e;
}
.forgetPwd {
	color: #6bb4f1;
}
.forgetPwd:hover {
	color: #2d4d66;
}

.inputBox {
	position: relative;
	margin: 50px 0;
}

.input {
	height: 50px;
}

.loginButton {
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

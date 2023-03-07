<script setup>
import { ref, reactive, onMounted, computed, nextTick, watch } from 'vue'
import { useStore } from 'vuex'
import axios from 'axios'
import { useRouter } from 'vue-router'
import Search from '../components/Search.vue'
import Options from '../components/Options.vue'
import Navitem from '../components/NavItem.vue'
import UserCard from '../components/UserCard.vue'
import { ElNotification } from 'element-plus'
// const store = useStore()
// const route = useRouter()

const title = ref('')
const websocket = ref('')
const text_input = ref('')
const msgList = reactive([])
const iconList = reactive([
	{ to: '/', icon: 'icon-user-group-fill' },
	{ to: '/chat', icon: 'icon-message1' },
	{ to: '/blog', icon: 'icon-file-fill' },
	{ to: '/all', icon: 'icon-ellipsis' },
])
// const userinfo = reactive([])
const store = useStore()
const route = useRouter()

const userinfo = computed(() => {
	return store.state.userinfo
})

const token = computed(() => {
	return store.state.token
})

// watch((newVal) => {
// 	if (newVal[0]) {
// 		console.log('-----公共频道token监听-----')
// 		console.log(newVal[0])
// 		initWebSocket()
// 	}
// })

// console.log('vuex:' + token.value)
// console.log('vuexu:' + getuserinfo.value)

// 自动登录
function autoLogin() {
	store.dispatch('tryAutoLogin', localStorage.getItem('token'))
}

// 快捷发送
function enterSendmsg() {
	// console.log(e)
	// console.log(websocket.value)
	// if (websocket.readyState == 3) {
	// 	initWebSocket()
	// 	return
	// }
	let msg = {
		code: 200,
		content: {
			token: localStorage.getItem('token'),
			data: {
				text: text_input.value,
			},
		},
	}
	sendMessage(msg)
	text_input.value = ''
}

// 点击发送
function clickToSend() {
	console.log(text_input.value)
	// msgList.push(text_input.value)
	let msg = {
		code: 200,
		content: {
			token: localStorage.getItem('token'),
			data: {
				text: text_input.value,
			},
		},
	}
	sendMessage(msg)
	text_input.value = ''
	// 操作dom 在发送操作执行之后会导致看不到发送的最新的消息
	// let list_dom = document.getElementById('message-list')
	// nextTick(() => {
	// 	list_dom.scrollTop = list_dom.scrollHeight
	// })
}

// 获取标题
function getData() {
	axios({
		method: 'get',
		url: 'http://127.0.0.1:9000/api/',
	}).then((res) => {
		// console.log(res)
		title.value = res.data.title
	})
}

// 初始化websocket
function initWebSocket() {
	websocket.value = new WebSocket('ws://127.0.0.1:9000/chat/myroom/')
	console.log(websocket)
	websocket.value.onopen = onOpen
	websocket.value.onmessage = onMessage
	websocket.value.onerror = onError
	websocket.value.onclose = onClose
}
// 打开链接
function onOpen(e) {
	console.log('ws通信已建立')
	console.log(e)

	let msg = {
		code: 100,
		content: {
			token: localStorage.getItem('token'),
			data: {
				text: '进入房间成功',
			},
		},
	}
	sendMessage(msg)
}

// 接收message
function onMessage(e) {
	// console.log(e)
	let receive = JSON.parse(e.data).message
	console.log(receive)
	if (receive.code == 100 || receive.code == 200) {
		let msg_item = {
			nickName: receive.nickName,
			avatar: receive.avatar,
			data: receive.data,
		}
		msgList.push(msg_item)
		// 操作dom使滚轴自动滚动至最新消息
		let list_dom = document.getElementById('message-list')
		nextTick(() => {
			list_dom.scrollTop = list_dom.scrollHeight
		})
	}
}

// 发送信息
function sendMessage(msg) {
	let text_data = JSON.stringify(msg)
	websocket.value.send(text_data)
}

// 报错
function onError() {}

// 关闭连接
function onClose(e) {
	console.log(e)
	ElNotification({
		title: '错误',
		message: '登录已过期，请重新登录',
		type: 'error',
	})
	route.push({ name: 'Login' })
}

onMounted(() => {
	// autoLogin()
	getData()
	if (localStorage.getItem('token')) {
		initWebSocket()
	}
})
</script>

<template>
	<div class="layout">
		<!-- {{ $store.state.token }} -->
		<nav class="globalNav">
			<div class="nav-top">
				<el-avatar
					class="avatar"
					shape="circle"
					:size="40"
					:src="userinfo.avatar"
				/>
			</div>
			<div class="nav-mid">
				<!-- <div>
					<router-link to="/" class="flex-ac-jsb">
						<TheIcon class="box" icon="icon-user-group-fill" :sizes="22" />
					</router-link>
				</div>
				<div>
					<router-link to="/chat" class="flex-ac-jsb">
						<TheIcon class="box" icon="icon-message1" :sizes="22" />
					</router-link>
				</div>
				<div>
					<router-link to="/blog" class="flex-ac-jsb">
						<TheIcon class="box" icon="icon-file-fill" :sizes="22" />
					</router-link>
				</div>
				<div>
					<router-link to="/all" class="flex-ac-jsb">
						<TheIcon class="box" icon="icon-ellipsis" :sizes="22" />
					</router-link>
				</div> -->

				<Navitem v-for="nav in iconList" :to="nav.to" :icon="nav.icon" />
			</div>
			<div class="nav-down">
				<!-- <router-link to="/settings">
					<div style="margin-top: 12px">
						<TheIcon class="box" icon="icon-setting-fill" :sizes="22" />
					</div>
				</router-link> -->
				<Navitem to="/settings" icon="icon-setting-fill" />
			</div>
		</nav>
		<div class="itemList">
			<!-- <router-view name="userlist"></router-view> -->
			<router-view name="userinfo"></router-view>
			<template v-if="$route.path == '/'">
				<div class="search-area">
					<Search></Search>
				</div>
				<div class="operations">
					<Options
						type="全部用户"
						option1="全部用户"
						option2="在线用户"
					></Options>
				</div>
				<UserCard v-for="item in 4" />
			</template>
		</div>
		<main class="chatPage">
			<!-- <router-view name="pchat"></router-view> -->
			<router-view></router-view>
			<template v-if="$route.path == '/'">
				<div class="header">
					<h2>{{ title }}</h2>
					<div class="userinfo">
						<span>当前用户：</span>
						<img :src="userinfo.avatar" alt="" />
						<span>{{ userinfo.nickName }}</span>
						<!-- {{ store.state.token }} -->
					</div>
				</div>
				<div id="message-list">
					<div v-for="(item, index) in msgList" :key="index">
						<div
							v-if="userinfo.nickName != item.nickName"
							class="other message"
						>
							<img
								:src="'http://127.0.0.1:9000/upload/' + item.avatar"
								alt=""
							/>
							<div class="nickname">{{ item.nickName }}</div>
							<div class="msgtext">{{ item.data.text }}</div>
						</div>
						<div v-else class="self message">
							<img
								:src="'http://127.0.0.1:9000/upload/' + item.avatar"
								alt=""
							/>
							<div class="nickname">{{ item.nickName }}</div>
							<div class="msgtext">{{ item.data.text }}</div>
						</div>
					</div>
				</div>
				<div class="footer">
					<input
						@keydown.enter="enterSendmsg()"
						v-model="text_input"
						type="text"
					/>
					<button @click="clickToSend">send</button>
				</div>
			</template>
		</main>
	</div>
</template>

<style scoped>
.layout {
	width: 100vw;
	height: 100vh;
	max-width: 100%;
	max-height: 100%;
	display: grid;
	grid-template-columns: 5% 25% 70%;
	/* grid-template-rows: 1fr; */
	grid-template-areas: 'nav div main';
	/* justify-content: space-between; */
}

.globalNav {
	grid-area: nav;
	background: #292f4c;
	display: grid;
	grid-template-rows: 2fr 10fr 2fr;
	grid-template-columns: 1fr;
	justify-content: space-between;
	/* color: white; */
}

.nav-top {
	height: 100px;
	display: flex;
	justify-content: center;
	padding: 15px;
}

.nav-mid {
	height: 380px;
	display: grid;
	grid-template-rows: 20% 20% 20% 20%;
	justify-content: center;
	align-items: center;
	/* align-content: space-between; */
	/* border: 1px solid hsl(280deg, 100%, 90%); */
}

.nav-mid div {
	background-clip: content-box;
	/* padding: 10px; */
}
.router-link-exact-active {
	position: relative;
	color: hsl(280deg, 100%, 90%);
}

.router-link-exact-active::before {
	content: '';
	position: absolute;
	width: 3px;
	height: 50px;
	background: hsl(280deg, 100%, 70%);
	left: -12px;
}

.nav-down {
	display: flex;
	justify-content: center;
}

.itemList {
	grid-area: div;
	/* background: #fbfbfb; */
}

#message-list {
	padding: 15px;
	overflow-y: scroll;
}

.footer {
	background: #fbfafa;
	display: flex;
	justify-content: center;
	align-items: center;
}

.footer input {
	width: 80%;
	padding: 8px 14px;
	border: 1px solid hsl(280deg, 50%, 50%);
	border-radius: 4px;
	outline: none;
	background: hsl(280deg, 50%, 30%, 0.2);
	color: white;
	margin-right: 10px;
}

.footer button {
	border: none;
	background: linear-gradient(
		90deg,
		hsl(240deg, 50%, 50%),
		hsl(280deg, 50%, 50%)
	);
	padding: 1em 2em;
	/* margin-top: 24px;
	margin-right: 12px; */
	border-radius: 4px;
	color: white;
}
</style>

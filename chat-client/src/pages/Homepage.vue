<template>
	<div class="layout">
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
				<!-- <Navitem v-for="nav in iconList" :to="nav.to" :icon="nav.icon" /> -->
				<Navitem to="/" icon="icon-user-group-fill" />

				<el-badge v-if="unreadList.length != 0" :value="unreadList.length">
					<Navitem
						@click="openOtherChat(unreadList)"
						to="/chat"
						icon="icon-message1"
					/>
				</el-badge>
				<Navitem v-else to="/chat" icon="icon-message1" />
				<Navitem to="/blog" icon="icon-file-fill" />
				<Navitem to="/all" icon="icon-ellipsis" />
			</div>
			<div class="nav-down">
				<!-- <router-link to="/settings">
					<div style="margin-top: 12px">
						<TheIcon class="box" icon="icon-setting-fill" :sizes="22" />
					</div>
				</router-link> -->
				<Navitem
					@click="changePage()"
					to="/settings"
					icon="icon-setting-fill"
				/>
			</div>
		</nav>
		<div
			:class="{
				itemList_ro_t: openSetting === false,
				itemList_ro_f: openSetting === true,
			}"
		>
			<!-- <router-view :unreadList="unreadList" name="userlist"></router-view> -->
			<router-view
				:unreadList="unreadList"
				:otherChatData="privateList"
				name="userinfo"
				@currentChat="openOtherChat"
			></router-view>
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
				<div class="userlist">
					<UserCard
						v-for="item in userList"
						:name="item.nickName"
						:avatar="item.avatar"
						:desc="item.description"
					/>
				</div>
			</template>
		</div>
		<main class="chatPage">
			<router-view
				@privateMsg="sendMessage"
				@pushSelfMsg="pushSelfMsg"
				:msgList="privateList"
			></router-view>
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
					<!-- <div v-for="(item, index) in msgList" :key="index">
						<div
							v-if="userinfo.nickName != item.nickName"
							class="other message"
						>
							<el-avatar
								:src="'http://127.0.0.1:9000/upload/' + item.avatar"
								@click="openOtherChat(item)"
							/>
							<div class="msgtext">{{ item.data[0].text }}</div>
						</div>

						<div v-else class="self message">
							<el-avatar :src="'http://127.0.0.1:9000/upload/' + item.avatar" />
							<div class="msgtext">{{ item.data[0].text }}</div>
						</div>
					</div> -->
					<div
						v-for="(item, index) in msgList"
						:key="index"
						:class="{
							other: userinfo.nickName != item.nickName,
							self: userinfo.nickName == item.nickName,
						}"
					>
						<div
							class="flex-ai"
							:class="{ flex_di: userinfo.nickName == item.nickName }"
						>
							<el-avatar
								v-if="userinfo.nickName != item.nickName"
								:src="'http://127.0.0.1:9000/upload/' + item.avatar"
								alt=""
								@click="openOtherChat(item)"
							/>
							<el-avatar
								v-else
								:src="'http://127.0.0.1:9000/upload/' + item.avatar"
								alt=""
							/>
							<div class="message" style="text-align: left">
								{{ item.data[0].text }}
							</div>
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

<script setup>
import { ref, reactive, onMounted, computed, nextTick } from 'vue'
import { useStore } from 'vuex'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'
import Search from '../components/Search.vue'
import Options from '../components/Options.vue'
import Navitem from '../components/NavItem.vue'
import UserCard from '../components/UserCard.vue'
import { ElNotification } from 'element-plus'

const store = useStore()
const router = useRouter()
const route = useRoute()

const title = ref('')
const websocket = ref('')
const userList = ref([])
const text_input = ref('')
const msgList = reactive([])
const privateList = reactive({
	nickName: '',
	avatar: '',
	data: [],
	id: Number,
	from: Number,
})
const unreadList = reactive([])
// 监控是否打开了设置页
// const openSetting = ref(false)
// 判断此时是否在聊天页面内
const inOtherChat = ref(false)

// const iconList = reactive([
// 	{ to: '/', icon: 'icon-user-group-fill' },
// 	{ to: '/chat', icon: 'icon-message1' },
// 	{ to: '/blog', icon: 'icon-file-fill' },
// 	{ to: '/all', icon: 'icon-ellipsis' },
// ])

const userinfo = computed(() => {
	return store.state.userinfo
})
// console.log(userinfo.value.id)

const token = computed(() => {
	return store.state.token
})

// 获取用户列表
function getUserList() {
	axios({
		method: 'get',
		url: 'http://127.0.0.1:9000/api-chat/userinfo/',
	}).then((res) => {
		userList.value = res.data
		console.log(userList.value)
	})
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

// 控制列表页与设置页的切换
function changePage() {
	console.log(router.to)
	// if (router.path === '/settings') {
	// 	openSetting = true
	// } else {
	// 	openSetting = false
	// }
}

// 打开私聊窗口
function openOtherChat(data) {
	privateList.nickName = data.nickName
	privateList.avatar = data.avatar
	privateList.data = data.data
	privateList.id = data.id
	privateList.from = data.from
	inOtherChat.value = true
	// privateList.data = []
	router.push({
		name: 'Chat',
	})
	// console.log(privateList)
	// console.log(data)
}
// query 弃用
// function openOtherChat(other) {
// 	router.push({
// 		name: 'Chat',
// 		query: {
// 			nickName: other.nickName,
// 			avatar: other.avatar,
// 			id: other.id,
// 			data: JSON.stringify(other.data),
// 		},
// 	})
// }

function pushSelfMsg(text) {
	privateList.data.push(text)
}

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

// 初始化websocket
function initWebSocket() {
	websocket.value = new WebSocket(
		'ws://127.0.0.1:9000/chat/myroom/' + userinfo.value.id + '/'
	)
	// console.log(websocket)
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
			data: [receive.data],
			id: receive.id,
		}
		msgList.push(msg_item)
		// 操作dom使滚轴自动滚动至最新消息
		let list_dom = document.getElementById('message-list')
		nextTick(() => {
			list_dom.scrollTop = list_dom.scrollHeight
		})
	}
	// 未读消息显示
	if (receive.code == 201) {
		if (inOtherChat.value) {
			// console.log(inOtherChat.value)
			if (privateList.id == receive.from) {
				privateList.data.push(receive.data)
			}
		} else {
			if (unreadList.length == 0) {
				let msg_item = {
					nickName: receive.nickName,
					avatar: receive.avatar,
					data: [receive.data],
					id: receive.id,
					from: receive.from,
				}
				unreadList.push(msg_item)
			} else {
				for (let i = 0; i < unreadList.length; i++) {
					if (unreadList[i].from == receive.from) {
						unreadList[i].data.push(receive.data)
						return
					}
				}
				let msg_item = {
					nickName: receive.nickName,
					avatar: receive.avatar,
					data: [receive.data],
					id: receive.id,
					from: receive.from,
				}
				unreadList.push(msg_item)
			}
		}
	}
}

// 发送信息
function sendMessage(msg) {
	// console.log(msg)
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
	// route.push({ name: 'Login' })
}

onMounted(() => {
	// autoLogin()
	getUserList()
	console.log(userList)
	getData()
	if (localStorage.getItem('token')) {
		initWebSocket()
	}
})
</script>

<style scoped>
.layout {
	width: 100vw;
	height: 100vh;
	max-width: 100%;
	max-height: 100%;
	display: grid;
	grid-template-columns: 80px 30% 10fr;
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

#message-list {
	grid-area: message-list;
	padding: 15px;
	overflow-y: scroll;
}
#message-list .other {
	display: flex;
	justify-content: start;
}
#message-list .self {
	display: flex;
	justify-content: end;
	background-color: none;
}
#message-list .self .message {
	background-color: #4f9dde;
}
.other {
	cursor: pointer;
}
/* .flex_di {
	flex-direction: row-reverse;
} */
</style>

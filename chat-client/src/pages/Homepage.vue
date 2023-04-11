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
				<Navitem to="/note" icon="icon-file-fill" />
				<Navitem to="/all" icon="icon-ellipsis" />
			</div>
			<div class="nav-down">
				<Navitem to="/settings" icon="icon-setting-fill" />
			</div>
		</nav>
		<div
			:class="{
				itemList_ro_t: openSetting === false,
				itemList_ro_f: openSetting === true,
			}"
		>
			<router-view name="userinfo"></router-view>
			<router-view
				:unreadList="unreadList"
				:otherChatData="privateList"
				@currentChat="openOtherChat"
				name="userchat"
			></router-view>
			<router-view name="noteList"></router-view>
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
						@click="openUserinfo(item)"
						:name="item.nickName"
						:avatar="item.avatar"
						:desc="item.description"
					/>
				</div>
			</template>
		</div>
		<main class="rightpage">
			<router-view
				:msgList="privateList"
				:inPrivateChat="inOtherChat"
			></router-view>
			<template v-if="$route.path == '/'">
				<div class="chatpage">
					<div class="header">
						<div class="f-large">Cereliseの自留地</div>
						<div class="f-sub">{{ userList.length }}位成员</div>
					</div>
					<div id="message-list">
						<div
							style="margin: 10px 0"
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
									:size="60"
									v-if="userinfo.nickName != item.nickName"
									:src="'http://127.0.0.1:9000/upload/' + item.avatar"
									alt=""
									@click="openOtherChat(item)"
								/>
								<el-avatar
									v-else
									:size="60"
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
						<MsgInput @publicMsg="sendMessage" />
					</div>
				</div>
			</template>
		</main>
	</div>

	<ProfileEditing :showBox="showEditBox" />
	<el-drawer v-model="userinfoDrawer" direction="rtl" :size="userinfoWidth">
		<div class="standard">
			<div class="ui-header">
				<div class="ui-avatar">
					<img :src="singleUser.avatar" alt="" />
					<el-button type="primary" size="large" circle
						><i class="iconfont">&#xe82e;</i></el-button
					>
				</div>
				<div class="basic">
					<p class="f-large">{{ singleUser.nickName }}</p>
					<p class="f-mid">{{ singleUser.area }}</p>
					<p class="f-small">{{ singleUser.description }}</p>
				</div>
				<div class="flex-ac-jc">
					<div class="flex cm-item">
						<TheIcon icon="icon-github" :sizes="22" />
					</div>
					<div class="flex cm-item">
						<TheIcon icon="icon-bilibili-line" :sizes="22" />
					</div>
				</div>
			</div>
			<el-divider></el-divider>
			<div class="basic-mid">
				<div class="info">联系电话：</div>
				<div style="text-align: left">
					{{ singleUser.phone }}
				</div>
				<div class="info">电子邮件：</div>
				<div>{{ singleUser.email }}</div>
				<div class="info">个人网站：</div>
				<div>test.org</div>
			</div>
		</div>
	</el-drawer>
</template>

<script setup>
import { ref, reactive, onMounted, computed, nextTick, provide } from 'vue'
import { useStore } from 'vuex'
import axios from 'axios'
import { useRouter } from 'vue-router'
import Search from '../components/Search.vue'
import Options from '../components/Options.vue'
import Navitem from '../components/NavItem.vue'
import UserCard from '../components/UserCard.vue'
import TheIcon from '../components/TheIcon.vue'
import MsgInput from '../components/MsgInput.vue'
import ProfileEditing from './ProfileEditing.vue'
import { ElNotification } from 'element-plus'

const store = useStore()
const router = useRouter()
// const route = useRoute()

const websocket = ref('')
const userList = ref([])
const msgList = reactive([])
const singleUser = ref()
const privateList = reactive({
	nickName: '',
	avatar: '',
	data: [],
	id: Number,
	from: Number,
})
const unreadList = reactive([])
// 监控是否打开了设置页
const openSetting = ref(false)
// 判断此时是否在聊天页面内
const inOtherChat = ref(false)
const userinfoDrawer = ref(false)
// 修改个人信息
const showEditBox = ref(false)

const userinfoWidth = computed(() =>
	document.body.clientWidth < 500 ? 300 : '30%'
)

const userinfo = computed(() => {
	return store.state.userinfo
})
provide('userinfoEdit', userinfo)

const userId = computed(() => {
	return store.state.userinfo.id
})
provide('getNoteAuthor', userId)

// 修改个人信息
function goEditpage() {
	showEditBox.value = true
	console.log(showEditBox.value)
}
provide('goEditpage', goEditpage)

function leaveEditpage() {
	showEditBox.value = false
	// console.log(showEditBox.value)
}
provide('leaveEditpage', leaveEditpage)

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

function openUserinfo(info) {
	userinfoDrawer.value = true
	singleUser.value = info
}

// 控制列表页与设置页的切换
// function toSettingPage(data) {
// 	console.log(data)
// 	openSetting.value = data
// }

// 打开私聊窗口
function openOtherChat(data) {
	privateList.nickName = data.nickName
	privateList.avatar = data.avatar
	privateList.data = data.data
	privateList.id = data.id
	privateList.from = data.from
	inOtherChat.value = true

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
provide('pushSelfMsg', pushSelfMsg)

// 自动登录
function autoLogin() {
	store.dispatch('tryAutoLogin', localStorage.getItem('token'))
}

// 统计聊天信息
function unreadListCount() {
	let arr = unreadList
	let count = 0
	arr.forEach((item) => {
		count += item.data.length
	})
	return count
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
provide('sendMessage', sendMessage)

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
	getUserList()
	// getUserArticles()
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
	/* color: hsl(280deg, 100%, 90%); */
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
	background: #0e1621;
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

/* 抽屉面板 */
.basic {
	display: grid;
	justify-content: center;
	justify-items: center;
}

.basic-mid {
	display: grid;
	grid-template-rows: 1fr 1fr 1fr;
	grid-template-columns: 1fr 1fr;
}

.basic-mid > div {
	display: flex;
	justify-content: start;
}

.basic-mid > div:nth-child(odd) {
	justify-content: end;
}

.ui-header {
	grid-area: ui-header;
	display: grid;
	justify-content: center;
	justify-items: center;
	gap: 10px;
}

.ui-avatar {
	position: relative;
}

.ui-header .ui-avatar img {
	width: 100px;
	height: 100px;
	border-radius: 100px;
}

.el-button {
	position: absolute;
	top: 75px;
	right: 0;
}

.cm-item {
	width: 30px;
	height: 30px;
	border-radius: 30px;
	background: #262335;

	margin-right: 20px;
	cursor: pointer;
}
</style>

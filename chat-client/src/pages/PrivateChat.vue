<template>
	<div v-if="!msgList.nickName" class="defaultpage">
		<img
			style="height: 200px; object-fit: cover; object-position: center"
			src="../assets/bg-pic/undraw_chat.svg"
			alt=""
		/>
	</div>
	<div v-else class="chatpage">
		<div class="p-header">
			<el-avatar :src="'http://127.0.0.1:9000/upload/' + msgList.avatar" />
			<div class="info">
				<div class="name">{{ msgList.nickName }}</div>
				<div class="status">在线 最后阅读时间：3小时前</div>
			</div>
		</div>
		<div id="message-list">
			<div v-for="(item, index) in msgList.data" :key="index">
				<div v-if="item.to" class="other">
					<div class="flex-ai">
						<el-avatar
							:src="'http://127.0.0.1:9000/upload/' + msgList.avatar"
						/>
						<div class="message" style="text-align: left">{{ item.text }}</div>
					</div>
				</div>
				<div v-else class="self">
					<div class="flex-ai flex_di">
						<el-avatar :src="userinfo.avatar" />
						<div class="message" style="text-align: right">{{ item.text }}</div>
					</div>
				</div>
			</div>
		</div>
		<div class="footer">
			<!-- <input @keydown.enter="enterSendmsg()" v-model="text_input" type="text" />
			<button @click="clickToSend">send</button> -->
			<MsgInput
				@publicMsg="sendMessage"
				@privateMsg="sendMessage"
				@pushSelfMsg="pushSelfMsg"
				:msgList="msgList"
				:inPrivateChat="inPrivateChat"
			/>
		</div>
	</div>
</template>

<script setup>
import MsgInput from '../components/MsgInput.vue'
import { ref, onMounted, computed, nextTick, watch, inject } from 'vue'
// import { useRoute } from 'vue-router'
import { useStore } from 'vuex'

// const emit = defineEmits(['privateMsg', 'pushSelfMsg'])
const props = defineProps({
	inPrivateChat: Boolean,
	msgList: Array,
})
// const route = useRoute()
const store = useStore()
const text_input = ref('')
// const message = ref('')

const userinfo = computed(() => {
	return store.state.userinfo
})
const sendMessage = inject('sendMessage')
const pushSelfMsg = inject('pushSelfMsg')

watch(
	() => props.inPrivateChat,
	(newVal, oldVal) => {
		console.log(`myProp changed from ${oldVal} to ${newVal}`)
	}
)

onMounted(() => {
	// console.log(route.query)
	// console.log(route.query.data)
	// console.log(id)
	console.log(props.msgList)
})
</script>

<style scoped>
.p-header {
	display: flex;
	align-items: center;
	padding: 15px;
	/* border: 1px solid #fff; */
	color: #fff;
}

.p-header .info {
	flex: 4;
	padding-left: 20px;
	font-size: 14px;
}

#message-list {
	max-height: 73vh;
	padding: 10px;
	overflow-y: scroll;
}

.nickname {
	text-align: left;
}

.msgtext {
	text-align: left;
}

/* .other .el-avatar {
	float: left !important;
} */

/* .self {
	background: #4f9dde;
} */

.self .el-avatar {
	float: right !important;
}

.self .nickname {
	text-align: right;
}

.self .msgtext {
	text-align: right;
}

#message-list .other {
	display: flex;
	justify-content: start;
}
#message-list .self {
	display: flex;
	justify-content: end;
}
#message-list .self .message {
	background-color: aqua;
}
.other {
	cursor: pointer;
}

input {
	width: 80%;
	padding: 8px 14px;
	border: 1px solid hsl(280deg, 50%, 50%);
	border-radius: 4px;
	outline: none;
	background: hsl(280deg, 50%, 30%, 0.2);
	color: white;
	margin-right: 10px;
}

button {
	border: none;
	background: linear-gradient(
		90deg,
		hsl(240deg, 50%, 50%),
		hsl(280deg, 50%, 50%)
	);
	padding: 1em 2em;
	border-radius: 4px;
	color: white;
}
</style>

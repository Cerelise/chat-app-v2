<template>
	<div class="p-header">
		<el-avatar :src="'http://127.0.0.1:9000/upload/' + msgList.avatar" />
		<div class="info">
			<div class="name">{{ msgList.nickName }}</div>
			<div class="status">在线 最后阅读时间：3小时前</div>
		</div>
	</div>
	<div id="message-list">
		<!-- <div v-for="(item, index) in msgList.data" :key="index">
			<div class="flex-ai">
				<el-avatar
					:size="30"
					:src="'http://127.0.0.1:9000/upload/' + msgList.avatar"
				/>
				<div class="message" style="text-align: left">{{ item.text }}</div>
			</div>
		</div> -->

		<!-- <div v-for="(item, index) in msgList.data" :key="index">
			<div v-if="item.to" class="other message">
				<el-avatar
					:size="25"
					:src="'http://127.0.0.1:9000/upload/' + msgList.avatar"
				/>
				<div style="text-align: left">{{ item.text }}</div>
			</div>
			<div v-else class="self message">
				<el-avatar :size="25" :src="userinfo.avatar" />
				<div style="text-align: right">{{ item.text }}</div>
			</div>
		</div> -->
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
		<input @keydown.enter="enterSendmsg()" v-model="text_input" type="text" />
		<button @click="clickToSend">send</button>
	</div>
</template>

<script setup>
import { ref, onMounted, computed, nextTick } from 'vue'
// import { useRoute } from 'vue-router'
import { useStore } from 'vuex'

const emit = defineEmits(['privateMsg', 'pushSelfMsg'])
const props = defineProps({
	msgList: Array,
})
// const route = useRoute()
const store = useStore()
const text_input = ref('')
// const message = ref('')

const userinfo = computed(() => {
	return store.state.userinfo
})

function clickToSend() {
	let msg = {
		code: 201,
		content: {
			token: localStorage.getItem('token'),
			data: {
				to: props.msgList.id,
				text: text_input.value,
			},
		},
	}
	emit('privateMsg', msg)
	text_input.value = ''
	// console.log(route.query)
}

function enterSendmsg() {
	let msg = {
		code: 201,
		content: {
			token: localStorage.getItem('token'),
			data: {
				to: props.msgList.id,
				text: text_input.value,
			},
		},
	}
	emit('privateMsg', msg)
	emit('pushSelfMsg', { text: text_input.value })

	// 操作dom使滚轴自动滚动至最新消息
	let list_dom = document.getElementById('message-list')
	nextTick(() => {
		list_dom.scrollTop = list_dom.scrollHeight
	})

	text_input.value = ''
}

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
	border: 1px solid #fff;
	color: #fff;
}

.p-header .info {
	flex: 4;
	padding-left: 20px;
	font-size: 14px;
}

#message-list {
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
</style>

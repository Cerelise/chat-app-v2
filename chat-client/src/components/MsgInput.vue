<template>
	<div class="input-container">
		<div class="input-icon">
			<TheIcon class="box" icon="icon-clip" :sizes="22" />
		</div>
		<input
			@keydown.enter="enterSendmsg()"
			v-model="text_input"
			type="text"
			placeholder="输入消息..."
		/>
		<div class="input-operations">
			<div><TheIcon class="box" icon="icon-emoji-happy" :sizes="22" /></div>
			<div><TheIcon class="box" icon="icon-voice" :sizes="22" /></div>
			<button class="clickSend">
				<TheIcon
					@click="clickToSend"
					class="box"
					icon="icon-send"
					:sizes="22"
				/>
			</button>
		</div>
	</div>
</template>

<script setup>
import TheIcon from './TheIcon.vue'
import { ref } from 'vue'

const text_input = ref('')
const emit = defineEmits(['publicMsg'])

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
	// sendMessage(msg)
	emit('publicMsg', msg)
	text_input.value = ''
}

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
	emit('publicMsg', msg)
	text_input.value = ''
}
</script>

<style scoped>
.input-container {
	display: flex;
	align-items: center;
	width: 90%;
	background-color: rgba(241, 237, 237, 0.3);
	border-radius: 24px;
	color: white;
	margin-right: 5px;
	padding: 0 20px;
}

.input-icon {
	margin-right: 16px;
}

input {
	width: 100%;
	height: 40px;
	background: rgba(241, 237, 237, 0);
	border: none;
	color: #181c2f;
	outline: none;
}

.input-operations {
	display: flex;
	align-items: center;
	margin-right: -10px;
}

.clickSend {
	border: none;
	outline: none;
	display: inline-flex;
	cursor: pointer;
	justify-content: center;
	align-items: center;
	width: 52px;
	height: 52px;
	border-radius: 50%;
	background-color: #4f9dde;
	margin-right: -15px;
	/* z-index: 10; */
}

.clickSend:hover {
	transform: scale(1.05);
	box-shadow: 0px 6px 16px rgba(204, 102, 255, 0.5);
}

.clickSend .icon {
	color: white !important;
}
</style>

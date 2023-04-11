<template>
	<div class="msg-card">
		<div class="card-container">
			<div class="avatar">
				<el-avatar
					size="medium"
					:src="'http://127.0.0.1:9000/upload/' + avatar"
					alt=""
				/>
			</div>
			<div class="name">{{ name }}</div>
			<div class="p-time">09:23</div>
			<div class="p-status">在线</div>

			<div v-if="!removeUnread" class="flex-ac-jsb p-msg">
				<p>{{ msg }}</p>
				<div class="unread">{{ unread }}</div>
			</div>
			<div v-else class="flex-ac-jsb p-msg">
				<p>{{ msg }}</p>
			</div>
		</div>
	</div>
</template>

<script setup>
// import { onMounted } from 'vue'
const props = defineProps(['name', 'avatar', 'msg', 'unread', 'removeUnread'])
// const emit = defineEmits(['changeSetUI'])

// onMounted(() => {
// 	emit('changeSetUI', false)
// })
</script>

<style scoped>
.msg-card {
	margin: 10px;
	padding: 20px 20px;
	position: relative;

	overflow: hidden;
	border: none;
	border-radius: 6px;
	box-shadow: 0 18px 40px 0 rgba(204, 102, 255, 0.2);
}

/* .msg-card::before,
.msg-card::after {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 0;
}

.msg-card::before {
	content: '';
	background: #1c1e27;
	width: 120%;
	left: -10%;
	transform: skew(30deg);
	transition: transform 0.4s cubic-bezier(0.3, 1, 0.8, 1);
}

.msg-card:hover::before {
	transform: translate3d(100%, 0, 0);
}

.msg-card:active {
	transform: scale(0.95);
	color: #8e2de2;
} */

.card-container {
	position: relative;
	z-index: 10;
	transition: color 0.4s;
	display: grid;
	grid-template-areas:
		'avatar name time'
		'avatar p-status p-status'
		'p-msg p-msg p-msg';
	grid-template-columns: 64px 1fr 1fr;
	/* grid-template-rows: 1fr 1fr 1fr; */
	align-items: center;
	row-gap: 5px;
}

.avatar {
	grid-area: avatar;
}

.name {
	grid-area: name;
	font-size: 20px;
	font-weight: 700;
}

.p-time {
	grid-area: time;
	text-align: right;
}

.p-status {
	grid-area: p-status;
	font-size: 12px;
	color: #76828d;
}

.p-msg {
	grid-area: p-msg;
}

.p-msg p {
	font-size: 16px;
	text-overflow: ellipsis;
	white-space: nowrap;
	overflow: hidden;
}

.p-msg .unread {
	width: 20px;
	height: 20px;
	border-radius: 50%;
	background: #f34848;
	text-align: center;
	line-height: 20px;
}
</style>

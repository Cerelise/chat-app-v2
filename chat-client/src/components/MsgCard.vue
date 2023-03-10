<template>
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

		<div v-if="unread" class="flex-ac-jsb p-msg">
			<p>{{ msg }}</p>
			<div class="unread">{{ unread }}</div>
		</div>
		<div v-else class="flex-ac-jsb p-msg">
			<p>{{ msg }}</p>
		</div>
	</div>
</template>

<script setup>
defineProps(['name', 'avatar', 'msg', 'unread'])
</script>

<style scoped>
.card-container {
	margin: 10px;
	padding: 20px 20px;
	box-shadow: 0 18px 40px 0 rgba(133, 238, 167, 0.2);
	border-radius: 6px;
	display: grid;
	grid-template-areas:
		'avatar name time'
		'avatar p-status p-status'
		'p-msg p-msg p-msg';
	grid-template-columns: 64px 1fr 1fr;
	/* grid-template-rows: 1fr 1fr 1fr; */
	background: #696d81;
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

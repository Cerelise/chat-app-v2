<template>
	<div class="msg-card">
		<div class="card-container">
			<div class="avatar">
				<el-avatar size="medium" :src="avatar" />
			</div>
			<div class="name">{{ name }}</div>
			<div class="status">在线</div>
			<div class="desc">{{ desc }}</div>
		</div>
	</div>
</template>

<script setup>
// import { onMounted } from 'vue'
const props = defineProps(['name', 'avatar', 'desc'])
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
	background: linear-gradient(to right, #8e2de2, #4a00e0);
	overflow: hidden;
	border: none;
	border-radius: 6px;
	box-shadow: 0 18px 40px 0 rgba(204, 102, 255, 0.2);
}
.card-container {
	position: relative;
	z-index: 10;
	transition: color 0.4s;
	display: grid;
	grid-template-areas:
		'avatar name name'
		'avatar status status'
		'desc desc desc';
	grid-template-columns: 64px 1fr 1fr;
	align-items: center;
	row-gap: 5px;
}

.msg-card::before,
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
	background: #0e1621;
	width: 120%;
	left: -10%;
	/* transform: skew(30deg); */
	transition: transform 0.4s cubic-bezier(0.3, 1, 0.8, 1);
}

.msg-card:hover::before {
	transform: translate3d(100%, 0, 0);
}

.msg-card:active {
	transform: scale(0.95);
}

.card-container .avatar {
	grid-area: avatar;
}

.card-container .name {
	grid-area: name;
	font-size: 20px;
	font-weight: 700;
}

.card-container .status {
	grid-area: status;
	font-size: 12px;
	color: #76828d;
}
.card-container .desc {
	grid-area: desc;
	text-overflow: ellipsis;
	overflow: hidden;
	white-space: nowrap;
}
</style>

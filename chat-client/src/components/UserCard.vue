<template>
	<div class="card-container">
		<div class="avatar">
			<el-avatar size="medium" :src="avatar" />
		</div>
		<div class="name">{{ name }}</div>
		<div class="status">在线</div>
		<div class="desc">{{ desc }}</div>
	</div>
</template>

<script setup>
defineProps(['name', 'avatar', 'desc'])
</script>

<style scoped>
.card-container {
	margin: 10px;
	padding: 20px 20px;
	box-shadow: 0 18px 40px 0 rgba(133, 238, 167, 0.2);
	border-radius: 6px;
	display: grid;
	grid-template-areas:
		'avatar name name'
		'avatar status status'
		'desc desc desc';
	grid-template-columns: 64px 1fr 1fr;
	/* grid-template-rows: 1fr 1fr 1fr; */
	background: #696d81;
	align-items: center;
	row-gap: 5px;
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

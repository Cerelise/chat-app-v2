<template>
	<div class="card">
		<el-avatar :size="50" src="http://127.0.0.1:9000/upload/avatar.png" />
		<div class="info">
			<div class="name">Alex</div>
			<div class="status">在线</div>
			<div class="desc">即使爬到最高的山上，一次也只能脚踏实地666</div>
		</div>
	</div>
</template>

<script setup></script>

<style scoped>
.card {
	display: flex;
	align-items: center;
	margin: 15px;
	padding: 10px 12px 10px 24px;
	border: 2px solid hsl(280deg, 100%, 90%);
	border-radius: 10px;
}

.card .info {
	flex: 4;
	padding-left: 20px;
	font-size: 14px;
	min-width: 0;
}

.card .info .desc {
	text-overflow: ellipsis;
	overflow: hidden;
	white-space: nowrap;
}

.card .info .name {
	font-size: 16px;
	padding-bottom: 4px;
}
.card .info .status {
	color: #a5a9ad;
	font-size: 12px;
	padding-bottom: 4px;
}
</style>

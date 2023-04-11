<template>
	<section class="header-wrapper">
		<h1 class="header-area">
			<!-- <strong class="header-text">Markdown编辑器</strong> -->
			<el-input v-model="title" class="input" placeholder="标题..."></el-input>
		</h1>
	</section>
</template>

<script setup></script>

<style scoped>
.header-wrapper {
	height: 60px;
	line-height: 60px;
	/* z-index: 999; */
	box-shadow: 0 0 12px 2px rgba(204, 102, 255, 0.2);
	margin: 10px;
}

.header-wrapper .header-area {
	width: 80%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	margin: auto;
}

.input {
	margin: 20px 0;
	/* height: 50px; */
	width: 40vw;
}
</style>

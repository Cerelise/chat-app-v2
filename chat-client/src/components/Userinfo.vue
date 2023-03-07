<template>
	<div class="basic standard">
		<header>
			<div class="avatar">
				<img :src="userinfo.avatar" alt="" />
				<el-button type="primary" size="large" circle
					><i class="iconfont">&#xe82e;</i></el-button
				>
			</div>
			<p class="f-large">{{ userinfo.nickName }}</p>
			<p class="f-mid">{{ userinfo.area }}</p>
			<p class="f-small">{{ userinfo.description }}</p>
			<div class="cm-account flex-ac-jc">
				<div class="flex cm-item">
					<TheIcon icon="icon-github" :sizes="22" />
				</div>
				<div class="flex cm-item">
					<TheIcon icon="icon-bilibili-line" :sizes="22" />
				</div>
				<!-- <div class="cm-item">
					<a href=""></a>
				</div> -->
			</div>
		</header>
		<el-divider />
		<main>
			<div class="info">联系电话：{{ userinfo.phone }}</div>
			<div class="info">电子邮件：{{ userinfo.email }}</div>
			<div class="info">个人网站：test.org</div>
		</main>
		<el-divider />
		<footer class="standard">測試區</footer>
	</div>
</template>

<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'
import TheIcon from './TheIcon.vue'

const store = useStore()

const userinfo = computed(function () {
	return store.state.userinfo
})
</script>

<style scoped>
.basic {
	display: grid;
	grid-template-rows: 40% 25% 35%;
	grid-template-areas:
		'header'
		'main'
		'footer';
	justify-content: center;
	justify-items: center;
}

header {
	margin-top: 50px;
	display: grid;
	grid-template-columns: 1fr;
	justify-content: center;
	justify-items: center;
	gap: 10px;
}

.avatar {
	position: relative;
}

img {
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
	/* border: 1px solid #fff; */
	margin-right: 20px;
	cursor: pointer;
}
</style>

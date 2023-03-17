<template>
	<div class="settings">
		<div class="flex up">
			<h2>Settings</h2>
		</div>
		<div class="operations">
			<div>
				<h2>账号设置</h2>
				<div>
					<div class="op-item">
						<div class="text">修改个人信息</div>
						<div class="sign">></div>
					</div>
					<div class="op-item">
						<div class="text">修改密码</div>
						<div class="sign">></div>
					</div>
				</div>
			</div>
			<el-divider />
			<div>
				<h2>其他设置</h2>
				<div class="op-item">
					<div class="text">切换账号</div>
					<div class="sign">></div>
				</div>
				<div @click="userLogout" class="op-item">
					<div class="text">退出登录</div>
					<div class="sign">></div>
				</div>
			</div>
			<el-divider />
			<div class="about">
				<h2>关于</h2>
				<div class="introductions">
					<div class="desc">这是一个基于websocket实现的即时通讯聊天室。</div>
				</div>
				<div class="connect">
					<h3 style="color: #fff">联系方式</h3>
					<div class="item">QQ:291244924</div>
					<div class="item">Github:https://github.com/Cerelise/chat-app</div>
					<div class="item">Twitter:https://twitter.com/CatsayerZC</div>
				</div>
			</div>
		</div>
		<div class="flex down">
			<p>copyright@南街清茶</p>
		</div>
	</div>
</template>

<script setup>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { ElNotification } from 'element-plus'

const store = useStore()
const router = useRouter()

function userLogout() {
	store.dispatch('userLogout')
	ElNotification({
		title: 'Success',
		message: '登出成功',
		type: 'success',
	})
	router.push({ name: 'Login' })
}
</script>

<style scoped>
.settings {
	height: 100vh;
	padding: 20px 30px;
	display: grid;
	grid-template-areas:
		'up'
		'operations'
		'down';
	grid-template-rows: 2fr 20fr 2fr;
}

.up {
	grid-area: up;
}

.operations {
	grid-area: operations;
}

.op-item {
	display: flex;
	justify-content: space-between;
	margin: 15px 0 5px 0;
	padding: 10px 30px 10px 30px;
	background: transparent;
	border: none;
	color: #ffedd3;
	position: relative;
	transition: 0.5s ease;
}

.op-item::before {
	content: '';
	position: absolute;
	left: 0;
	bottom: 0;
	height: 2px;
	width: 0;
	background-color: hsl(280deg, 100%, 70%);
	transition: 0.5s ease;
}
.op-item:hover {
	color: #1e1e2b;
	transition-delay: 0.5s;
}

.op-item:hover::before {
	width: 100%;
}

.op-item::after {
	content: '';
	position: absolute;
	left: 0;
	bottom: 0;
	height: 0;
	width: 100%;
	background-color: hsl(280deg, 100%, 70%);
	transition: 0.4s ease;
	z-index: -1;
}

.op-item:hover::after {
	height: 100%;
	transition-delay: 0.4s;
	color: aliceblue;
}

.about {
	display: grid;
	row-gap: 10px;
}

.down {
	grid-area: down;
}

.el-button:focus,
.el-button:hover {
	background: hsl(280deg, 100%, 70%) !important;
	color: #fff;
}
</style>

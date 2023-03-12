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
				<div class="op-item">
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

<script>
import Options from '../components/Options.vue'
import { useRouter } from 'vue-router'
export default {
	components: {
		Options,
	},
	setup() {
		const route = useRouter()

		function userLogout() {
			route.replace({ name: 'Login' })
		}

		return {
			userLogout: userLogout,
		}
	},
}
</script>

<style scoped>
.settings {
	min-height: 730px;
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
	border: 1px solid #fff;
	border-radius: 15px;
}

.op-item:hover {
	background-color: hsl(280deg, 100%, 70%);
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

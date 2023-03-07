<template>
	<div class="flex">
		<h2>Settings</h2>
	</div>
	<div>
		<div>
			<h2>账号设置</h2>
			<div class="flex-ai">
				<el-button text>修改个人信息</el-button>
				<el-button text>修改密码</el-button>
			</div>
		</div>
		<el-divider />
		<div>
			<h2>其他设置</h2>
			<el-button text>切换账号</el-button>
			<el-button text @click="userLogout">登出</el-button>
		</div>
		<el-divider />
		<div>
			<h2>关于</h2>
			<div class="introductions">
				<div class="desc">这是基于websocket实现的即时通讯聊天室。</div>
				<h2>联系方式</h2>
				<div class="item">QQ:291244924</div>
				<div class="item">Github:https://github.com/Cerelise/chat-app-v2</div>
				<div class="item">Twitter:https://twitter.com/CatsayerZC</div>
			</div>
		</div>
	</div>
	<div class="flex">
		<p>copyright@南街清茶</p>
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
.el-button:focus,
.el-button:hover {
	background: hsl(280deg, 100%, 70%) !important;
	color: #fff;
}
</style>

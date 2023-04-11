<template>
	<div class="index-page">
		<section class="flex-cm header-wrapper">
			<div class="flex-cm header-area">
				<!-- <strong class="header-text">Markdown编辑器</strong> -->
				<el-input
					v-model="title"
					class="input"
					placeholder="标题..."
				></el-input>
			</div>
			<div class="flex-cm header-area">
				<el-input v-model="desc" class="input" placeholder="描述..."></el-input>
			</div>
		</section>
		<div id="vditor" class="vditor"></div>
		<div class="flex-cm editFooter">
			<el-button @click="handleSumbit" type="primary">修改</el-button>
			<el-button @click="exitEdit" type="danger">取消</el-button>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { articleList, articleUpdate } from '../../api/apis'
import { ElNotification } from 'element-plus'
// import axios from 'axios'
import useAxios from '../../composables/useAxios'
import Vditor from 'vditor'
import 'vditor/dist/index.css'

const router = useRouter()
const route = useRoute()
const store = useStore()
const axios = useAxios()
const title = ref('')
const desc = ref('')

const user = computed(() => {
	return {
		userId: store.state.userinfo.id,
		token: store.state.userinfo.token,
	}
})

const getUserArticles = () => {
	const userID = user.value.userId
	// console.log(userId)
	articleList({ userId: userID }).then((res) => {
		console.log(res.data)
		articles.value = res.data
	})
}

const initVditor = (content) => {
	vditor.value = new Vditor('vditor', {
		height: 730,
		theme: 'dark',
		icon: 'ant',
		outline: {
			enable: false,
		},
		cache: {
			enable: false,
		},
		typewriterMode: true,
		// value: `# init vditor complete`,
		mode: 'wysiwyg',
		counter: '999999',
		preview: {
			delay: 100,
			theme: {
				current: 'dark',
			},
			math: {
				engine: 'KaTeX',
			},
			hljs: {
				style: 'rrt',
				lineNumber: true,
			},
		},
		after: () => {
			vditor.value.setValue(content)
		},
	})
}

const handleSumbit = () => {
	const token = localStorage.getItem('token')
	const content = vditor.value.getValue()
	const formData = new FormData()
	formData.append('articleId', route.params.id)
	formData.append('title', title.value)
	formData.append('desc', desc.value)
	formData.append('content', content)
	formData.append('token', token)
	// console.log(formData)
	articleUpdate(formData).then((res) => {
		// console.log(res)
		if (res == 'ok') {
			ElNotification({
				title: '成功',
				message: '修改笔记成功',
				type: 'success',
			})
		}
		// getUserArticles()
		router.push({ name: 'noteView', params: { id: route.params.id } })
	})
}

const exitEdit = () => {
	router.push({ name: 'noteView', params: { id: route.params.id } })
}

onMounted(async () => {
	// console.log(route.params)
	// console.log(router.currentRoute.value)
	const userID = user.value.userId
	let res = await axios({
		url: '/api-note/article/?' + 'id=' + route.params.id + '&userId=' + userID,
		method: 'get',
	})
	let receive = res.data
	title.value = receive.title
	desc.value = receive.desc

	initVditor(receive.content)
})
</script>

<style scoped>
.header-wrapper {
	/* z-index: 999; */
	margin: 10px;
}

.header-wrapper .header-area {
	margin: 0 5px;
	width: 50%;
	height: 100%;
	/* margin: auto; */
	box-shadow: 0 0 12px 2px rgba(204, 102, 255, 0.2);
}

.input {
	margin: 20px 10px;
	padding: 10px;
	height: 50px;
	width: 30vw;
}
.index-page .vditor {
	width: 80%;
	margin: 30px 10px;
	box-shadow: 0 0 12px 2px rgba(204, 102, 255, 0.2);
}

.editFooter {
	/* z-index: 999; */
	height: 50px;
	box-shadow: 0 0 12px 2px rgba(204, 102, 255, 0.2);
	margin: 10px;
}
</style>

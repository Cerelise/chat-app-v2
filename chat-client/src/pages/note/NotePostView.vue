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
			<el-button @click="submitArticle" type="primary">发布</el-button>
			<el-button @click="exitPost" type="danger">取消</el-button>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Vditor from 'vditor'
import 'vditor/dist/index.css'
import { articleCommit, articleList } from '../../api/apis'
import { ElNotification } from 'element-plus'

const router = useRouter()
const vditor = ref(null)
const title = ref('')
const desc = ref('')

const initVditor = () => {
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
		upload: {
			accept: 'image/jpg, image/jpeg, image/png',
			// token: localStorage.getItem('token'),
			// 请求的接口
			// url: 'http://127.0.0.1:9000/api-note/article_img/',
			multiple: false,
			filename(name) {
				return name
			},
			// 上传图片回显处理
			// format(files, responseText) {
			// 	const resData = JSON.parse(responseText)
			// 	const name = files[0].name
			// 	const url = resData.upload
			// 	const result = JSON.stringify({
			// 		code: 0,
			// 		data: { errFiles: '', succMap: { [name]: url } },
			// 	})
			// 	return result
			// },
		},
		after: () => {
			vditor.value.setValue(`# init vditor complete`)
		},
	})
}

function getUserArticles() {
	const userID = author.value
	// console.log(userId)
	articleList({ userId: userID }).then((res) => {
		articles.value = res.data
	})
}

const submitArticle = () => {
	const token = localStorage.getItem('token')
	const contents = vditor.value.getValue()
	const formData = new FormData()
	formData.append('title', title.value)
	formData.append('desc', desc.value)
	formData.append('contents', contents)
	formData.append('token', token)
	// console.log(formData)
	articleCommit(formData).then((res) => {
		console.log(res)
		if (res == 'ok') {
			ElNotification({
				title: '成功',
				message: '发布笔记成功',
				type: 'success',
			})
		}
		getUserArticles()
		router.push({ path: '/note' })
	})
}

const exitPost = () => {
	router.push({ path: '/note' })
}

onMounted(() => {
	initVditor()
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

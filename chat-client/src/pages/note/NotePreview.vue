<template>
	<div class="index-page">
		<section class="header-wrapper">
			<div class="header-area">
				<h1 class="title">{{ articleData.title }}</h1>
				<span class="desc">{{ articleData.desc }}</span>
				<div class="flex-cm author-info">
					<el-avatar :size="30" :src="articleData.avatar"></el-avatar>
					<span>{{ articleData.author }}</span>
					<span>|</span>
					<span>{{ articleData.published.split('T')[0] }}</span>
				</div>
			</div>
		</section>
		<!--Markdown-->
		<div id="preview" class="preview"></div>
		<!-- operations -->
		<div
			class="op-row flex-cm"
			style="flex-warp: wrap; justify-content: space-evenly"
		>
			<div>
				<TheIcon @click="editArticle" icon="icon-edit1" :sizes="20" />
			</div>
			<div>
				<TheIcon icon="icon-trash1" :sizes="20" />
			</div>
			<div>
				<TheIcon @click="goBack" icon="icon-ellipsis" :sizes="20" />
			</div>
		</div>
	</div>
</template>

<script setup>
import TheIcon from '../../components/TheIcon.vue'
import Vditor from 'vditor'
import 'vditor/dist/index.css'
import useAxios from '../../composables/useAxios'
import { ref, reactive, onMounted, inject, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

/* this.$route：当前激活的路由的信息对象。每个对象都是局部的，可以获取当前路由的 path, name, params, query 等属性。

this.$router：全局的 router 实例。通过 vue 根实例中注入 router 实例，然后再注入到每个子组件，从而让整个应用都有路由功能。

其中包含了很多属性和对象（比如 history 对象），任何页面也都可以调用其 push(), replace(), go() 等方法。 */
const route = useRoute()
const router = useRouter()
const axios = useAxios()
const articleData = reactive({
	id: '',
	belongUser: '0',
	title: '',
	desc: '',
	content: '',
	author: '',
	published: '',
	avatar: '',
})

const author = inject('getNoteAuthor')

const renderMarkdown = (md) => {
	Vditor.preview(document.getElementById('preview'), md, {
		delay: 100,
		theme: {
			current: 'dark',
		},
		hljs: { style: 'rrt' },
	})
}

const editArticle = () => {
	const articleID = route.params.id
	// console.log(articleID)
	router.push({ name: 'noteEdit', params: { id: articleID } })
}

const goBack = () => {
	router.replace({ path: '/note' })
}

watch(route, async () => {
	const userId = author.value.id
	let res = await axios({
		url: '/api-note/article/?' + 'id=' + route.params.id + '&userId=' + userId,
		method: 'get',
	})
	// console.log(res.data)
	let receive = res.data
	articleData.id = receive.id
	articleData.title = receive.title
	articleData.desc = receive.desc
	articleData.belongUser = receive.belongUser
	articleData.content = receive.content
	articleData.author = receive.nickName
	articleData.published = receive.published
	articleData.avatar = receive.avatar

	renderMarkdown(receive.content)
})

console.log(route.params)
console.log(router.currentRoute.value)

const renderArticle = async () => {
	const userId = author.value
	let res = await axios({
		url: '/api-note/article/?' + 'id=' + route.params.id + '&userId=' + userId,
		method: 'get',
	})
	// console.log(res.data)
	let receive = res.data
	articleData.id = receive.id
	articleData.title = receive.title
	articleData.desc = receive.desc
	articleData.belongUser = receive.belongUser
	articleData.content = receive.content
	articleData.author = receive.nickName
	articleData.published = receive.published
	articleData.avatar = receive.avatar

	renderMarkdown(receive.content)
}

renderArticle()

// onMounted(async () => {

// })
</script>

<style scoped>
.header-area {
	display: grid;
	grid-template-areas:
		'title author-info'
		'desc author-info';
	/* grid-template-columns: 5fr 5fr; */
	grid-template-rows: 5fr 5fr;
	margin: 15px 5px;
	padding: 15px;
	border-radius: 10px;
	box-shadow: 0 0 12px 2px rgba(204, 102, 255, 0.2);
	row-gap: 10px;
}

.header-area .author-info {
	grid-area: author-info;
}

/* .header-area .author-info {

} */
.header-area .author-info span {
	margin: 0 5px;
}

#preview {
	height: 78vh;
}

.index-page .preview {
	overflow: scroll-y;
	width: 65vw;
	margin: 30px 5px;
	padding: 0 5px;
	box-shadow: 0 0 12px 2px rgba(204, 102, 255, 0.2);
}

.op-row {
	position: fixed;
	bottom: 10px;
	margin: 0 5px;
	/* padding: 5px 0; */
	width: 65vw;
	height: 45px;
	border-radius: 10px;
	box-shadow: 5px 0px 10px rgba(204, 102, 255, 0.4),
		-5px 0px 10px rgba(204, 102, 255, 0.2);
}
</style>

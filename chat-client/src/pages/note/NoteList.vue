<template>
	<div class="main-panel">
		<div class="search-area">
			<Search />
		</div>
		<div class="operations">
			<Options type="最新消息" option1="最新消息" option2="最后查看" />
			<div class="add-note">
				<span style="margin-right: 5px">添加笔记</span>
				<!-- <router-link to="/note-post" class="add-btn">
					<span class="icon iconfont icon-add-bold"></span>
				</router-link> -->
				<div @click="toPostArticle" class="add-btn">
					<span class="icon iconfont icon-add-bold"></span>
				</div>
			</div>
		</div>
		<div class="noteList">
			<NoteCard
				v-for="(item, index) in articles"
				:class="{ bg: index == currentIndex }"
				@click="toPreview(index, item.id)"
				:title="item.title"
				:publish="item.publish"
				:desc="item.desc"
			/>
		</div>
	</div>
</template>

<script setup>
// import TheIcon from '../../components/TheIcon.vue'
import Options from '../../components/Options.vue'
import Search from '../../components/Search.vue'
import NoteCard from '../../components/NoteCard.vue'
import { articleList } from '../../api/apis'
import { inject, ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const author = inject('getNoteAuthor')
const articles = ref([])
const currentIndex = ref(-1)
// console.log(author.value)
// 获取用户笔记列表
function getUserArticles() {
	const userID = author.value
	// console.log(userId)
	articleList({ userId: userID }).then((res) => {
		console.log(res.data)
		articles.value = res.data
	})
}

const toPostArticle = () => {
	router.push({ path: '/note-post' })
}

const toPreview = (index, id) => {
	currentIndex.value = index
	router.push({ name: 'noteView', params: { id: id } })
}

onMounted(() => {
	getUserArticles()
})
</script>

<style scoped>
.operations {
	display: grid;
	grid-template-columns: 2fr 1fr;
	align-items: center;
}

.add-note {
	display: inline-flex;
	justify-content: flex-end;
	align-items: center;
	margin: 0 15px;
}

.add-note span {
	font-size: 12px;
}

.add-btn {
	width: 30px;
	height: 30px;
	border-radius: 50%;
	color: white;
	background-color: #4f9dde;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	border: none;
	outline: none;
	cursor: pointer;
	box-shadow: 0 6px 12px rgba(204, 102, 255, 0.2);
}

.add-btn .icon {
	color: white !important;
	/* text-align: center; */
	font-size: 18px;
}

.add-btn:hover {
	transform: scale(1.05);
	box-shadow: 0 6px 16px rgba(204, 102, 255, 0.2);
}
</style>

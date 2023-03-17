<template>
	<div class="main-panel">
		<div class="search-area">
			<Search />
		</div>
		<div class="operations">
			<Options type="最新消息" option1="最新消息" option2="最后查看" />
		</div>
		<div class="msgList">
			<MsgCard
				v-for="(item, index) in unreadList"
				:class="{ bg: index == currentIndex }"
				@click="openChat(index)"
				:name="item.nickName"
				:avatar="item.avatar"
				:msg="item.data[item.data.length - 1].text"
				:unread="item.data.filter((obj) => obj.hasOwnProperty('to')).length"
				:removeUnread="removeUnread"
			/>
			{{ unreadList }}
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import Options from './Options.vue'
import Search from './Search.vue'
import MsgCard from './MsgCard.vue'
// 未读消息
const emit = defineEmits(['currentChat'])
const currentIndex = ref(-1)
const removeUnread = ref(false)
const props = defineProps({
	unreadList: Array,
	otherChatData: Array,
})

function openChat(index) {
	removeUnread.value = true
	currentIndex.value = index
	emit('currentChat', props.unreadList[index])

	// props.unreadList.forEach((obj, index) => {
	// 	if (obj == other) {
	// 		props.unreadList.splice(index, 1)
	// 	}
	// })
}
</script>

<style scope></style>

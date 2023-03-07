<template>
	<span class="icon iconfont" :class="icon" :size="sizes"></span>
</template>

<script setup>
// props: ['icon', 'size']
defineProps({
	icon: String,
	sizes: Number,
})

// interface Props {
// 	icon: string
// 	size: number
// }
// defineProps<Props>()
</script>

<style scoped>
.icon {
	font-size: v-bind(sizes + 'px');
	margin: 0 10px;
	color: #696d81 !important;
}
</style>

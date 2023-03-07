<template>
	<router-view></router-view>
</template>

<script setup>
import { computed, watch } from 'vue'
import { useStore } from 'vuex'

const store = useStore()
const token = computed(() => {
	return store.state.token
})

watch([token], (newVal, oldVal) => {
	if (newVal[0]) {
		console.log('-----token监听-----')
		console.log(newVal, oldVal)
		// 通过router进行自动登录
		store.dispatch('tryAutoLogin', newVal[0])
	}
})
</script>

<style></style>

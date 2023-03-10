<template>
	<div>
		<router-link :to="to" class="flex-ac-jsb">
			<TheIcon class="box" :icon="icon" :sizes="22" />
		</router-link>
	</div>
</template>

<script setup>
import TheIcon from './TheIcon.vue'
// import { onMounted } from 'vue'

defineProps({
	to: String,
	icon: String,
	// unreadList: Object,
})
</script>

<style scoped>
.box {
	transition: all 0.5s ease-in-out;
}

.box:hover {
	transform: scale(1.25);
}

.router-link-exact-active {
	position: relative;
	color: hsl(280deg, 100%, 90%);
}

.router-link-exact-active::before {
	content: '';
	position: absolute;
	width: 3px;
	height: 50px;
	background: hsl(280deg, 100%, 70%);
	left: -12px;
}
</style>

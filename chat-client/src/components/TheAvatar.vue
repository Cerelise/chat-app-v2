<template>
	<el-avatar class="avatar" shape="circle" :size="size" :src="src" />
</template>

<script setup>
const props = defineProps {
  size: number;
  src: string;
}
</script>

<style scoped>
.avatar {
	margin-right: 10px;
}
.commentAvatar {
	margin-top: 10px;
}
</style>

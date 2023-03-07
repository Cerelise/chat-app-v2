<script>
import Options from './Options.vue'
import Search from './Search.vue'
export default {
	components: {
		Options,
		Search,
	},
}
</script>

<template>
	<div class="search-area">
		<Search />
	</div>
	<div class="operations">
		<Options type="最新消息" option1="最新消息" option2="最后查看" />
	</div>
</template>

<style scope></style>

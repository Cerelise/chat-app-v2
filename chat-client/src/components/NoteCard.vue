<template>
	<div class="note-card">
		<div class="card-container">
			<h2 class="title">{{ title }}</h2>
			<div class="publish">{{ publish.split('T')[0] }}</div>
			<div class="note">{{ desc }}</div>
		</div>
	</div>
</template>

<script setup>
const props = defineProps(['title', 'publish', 'desc'])
</script>

<style scoped>
.note-card {
	margin: 10px;
	padding: 35px;
	position: relative;
	overflow: hidden;
	border: none;
	border-radius: 6px;
	box-shadow: 0 18px 40px 0 rgba(204, 102, 255, 0.2);
}

.card-container {
	display: grid;
	grid-template-areas:
		'title publish'
		'note note';
	grid-template-columns: 1fr 0.5fr;
	row-gap: 10px;
}

.publish {
	text-align: right;
	color: #7f8c8d;
	font-size: 15px;
}

.note {
	grid-area: note;
	text-overflow: ellipsis;
	white-space: nowrap;
	overflow: hidden;
}
</style>

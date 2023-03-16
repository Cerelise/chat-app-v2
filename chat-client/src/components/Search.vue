<template>
	<div class="inputContainer">
		<i class="iconfont icon">&#xe82e;</i>
		<input class="input" type="text" placeholder="请输入要搜索的内容..." />
	</div>
</template>

<script></script>

<style scoped>
.inputContainer {
	display: flex;
	line-height: 28px;
	align-items: center;
	position: relative;
	/* border-radius: 24px; */
	padding: 0 10px;
}

.inputContainer i {
	color: #ceced1;
}

.input {
	width: 100%;
	height: 40px;
	line-height: 28px;
	padding: 0 1rem;
	padding-left: 2.5rem;
	border: 2px solid transparent;
	border-radius: 8px;
	outline: none;
	background-color: #f3f3f4;
	color: #0d0c22;
	font-size: 15px;
	transition: 0.3s ease;
}

.input::placeholder {
	color: #9e9ea7;
}

.input:focus,
input:hover {
	outline: none;
	border-color: hsl(280deg, 100%, 70%);
	background-color: #fff;
	box-shadow: 0 0 0 4px rgb(234 76 137 / 10%);
}

.icon {
	position: absolute;
	left: 1.5rem;
	bottom: 1rem;
	fill: #9e9ea7;
	width: 1rem;
	height: 1rem;
}
</style>

<template>
	<div class="header">
		<h2>{{ title }}</h2>
	</div>
	<div id="message-list">
		<div class="message">
			姓名：{{ userinfo.name }} 年龄：{{ userinfo.age }}
		</div>
	</div>
	<div class="footer">
		<input type="text" />
		<button>send</button>
	</div>
</template>

<script></script>

<style scoped>
.header {
	border: 1px solid #fff;
	color: #fff;
}

#message-list {
	padding: 10px;
	overflow-y: scroll;
}

.message {
	width: 30%;
	background: #ffffff;
	text-align: center;
	margin-top: 10px;
	padding: 5px;
	border-radius: 10px;
	font-size: 18px;
	font-weight: 700;
	color: #00000080;
	word-break: break-all;
}
</style>

<template>
	<div class="operation-box">
		<div class="sort">
			<span>排序：</span>
			<el-dropdown>
				<span class="el-dropdown-link flex-ai"
					>{{ type }}
					<el-icon class="el-icon--right"><arrow-down /></el-icon>
				</span>
				<template #dropdown>
					<el-dropdown-menu>
						<el-dropdown-item>{{ option1 }}</el-dropdown-item>
						<el-dropdown-item>{{ option2 }}</el-dropdown-item>
					</el-dropdown-menu>
				</template>
			</el-dropdown>
		</div>
		<div class="other">
			<span>创建会话</span>
			<el-button type="primary" size="small" circle>+</el-button>
		</div>
	</div>
</template>

<script setup>
import { ArrowDown } from '@element-plus/icons-vue'
// export default {
// 	props: ['type', 'option1', 'option2'],
// }
defineProps(['type', 'option1', 'option2'])
</script>

<style scoped>
.operation-box {
	display: grid;
	grid-template-columns: 2fr 1fr;
	align-items: center;
}

.operation-box span {
	font-size: 12px;
	margin-right: 5px;
}

.sort {
	margin-left: 10px;
	display: flex;
	align-items: center;
}

.other .el-button {
	font-size: 18px;
	font-weight: 700;
}

/* .el-dropdown-link .el-tooltip__trigger .el-tooltip__trigger {
	border: none;
} */

.example-showcase .el-dropdown + .el-dropdown {
	margin-left: 15px;
}
.example-showcase .el-dropdown-link {
	cursor: pointer;
	color: var(--el-color-primary);
	display: flex;
	align-items: center;
}
</style>

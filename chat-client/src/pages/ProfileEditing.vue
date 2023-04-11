<template>
	<div v-if="showBox" id="edit-page">
		<div id="edit-box">
			<div class="edit-top">
				<div>个人信息</div>
				<div @click="leaveEdit" class="leaveBtn">x</div>
			</div>
			<div class="flex flex-fd-col edit-main">
				<div class="flex changeAvatar">
					<el-avatar v-if="src" :size="100" :src="src" />
					<el-avatar v-else :size="100" :src="form.avatar" />
					<!-- <el-avatar :size="100" :src="form.avatar" /> -->
					<el-upload
						class="upload-demo flex"
						name="avatar"
						accept="image/png, image/jpeg"
						:auto-upload="false"
						:on-change="Upload"
						:show-file-list="false"
					>
						<el-button class="uploadAvatar" type="primary" circle>+</el-button>
					</el-upload>
				</div>
				<div class="form">
					<el-form :model="form" label-width="120px">
						<el-form-item class="flex" label="用户名:">
							<el-input class="input" v-model="form.nickName" disabled />
						</el-form-item>
						<el-form-item class="flex" label="地区:">
							<el-input class="input" v-model="form.area" />
						</el-form-item>
						<el-form-item class="flex" label="电话:">
							<el-input class="input" v-model="form.phone" />
						</el-form-item>
						<el-form-item class="flex" label="邮箱:">
							<el-input class="input" v-model="form.email" />
						</el-form-item>
						<el-form-item class="flex" label="个人网站:">
							<el-input class="input" v-model="form.website" />
						</el-form-item>
						<el-form-item class="flex" label="个人简介:">
							<el-input
								class="input"
								type="textarea"
								:rows="2"
								v-model="form.desc"
								:maxlength="200"
							/>
						</el-form-item>
						<el-form-item class="button">
							<el-button @click="onSubmit" type="primary">提交更改</el-button>
							<el-button @click="leaveEdit">取消</el-button>
						</el-form-item>
					</el-form>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { useStore } from 'vuex'
import { ref, reactive, inject } from 'vue'
import { ElNotification } from 'element-plus'

const store = useStore()

const props = defineProps({
	showBox: Boolean,
})

const src = ref(null)
const upload = ref()
const leaveEdit = inject('leaveEditpage')
const userinfoEdit = inject('userinfoEdit')

const form = reactive({
	nickName: userinfoEdit.value.nickName,
	avatar: userinfoEdit.value.avatar,
	area: userinfoEdit.value.area,
	phone: userinfoEdit.value.phone,
	email: userinfoEdit.value.email,
	website: userinfoEdit.value.website,
	desc: userinfoEdit.value.description,
})

function Upload(file) {
	// const reader = new FileReader()
	// reader.readAsDataURL(file.raw)
	// const self = src
	// reader.onload = function () {
	// 	self.value = reader.result
	// }
	// _fileObj = file
	// console.log(_fileObj)

	var ext = file.name.substring(file.name.lastIndexOf('.') + 1)
	const extension = ext === 'png'
	const extension2 = ext === 'jpg'
	console.log(extension, extension2)
	src.value = URL.createObjectURL(file.raw)
	if (!extension && !extension2) {
		ElNotification({
			title: '错误',
			message: '上传的不是图片文件，请重新选择',
			type: 'error',
		})
	} else {
		upload.value = file.raw
	}
	console.log(upload.value)
}

function beforeUpload(file) {
	// 判断是否需要阻止文件上传
	var ext = file.name.substring(file.name.lastIndexOf('.') + 1)
	const extension = ext === 'png'
	const extension2 = ext === 'jpg'
	if (!extension && !extension2) {
		ElNotification({
			title: '错误',
			message: '上传的不是图片文件，请重新选择',
			type: 'error',
		})
	}
	return extension || extension2
}

async function onSubmit() {
	const token = localStorage.getItem('token')
	// let files = document.querySelector('.el-upload__input').files[0]
	let formData = new FormData()
	formData.append('token', token)
	formData.append('nickName', form.nickName)
	// formData.append('avatar', files ? files : '')
	formData.append('avatar', upload.value ? upload.value : '')
	formData.append('area', form.area)
	formData.append('email', form.email)
	formData.append('phone', form.phone)
	formData.append('website', form.website)
	formData.append('desc', form.desc)
	console.log(formData)
	await fetch('http://127.0.0.1:9000/api-chat/userinfo/', {
		method: 'PUT',
		body: formData,
	}).then((res) => console.log(res))
	store.dispatch('getUserinfo', token)
	console.log(form)
	leaveEdit()
}
</script>

<style scoped>
#edit-page {
	width: 100vw;
	height: 100vh;
	background-color: #ffffff50;
	position: absolute;
	top: 0;
	left: 0;
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 10;
}

#edit-box {
	min-width: 600px;
	min-height: 700px;
	background: #17212b;
	border-radius: 12px;
}

#edit-box .edit-top {
	display: flex;
	justify-content: space-between;
	padding: 20px;
}

#edit-box .edit-top .leaveBtn {
	cursor: pointer;
}

.changeAvatar {
	position: relative;
	min-width: 30vw;
	margin-left: 20px;
	margin-bottom: 20px;
}

.uploadAvatar {
	position: absolute;
	left: 290px;
	/* right: 150px; */
	bottom: 0;
	margin-left: 20px;
	padding: 15px 15px;
}

.el-form-item__label {
	width: 60px !important;
}
</style>

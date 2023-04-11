<template>
	<div style="display: flex; flex-direction: row; justify-content: center">
		<!-- 一定要在html的部分插入active,
  vue框架才会去真正监听并计算active参数-->
		<div hidden>active: {{ active }}</div>
		<div id="vditor"></div>
	</div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import Vditor from 'vditor'
import 'vditor/dist/index.css'
const vditor = ref(null)
const props = defineProps(['active'])
const active = computed({
	get() {
		if (vditor.value != null) {
			console.log(props.active)
			const mode = props.active ? 'dark' : 'classic'
			vditor.value.setTheme(mode, mode)
		}
		return props.active
	},
})

let content = ''
let width = 0
let height = 0
function ReInitVidor() {
	width = window.innerWidth * 0.92 < 600 ? 600 : window.innerWidth * 0.92
	height = window.innerHeight * 0.9
	vditor.value = new Vditor('vditor', {
		mode: 'sv',
		preview: {},
		icon: 'material',
		height: height,
		width: width,
		placeholder: '君子藏器于身，待时而动',
		counter: {
			enable: true,
		},
		preview: {
			actions: [],
		},
		input: (value) => {
			content = value
		},
		after: () => {
			// vditor.value is a instance of Vditor now and thus can be safely used here
			vditor.value.setValue(content)
		},
	})
}
onMounted(() => {
	window.addEventListener('resize', ReInitVidor)
	ReInitVidor()
})
</script>

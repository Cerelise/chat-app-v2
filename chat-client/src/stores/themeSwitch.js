import { ref, computed } from 'vue'
import { defineStore } from 'vuex'

export const useThemeSwitch = defineStore('themeSwitch', () => {
	const active = ref(false)
	function changeActive(newActive) {
		this.active = newActive
	}

	return { active, changeActive }
})

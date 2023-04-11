import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './routes'
import store from './stores/store'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// import Vditor from 'vditor'
import 'vditor/dist/index.css'
// import * as ElementPlusIconsVue from '@element-plus/icons-vue'

import './assets/iconfont/iconfont.css'

// createApp(App).mount('#app').use(router)
const app = createApp(App)
app.use(ElementPlus)
// app.use(Vditor)
app.use(router)
app.use(store)
app.mount('#app')

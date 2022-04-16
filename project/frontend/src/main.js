import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import axios from 'axios'
// import ElementUI from 'element-plus'
import ElementPlus from 'element-plus'
import { ElMessage} from 'element-plus'
import 'element-plus/dist/index.css';
// import CONSTANT from "@/constant/constant";
const app = createApp(App);
app.use(ElementPlus, { size: 'small', zIndex: 3000 })
app.config.globalProperties.fetchData = function (obj) {
    // let vm = this;
    return axios({
        method: obj.method,
        url: obj.url,
        data: obj.data,
        params: obj.params,
        headers: {
            token: localStorage.getItem('token')
        }
    })
        .then(res => {
            console.log("res", res);
            if(res && res.data) {
                obj.success && obj.success(res.data)
            }else{
                ElMessage.error(res);
                obj.error && obj.error(res)
            }
            // console.log(res)
            // if(res.data && res.data.code === CONSTANT.DEFAULT_SUCCESS.code){
            //     obj.success && obj.success(res.data.data)
            // }else if(res.data && res.data.code === CONSTANT.LACK.code){
            //     ElementUI.Message.error(res.data.msg);
            //     setTimeout(function () {
            //         vm.$router.push('/')
            //     }, 2000)
            // }else{
            //     ElementUI.Message.error(res.data.msg);
            //     obj.error && obj.error(res.data.msg)
            // }
        })
        .catch((err) => {
            ElMessage.error(`Error happens ${err}`);
            obj.error && obj.error(err)
        })
};

app.use(router).mount('#app');

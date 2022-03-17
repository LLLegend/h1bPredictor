import {createRouter, createWebHistory} from "vue-router";
import HelloWorld from "@/components/HelloWorld";
import VisaTrends from "@/components/VisaTrends";
import test from "@/components/test";

const routes = [
    {
        path: '/trends',
        component: VisaTrends
    },
    {
        path: '/',
        component: HelloWorld
    },
    {
        path: '/test',
        component: test
    }

];
export default createRouter({
    history: createWebHistory(),
    routes
})

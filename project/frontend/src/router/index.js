import {createRouter, createWebHistory} from "vue-router";
import HelloWorld from "@/components/HelloWorld";
import VisaTrends from "@/components/VisaTrends";
import test from "@/components/test";
import CaseStatus from "@/components/CaseStatus";
import WorksiteState from "@/components/WorksiteState";
import CasesByEmployer from "@/components/CasesByEmployer";
import CasesByJobTitle from "@/components/CasesByJobTitle";

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
    },
    {
        path: '/case_status',
        component: CaseStatus
    },
    {
        path: '/worksite_state',
        component: WorksiteState
    },
    {
        path: '/cases_by_employer',
        component: CasesByEmployer
    },
    {
        path: '/cases_by_job_title',
        component: CasesByJobTitle
    }


];
export default createRouter({
    history: createWebHistory(),
    routes
})

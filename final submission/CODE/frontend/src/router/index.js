import {createRouter, createWebHistory} from "vue-router";
import HelloWorld from "@/components/HelloWorld";
import VisaTrends from "@/components/VisaTrends";
import test from "@/components/TestComponent";
import CaseStatus from "@/components/CaseStatus";
import WorksiteState from "@/components/WorksiteState";
import CasesByEmployer from "@/components/CasesByEmployer";
import CasesByJobTitle from "@/components/CasesByJobTitle";
import ScrollBar from "@/components/ScrollBar";
import SalaryRange from "@/components/SalaryRange";
import PredictionInput from "@/components/PredictionInput"
import FeatureImportance from "@/components/FeatureImportance";
import TestComponent from "@/components/TestComponent"
import PredictionInputForm from "@/components/PredictionInputForm";
import CertificationRate from "@/components/CertificationRate";
import StackedStatus from "@/components/StackedStatus";

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
    // {
    //     path: '/case_status',
    //     component: CaseStatus
    // },
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
    },
    {
        path: '/salary_range',
        component: SalaryRange
    },
    {
        path: '/predict_case_prob',
        component: PredictionInput

    },
    {
        path: '/feature_importance',
        component: FeatureImportance
    },
    {
        path: '/test',
        component: TestComponent
    },
    {
        path: '/prediction',
        component: PredictionInputForm
    },
    {
        path: '/case_status',
        component: StackedStatus
    }



];
export default createRouter({
    history: createWebHistory(),
    routes
})

<template>
    <div :span="3">
      <el-menu
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          router="true"
      >
        <el-menu-item index="/cases_by_employer">
          <el-icon><Histogram/></el-icon>

          <span>Cases by Employer</span>
        </el-menu-item>
        <el-menu-item index="/cases_by_job_title">
          <el-icon><Histogram/></el-icon>
          <span>Cases by Job Title</span>
        </el-menu-item>
        <el-menu-item index="/case_status">
          <el-icon><TrendCharts/></el-icon>
          <span>Cases Status</span>
        </el-menu-item>
        <el-menu-item index="/trends">
          <el-icon><Histogram/></el-icon>
          <span>Case Trends</span>
        </el-menu-item>
        <el-menu-item index="/worksite_state">
          <el-icon><Location/></el-icon>
          <span>Worksite State</span>
        </el-menu-item>
        <el-menu-item index="/salary_range">
          <el-icon><Histogram/></el-icon>
          <span>Salary Range</span>
        </el-menu-item>
        <el-menu-item index="/feature_importance">
          <el-icon><Histogram/></el-icon>
          <span>Feature Importance</span>
        </el-menu-item>
        <el-menu-item index="/predict_case_prob">
          <el-icon><Opportunity/></el-icon>
          <span>Predict Your Case</span>
        </el-menu-item>

      </el-menu>
    </div>
</template>

<script setup>
import {
  Opportunity,
  Document,
    Histogram,
    TrendCharts,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
const handleOpen = (key, keyPath) => {
  console.log(key, keyPath)
}
const handleClose = (key, keyPath) => {
  console.log(key, keyPath)
}
</script>

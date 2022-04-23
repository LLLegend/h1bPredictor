<template>
  <div id="#CasesByJobTitlePage">
    <h1>Cases by Job Title</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div>
          <new-side-bar />
        </div>
      </el-col>
      <el-col :span="19" align="left">
        <cases-by-job-title-chart/>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import NewSideBar from "@/components/NewSideBar";
import CasesByJobTitleChart from "@/components/CasesByJobTitleChart";
export default {
  name: "CasesByJobTitlePage",
  components: {
    NewSideBar,
    CasesByJobTitleChart,
  },
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

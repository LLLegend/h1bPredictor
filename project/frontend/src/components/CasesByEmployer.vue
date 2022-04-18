<template>
  <div id="#CasesByEmployerPage">
    <h1>Cases by Employer</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div>
          <new-side-bar />
        </div>
      </el-col>
      <el-col :span="19" align="left">
        <cases-by-employer-chart/>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import NewSideBar from "@/components/NewSideBar";
import CasesByEmployerChart from "@/components/CasesByEmployerChart";
export default {
  name: "CasesByEmployer",
  components: {
    NewSideBar,
    CasesByEmployerChart,
  },
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

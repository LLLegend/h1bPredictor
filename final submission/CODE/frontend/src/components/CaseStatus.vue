<template>
  <div id="case_status_page">
    <h1>Applications by Case Status</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div  >
          <new-side-bar/>
        </div>
      </el-col>
      <el-col :span="19" align="left">
        <case-status-chart/>
        <case-status-table/>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import NewSideBar from "@/components/NewSideBar"
import CaseStatusChart from "@/components/CaseStatusChart";
import CaseStatusTable from "@/components/CaseStatusTable"
export default {
  components: {
    NewSideBar,
    CaseStatusChart,
    CaseStatusTable
  },
  name: "CastStatus"
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

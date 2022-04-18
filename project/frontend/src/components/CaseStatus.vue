<template>
  <div id="case_status_page">
    <h1>Case Status</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div :style="{ visibility: hiddenOrVisible }">
          <new-side-bar/>
        </div>
      </el-col>
      <el-col :span="19" align="left">
        <case-status-chart/>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import NewSideBar from "@/components/NewSideBar"
import CaseStatusChart from "@/components/CaseStatusChart";
export default {
  components: {
    NewSideBar,
    CaseStatusChart
  },
  name: "CastStatus"
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

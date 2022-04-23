<template>
  <div id="trendsPage">
    <h1>Visa Trends</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div>
          <new-side-bar/>
        </div>
      </el-col>
      <el-col :span="19" align="left">
        <certification-rate-chart/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import NewSideBar from "@/components/NewSideBar"
import CertificationRateChart from "@/components/CertificationRateChart";

export default {
  name: "CertificationRate",
  components:{
    NewSideBar,
    CertificationRateChart
  },
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

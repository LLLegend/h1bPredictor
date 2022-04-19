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
        <visa-trends-chart/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import NewSideBar from "@/components/NewSideBar"
import VisaTrendsChart from "@/components/VisaTrendsChart";

export default {
  name: "VisaTrends",
  components:{
    NewSideBar,
    VisaTrendsChart,
  },
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

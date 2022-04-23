<template>
  <div id="featureImportancePage">
    <h1>Feature Importance</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div>
          <new-side-bar/>
        </div>
      </el-col>
      <el-col :span="19" align="left" >
        <feature-importance-chart/>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import NewSideBar from "@/components/NewSideBar"
import FeatureImportanceChart from "@/components/FeatureImportanceChart";
export default {
  components: {
    NewSideBar,
    FeatureImportanceChart
  },
  name: "FeatureImportance"
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

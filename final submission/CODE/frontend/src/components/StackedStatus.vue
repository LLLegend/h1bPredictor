<template>
  <div>

    <h1>Applications by Case Status</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div>
          <new-side-bar/>
        </div>
      </el-col>
      <el-col :span="19" align="left">
        <stacked-status-chart/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import StackedStatusChart from "@/components/StackedStatusChart";
import NewSideBar from "@/components/NewSideBar"
export default {
  name: "StackedStatus",
  components: {StackedStatusChart, NewSideBar}
}
</script>

<style scoped>

</style>

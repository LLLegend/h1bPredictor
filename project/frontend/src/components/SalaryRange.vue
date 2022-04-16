<template>
  <div id="trendsPage">
    <h1>Salary Range</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div :style="{ visibility: hiddenOrVisible }">
          <new-side-bar/>
        </div>
      </el-col>
      <el-col :span="19">
        <salary-range-chart/>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import SalaryRangeChart from "@/components/SalaryRangeChart";
import NewSideBar from "@/components/NewSideBar"
export default {
  name: "SalaryRange",
  components:{
    SalaryRangeChart,
    NewSideBar
  }
}
</script>

<style scoped>

</style>

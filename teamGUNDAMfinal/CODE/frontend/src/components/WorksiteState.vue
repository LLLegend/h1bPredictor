<template>
  <div id="worksiteStatePage">

    <h1>Cases by State</h1>

    <el-row :gutter="50">
      <el-col :span="5">
        <div>
          <new-side-bar/>
        </div>
      </el-col>
      <el-col :span="19">
        <worksite-state-chart/>
      </el-col>
    </el-row>
  </div>
</template>

<script>

import WorksiteStateChart from "@/components/WorksiteStateChart";
import NewSideBar from "@/components/NewSideBar"
export default {
  name: "WorksiteState",
  components:{
    WorksiteStateChart,
    NewSideBar,
  },
  data(){
    return{

    }
  }
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
#state-borders {
  fill: none;
  stroke: #fff;
  stroke-width: 1.5px;
  stroke-linejoin: round;
  stroke-linecap: round;
  pointer-events: none;
}
</style>

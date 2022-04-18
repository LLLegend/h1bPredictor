<template>
  <div id="PredictionInput">
    <h1>Predict Your Case</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div>
          <new-side-bar/>
        </div>
      </el-col>
      <el-col :span="19" align="left" >
        <prediction-input-form/>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import NewSideBar from "@/components/NewSideBar"
import PredictionInputForm from "@/components/PredictionInputForm";
export default {
  components: {
    NewSideBar,
    PredictionInputForm
  },
  name: "PredictionInput"
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

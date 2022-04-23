<template>
  <el-table :data="certification_rate" style="width: 100%">
    <el-table-column prop="year" label="Year" width="180" />
    <el-table-column prop="rate" label="Certification Rate" />
  </el-table>
<!--  <div></div>-->
</template>

<script>
export default {
  name: "CaseStatusTable",
  data(){
    return {
      certification_rate: [],
    }
  },
  mounted(){
    this.getCertificationRateData();
  },
  methods:{
    getCertificationRateData() {
      this.fetchData({
        method: "get",
        url: "/api/certification_rate",
        params: {},
        success: (data) => {
          console.log("salaryRange", data)
          let probTableData = [];
          let keys = Object.keys(data);
          console.log("keys",keys)
          for(let idx in keys){
            probTableData.push({"year": keys[idx], "rate": data[keys[idx]]});
          }
          this.certification_rate = probTableData;
          console.log("certification_rate", this.certification_rate);
          // this.$refs.table.updateUI(this.salaryRangeData[0][1]);
          // this.updateUI(this.salaryRangeData[0][0]);
        },
      });
    },
  }
}
</script>

<style scoped>

</style>

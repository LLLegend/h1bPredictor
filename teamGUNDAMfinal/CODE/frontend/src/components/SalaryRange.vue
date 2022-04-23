<template>
  <div id="salaryRangePage">
    <h1>Salary Range</h1>
    <el-row :gutter="50">
      <el-col :span="5">
        <div :style="{ visibility: hiddenOrVisible }">
          <new-side-bar/>
        </div>
      </el-col>
      <el-col :span="19">
        <el-row id = "selectRow"> </el-row>
        <el-row> <salary-range-chart ref="chart"/> </el-row>
        <el-row> <salary-range-table :salaryRangeProb="salaryRangeProb"  ref="table"/> </el-row>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import SalaryRangeChart from "@/components/SalaryRangeChart";
import NewSideBar from "@/components/NewSideBar"
import SalaryRangeTable from "@/components/SalaryRangeTable";
import * as d3 from "d3";
export default {
  name: "SalaryRange",
  components:{
    SalaryRangeChart,
    NewSideBar,
    SalaryRangeTable
  },
  data(){
    return {
      salaryRangeData:[],
      salaryRangeProb:[
        {
          "salary_range":"sldfja",
          "prob":"prob"
        }
      ]
    }
  },
  methods:{
    createDropdown(){
      let yearArr = [2017,2018,2019,2020,2021];

      const dropDown = d3.select("#selectRow")
          .append("select")
          // .attr("class", "selection")
          .attr("id", "Dropdown");
      dropDown
          .selectAll("option")
          .data(yearArr)
          .enter()
          .append("option")
          .text(function (d) {
            console.log(d3.select(this).node().__data__)
            return d;
          })
          .attr("value", function (d) {
            return d;
          });
      let g = this;
      // event listener for the dropdown. Update choropleth and legend when selection changes. Call createMapAndLegend() with required arguments.
      dropDown.on("change", function () {
        let svg = d3.select("#SalaryRangeChart").select("svg")
        svg.selectAll("*").remove();
        svg.remove();
        // recover the option that has been chosen
        var selectedOption = d3.select(this).property("value")
        // run the updateChart function with this selected option
        g.$refs.chart.updateUI(g.salaryRangeData[+selectedOption - 2017][0]);
        g.salaryRangeProb = g.salaryRangeData[+selectedOption - 2017][1];
      })
    },
    getSalaryRangeData() {
      this.fetchData({
        method: "get",
        url: "/api/salary_range",
        params: {},
        success: (data) => {
          console.log("salaryRange", data)
          this.salaryRangeData = data;
          console.log(this.salaryRangeData[0][0], "0")
          this.$refs.chart.updateUI(this.salaryRangeData[0][0]);
          let newProbArr = [];
          let keys = Object.keys(this.salaryRangeData[0][1]);
          console.log("keys",keys)
          for(let idx in keys){
            console.log("idx",idx)
            if(idx == 0){
              newProbArr.push({"salary_range": "$" + +keys[idx] + " to " + "$" + +((+(keys[+idx+1])/1000) - 1)+","+"999", "certified_rate": this.salaryRangeData[0][1][keys[idx]]});
            }
            else if(idx != keys.length - 1){
              newProbArr.push({"salary_range": "$" + +(+keys[idx]/1000)+","+"000" + " to " + "$" + +((+(keys[+idx+1])/1000) - 1)+","+"999", "certified_rate": this.salaryRangeData[0][1][keys[idx]]});
            }else{
              newProbArr.push({"salary_range": ">= $"+ +(+keys[idx]/1000)+","+"000", "certified_rate": this.salaryRangeData[0][1][keys[idx]]});
            }
          }
          this.salaryRangeProb = newProbArr;
          console.log("salaryRangeProb", this.salaryRangeProb);

          // this.$refs.table.updateUI(this.salaryRangeData[0][1]);
          // this.updateUI(this.salaryRangeData[0][0]);
        },
      });
    },
  },

  created() {
    this.getSalaryRangeData();
  },
  mounted() {

  }

}
</script>

<style scoped>

</style>

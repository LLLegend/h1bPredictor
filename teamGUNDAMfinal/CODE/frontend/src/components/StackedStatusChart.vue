<template>
  <div id="StackedStatusChart">

  </div>
</template>

<script>
import * as d3 from "d3";
export default {
  name: "StackedStatusChart",
  created() {
    this.getCaseStatus();
  },
  mounted() {

  },
  data(){
    return {
      statusData:{

      }
    }
  },
  methods:{
    getCaseStatus() {
      this.fetchData({
        method: "get",
        url: "/api/case_status",
        params: {},
        success: (data) => {
          console.log(data);
          this.statusData = data;
          this.updateUI();
        },
      });

    },
    updateUI(){
      // set the dimensions and margins of the graph
      var margin = {top: 70, right: 70, bottom: 70, left: 70},
          width = 960 - margin.left - margin.right,
          height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
      var svg = d3.select("#StackedStatusChart")
          .append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

      // List of subgroups = header of the csv files = soil condition here
      var subgroups = Object.keys(this.statusData[0]);
      console.log("subgroups", subgroups)
      // List of groups = species here = value of the first column called group -> I show them on the X axis
      var groups = ["2017", "2018", "2019", "2020", "2021"];
      // Add X axis
      var x = d3.scaleBand()
          .domain(groups)
          .range([0, width])
          .padding([0.2])
      svg.append("g")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x).tickSizeOuter(0));

      // Add Y axis
      var y = d3.scaleLinear()
          .domain([0, 900000])
          .range([height, 0]);
      svg.append("g")
          .call(d3.axisLeft(y));

      // color palette = one color per subgroup
      // var color = d3.scaleOrdinal()
      //     .domain(subgroups)
      //     .range(['#e41a1c', '#377eb8', '#4daf4a', '#FFFF00'])

      //stack the data? --> stack per subgroup
      var stackedData = d3.stack()
          .keys(subgroups)(this.statusData);
      console.log("stackedData", stackedData);
      // Show the bars
      var colorArray = [d3.schemeCategory10, d3.schemeAccent];
      var colorScheme = d3.scaleOrdinal(colorArray[0]);
      svg.append("g")
          .selectAll("g")
          // Enter in the stack data = loop key per key = group per group
          .data(stackedData)
          .enter().append("g")
          .attr("fill", function (d, i) {
            // console.log("d.key", d, d.key);
            return colorScheme(i);
          })
          .selectAll("rect")
          // enter a second time = loop subgroup per subgroup to add all rectangles
          .data(function (d) {
            // console.log("d", d)
            return d;
          })
          .enter().append("rect")
          .attr("x", function (d, i) {
            return x((2017 + i) + "") + 24;
          })
          .attr("y", function (d) {
            // console.log("d1", d[1])
            return y(d[1]);
          })
          .attr("height", function (d) {
            return y(d[0]) - y(d[1]);
          })
          .attr("width", 80)
      // text label for the y axis
      svg.append("text")
          .attr("id", "y_axis_label")
          .attr("transform", "rotate(-90)")
          .attr("y", 0 - margin.left)
          .attr("x", 0 - (height / 2))
          .attr("dy", "1em")
          .style("text-anchor", "middle")
          .text("Cases");
      svg.append("text")
          .attr("id", "credit")
          .attr("transform", "translate(" + (width - 60) + "," + (height + 30) + ")")
          .style("text-anchor", "right")
          .text("Team GUNDAM");

      const lines = svg.append("g").attr("id", "lines").selectAll("lines")
          .data(subgroups)
          .enter();
      lines.append("rect")
          .attr("style",function (d, i) {
            // console.log(i, colorScheme(i));
            return "fill:"+colorScheme(i);
          })
          .attr("width", 10).attr("height", 10)
          .attr("transform", function(d, i) {
            console.log("d",d)
            return "translate(" + (600)
                + "," +  15 * i + ")";})
          .attr("y", -10);
      lines.append("text")
          .attr("style",function (d, i) {
            // console.log(i, colorScheme(i));
            return "fill:"+colorScheme(i) + ";font-family: Georgia;font-size: 90%;";
          })
          .attr("transform", function(d, i) {
            return "translate(" + (600)
                + "," +  15 * i + ")";})
          .attr("x", 10)
          .text(function(d) { return d; });

      svg.append("g")
          .attr("id", "cases")
          // .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
          .selectAll(".case")
          .data(this.statusData)
          .enter()
          .append("text")
          .attr("class", "caseText")
          // .attr("width", 60)
          .attr("x", function (d, i) {
            // console.log("dd",d)
            return x((i + 2017) + "") + 30;
          })
          // .attr("width", x.bandwidth())
          .attr("y", function (d) {
            console.log("d.values()",Object.values(d));
            return y(d3.sum(Object.values(d)));
          })
          .text(function(d) { return ((Object.values(d)[0] + Object.values(d)[1]) /d3.sum(Object.values(d))*100).toFixed(2) + "%"});
      // text label for the x axis
      svg.append("text")
          .attr("id", "x_axis_label")
          .attr("transform",
              "translate(" + (width / 2) + " ," + (height + 30) + ")")
          .style("text-anchor", "middle")
          .text("Year");
    }
  }
}
</script>

<style scoped>

</style>

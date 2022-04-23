<template>
  <div id="trends">
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "VisaTrends",
  data() {
    return {
      trendData: {},
    }
  },
  created() {
    this.getTrendsAvailable();
  },
  methods: {
    getTrendsAvailable() {
      this.fetchData({
        method: "get",
        url: "/api/trends",
        params: {},
        success: (data) => {
          console.log(data);
          this.trendData = data;
          this.updateUI();
        },
      });
    },
    updateUI() {
      var margin = {top: 0, right: 0, bottom: 0, left: 0},
          padding = {top: 70, right: 70, bottom: 70, left: 70},
          outerWidth = 960,
          outerHeight = 500,
          innerWidth = outerWidth - margin.left - margin.right,
          innerHeight = outerHeight - margin.top - margin.bottom,
          width = innerWidth - padding.left - padding.right,
          height = innerHeight - padding.top - padding.bottom;

      // define function to parse time in years format
      // const formatData = d3.timeParse("%y");
      // create scales x & y for X and Y axis and set their ranges
      var x = d3.scaleBand()
          .range([0, width]);
      var y = d3.scaleLinear()
          .range([height, 0]);

      // // append svg element to the body of the page
      // // set dimensions and position of the svg element
      var svg = d3.select("#trends")
          .append("svg")
          .attr("id", "svg1")
          .attr("width", outerWidth)
          .attr("height", outerHeight)
          .append("g")
          .attr("id", "container")
          .attr("transform", "translate(" + (margin.left + padding.left) + "," + (margin.top + padding.top) + ")");
      let data = [];
      for (let [key, value] of Object.entries(this.trendData)) {
        console.log(key, value);
        data.push({"year": key, "cases": value});
      }
      console.log("data", data);
      // const formatData = d3.timeParse("%Y");
      // data = data.map(function (entry) {
      //   entry.year = formatData(entry.year);
      //   return entry;
      // });
      /* Create bar plot using data from backend*/
      // set the domains of X and Y scales based on data
      x.domain(data.map(function(d) { return +d.year; })).padding(0.1);
      y.domain([0, d3.max(data, d => d.cases)]);

      // append the rectangles for the bar chart
      svg.append("g")
          .attr("id", "bars")
          // .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
          .selectAll(".bar")
          .data(data)
          .enter()
          .append("rect")
          .attr("style", "fill: steelblue;")
          .attr("class", "bar")
          .attr("width", 60)
          .attr("x", function (d) {
            return 44 + x(+d.year);
          })
          // .attr("width", x.bandwidth())
          .attr("y", function (d) {
            return y(d.cases);
          })
          .attr("height", function (d) {
            return height - y(d.cases);
          });
      console.log("bandwidth", x.bandwidth());
      svg.append("g")
          .attr("id", "cases")
          // .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
          .selectAll(".case")
          .data(data)
          .enter()
          .append("text")
          .attr("class", "caseText")
          // .attr("width", 60)
          .attr("x", function (d) {
            return 48 + x(+d.year);
          })
          // .attr("width", x.bandwidth())
          .attr("y", function (d) {
            return y(d.cases);
          })
          .text(function(d) { return d.cases});

      // add the x Axis
      const xAxis = d3.axisBottom(x);
      // xAxis.tickFormat(d3.time.format("%Y"));
      svg.append("g")
          .attr("id", "x_axis")
          .attr("transform", "translate(" + 0 + "," + height + ")")
          .call(xAxis);

      // text label for the x axis
      svg.append("text")
          .attr("id", "x_axis_label")
          .attr("transform",
              "translate(" + (width / 2) + " ," + (height + 30) + ")")
          .style("text-anchor", "middle")
          .text("Year");

      // add the y Axis
      svg.append("g")
          .attr("id", "y_axis")
          .attr("transform", "translate(" + 0 + "," + 0 + ")")
          .call(d3.axisLeft(y));

      // text label for the y axis
      svg.append("text")
          .attr("id", "y_axis_label")
          .attr("transform", "rotate(-90)")
          .attr("y", 0 - padding.left)
          .attr("x", 0 - (height / 2))
          .attr("dy", "1em")
          .style("text-anchor", "middle")
          .text("Cases");

      // svg.append("text")
      //     .attr("id", "title")
      //     .attr("transform",
      //         "translate(" + (width / 2) + "," + -padding.top/2 + ")")
      //     .style("text-anchor", "middle")
      //     .text("Case Trends By Year");

      svg.append("text")
          .attr("id", "credit")
          .attr("transform", "translate(" + (width - 60) + "," + (height + 30) + ")")
          .style("text-anchor", "right")
          .text("Team GUNDAM");

    }
  }

}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

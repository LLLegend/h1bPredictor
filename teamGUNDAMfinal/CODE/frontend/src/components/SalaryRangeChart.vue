<template>
  <div id="SalaryRangeChart">
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "SalaryRangeChart",
  data() {
    return {
      // salaryRangeData: {},
    }
  },
  created() {
    // this.getSalaryRangeData();

  },
  methods: {
    updateUI(salaryRangeData) {
      console.log("updateUICHART")
      // define the dimensions and margins for the graph
      // use the Margin Convention to layout our graph
      var margin = {top: 0, right: 100, bottom: 0, left: 100},
          padding = {top: 60, right: 60, bottom: 60, left: 60},
          outerWidth = 960,
          outerHeight = 500,
          innerWidth = outerWidth - margin.left - margin.right,
          innerHeight = outerHeight - margin.top - margin.bottom,
          width = innerWidth - padding.left - padding.right,
          height = innerHeight - padding.top - padding.bottom;


      // // append svg element to the body of the page
      // // set dimensions and position of the svg element
      var svg = d3.select("#SalaryRangeChart").append("svg")
          .attr("width", outerWidth)
          .attr("height", outerHeight)
          .append("g")
          .attr("transform", "translate(" + (margin.left + padding.left) + "," + (margin.top + padding.top) + ")");

      let data = [];
      for (let [key, value] of Object.entries(salaryRangeData)) {
        data.push({"salary_range": key, "cases": value});
      }
      console.log("data",data)
      // create scales x & y for X and Y axis and set their ranges
      var x = d3.scaleLinear().range([0, width]).domain([0, d3.max(data, function(d) { return d.cases; })]);
      // var y = d3.scaleLinear().range([0, height]).domain(data.map(function(d) { return d.salary_range; })).padding(0.1);
      var y = d3.scaleLinear().range([height, 0])
          .domain([d3.min(data, function(d) { return +d.salary_range; }),
            d3.max(data, function(d) { return +d.salary_range; })
          + (d3.max(data, function(d) { return +d.salary_range; }) - d3.min(data, function(d) { return +d.salary_range; })) / 10 ]);
      svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x).ticks(5)
              .tickFormat(function(d) { return d; })
              .tickSizeInner([-height]));

      var yAxis = d3.axisLeft().scale(y);
      svg.append("g")
          .attr("class", "y axis")
          .call(yAxis.tickValues( Object.keys(salaryRangeData)));

      svg.selectAll(".bar")
          .data(data)
          .enter().append("rect")
          .attr("style", "fill: steelblue;")
          //         .attr("class", "bar")
          .attr("x", 0)
          .attr("height", 30)
          .attr("y", function(d) { return y(+d.salary_range) - 30; })
          .attr("width", function(d) { return x(d.cases); });

      svg.selectAll(".barText")
          .data(data)
          .enter()
          .append("text")
          .attr("x", function(d) {
            console.log(d);
            return x(d.cases);
          })
          .attr("y", function(d) {
            return y(+d.salary_range) - 10;
          })
          .style("text-anchor", "right")
          .text(function(d) {
            return d.cases;
          })



      // text label for the x axis
      svg.append("text")
          .attr("id", "x_axis_label")
          .attr("transform",
              "translate(" + (width / 2) + " ," + (height + 30) + ")")
          .style("text-anchor", "middle")
          .text("Cases");

      // //add a value label to the right of each bar
      // bars.append("text")
      //     .attr("class", "label")
      //     //y position of the label is halfway down the bar
      //     .attr("y", function (d) {
      //       return y(d.employer)  + 4;
      //     })
      //     //x position is 3 pixels to the right of the bar
      //     .attr("x", function (d) {
      //       return x(d.cases) + 3;
      //     })
      //     .text(function (d) {
      //       return d.cases;
      //     });

      // text label for the y axis
      svg.append("text")
          .attr("id", "y_axis_label")
          .attr("transform", "rotate(-90)")
          .attr("y", 0 - padding.left * 2)
          .attr("x", 0 - (height / 2))
          .attr("dy", "1em")
          .style("text-anchor", "middle")
          .text("Salary Range");

      // svg.append("text")
      //     .attr("id", "title")
      //     .attr("transform",
      //         "translate(" + (width / 2) + "," + 0 + ")")
      //     .style("text-anchor", "middle")
      //     .text("Cases by Job Title");

      svg.append("text")
          .attr("id", "credit")
          .attr("transform", "translate(" + (width - 30) + "," + (height + 30) + ")")
          .style("text-anchor", "right")
          .text("Team GUNDAM");
      console.log("END")
    }
  }
}


</script>

<style scoped>
.bar {
  fill: steelblue;
}
</style>

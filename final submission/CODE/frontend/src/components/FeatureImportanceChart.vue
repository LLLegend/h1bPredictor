<template>
  <div id="FeatureImportance">
  </div>
</template>

<script>
import * as d3 from "d3";
export default {
  name: "FeatureImportance",
  data() {
    return {
      FeatureImportanceData: {},
    }
  },
  created() {
    this.getFeatureImportance();
  },
  methods: {
    getFeatureImportance() {
      this.fetchData({
        method: "get",
        url: "/api/feature_importance",
        params: {},
        success: (data) => {
          // console.log(data);
          this.FeatureImportanceData = data;
          this.updateUI(this.FeatureImportanceData);
        },
      });
    },
    updateUI(FeatureImportanceData) {
      // define the dimensions and margins for the graph
      // use the Margin Convention to layout our graph
      var margin = {top: 0, right: 0, bottom: 0, left: 0},
          padding = {top: 60, right: 60, bottom: 60, left: 150},
          outerWidth = 960,
          outerHeight = 500,
          innerWidth = outerWidth - margin.left - margin.right,
          innerHeight = outerHeight - margin.top - margin.bottom,
          width = innerWidth - padding.left - padding.right,
          height = innerHeight - padding.top - padding.bottom;
      // // append svg element to the body of the page
      // // set dimensions and position of the svg element
      var svg = d3.select("#FeatureImportance").append("svg")
          .attr("width", outerWidth)
          .attr("height", outerHeight)
          .append("g")
          .attr("transform", "translate(" + (margin.left + padding.left) + "," + (margin.top + padding.top) + ")");
      let data = [];
      for (let [key, value] of Object.entries(FeatureImportanceData[0]["score"])) {
        data.push({"feature": key, "score": value});
      }
      console.log(data)
      // create scales x & y for X and Y axis and set their ranges
      var x = d3.scaleLinear().range([0, width]).domain([0, d3.max(data, function(d) { return d.score; })]);
      var y = d3.scaleBand().range([0, height]).domain(data.map(function(d) { return d.feature; })).padding(0.1);
      svg.append("g")
          //         .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x).ticks(5)
              .tickFormat(function(d) { return d; })
              .tickSizeInner([-height]));
      svg.append("g")
          //         .attr("class", "y axis")
          .call(d3.axisLeft(y));
      svg.selectAll(".bar")
          .data(data)
          .enter().append("rect")
          .attr("style", "fill: steelblue;")
          //         .attr("class", "bar")
          .attr("x", 0)
          .attr("height", y.bandwidth())
          .attr("y", function(d) { return y(d.feature); })
          .attr("width", function(d) { return x(d.score); });
      svg.selectAll(".barText")
          .data(data)
          .enter()
          .append("text")
          .attr("x", function(d) {
            console.log(d);
            return x(d.score);
          })
          .attr("y", function(d) {
            return y(d.feature) + y.bandwidth()/2;
          })
          .style("text-anchor", "right")
          .text(function(d) {
            return d.score;
          })
      // text label for the x axis
      svg.append("text")
          .attr("id", "x_axis_label")
          .attr("transform",
              "translate(" + (width / 2) + " ," + (height + 30) + ")")
          .style("text-anchor", "middle")
          .text("Score");
      // //add a value label to the right of each bar
      // bars.append("text")
      //     .attr("class", "label")
      //     //y position of the label is halfway down the bar
      //     .attr("y", function (d) {
      //       return y(d.feature)  + 4;
      //     })
      //     //x position is 3 pixels to the right of the bar
      //     .attr("x", function (d) {
      //       return x(d.score) + 3;
      //     })
      //     .text(function (d) {
      //       return d.score;
      //     });
      // text label for the y axis
      svg.append("text")
          .attr("id", "y_axis_label")
          .attr("transform", "rotate(-90)")
          .attr("y", 0 - padding.left * 4)
          .attr("x", 0 - (height / 2))
          .attr("dy", "1em")
          .style("text-anchor", "middle")
          .text("Name");
      svg.append("text")
          .attr("id", "title")
          .attr("transform",
              "translate(" + (width / 2) + "," + -padding.top/4 + ")")
          .style("text-anchor", "middle")
          .text("Score by Name");
      svg.append("text")
          .attr("id", "credit")
          .attr("transform", "translate(" + (width - 70) + "," + (height + 30) + ")")
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

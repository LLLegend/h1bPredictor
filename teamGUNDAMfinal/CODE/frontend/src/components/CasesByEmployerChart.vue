<template>
  <div id="CasesByEmployer"/>
</template>

<script>
import * as d3 from "d3";
export default {
  name: "CasesByEmployerChart",
  data() {
    return {
      casesByEmployerData: {},
    }
  },
  created() {
    // this.createDropdown();
    this.getCasesByEmployer();
  },
  mounted(){
    this.createDropdown();

  },
  methods: {
    createDropdown(){
      let yearArr = [2017,2018,2019,2020,2021];
      const dropDown = d3.select("#CasesByEmployer")
          .append("select")
          // .attr("class", "selection")
          .attr("id", "Dropdown");
      d3.select("#CasesByEmployer").append("br");
      console.log("dropdown", dropDown)
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
        let svg = d3.select("#CasesByEmployer").select("svg")
        svg.selectAll("*").remove();
        svg.remove();
        // recover the option that has been chosen
        var selectedOption = d3.select(this).property("value")
        // run the updateChart function with this selected option
        g.updateUI(g.casesByEmployerData[+selectedOption - 2017]);

      })
    },
    getCasesByEmployer() {
      this.fetchData({
        method: "get",
        url: "/api/cases_by_employer",
        params: {},
        success: (data) => {
          this.casesByEmployerData = data;
          console.log("cao",this.casesByEmployerData)
          this.updateUI(this.casesByEmployerData[0]);
        },
      });
    },
    updateUI(casesByEmployerData) {
      console.log("when updating", casesByEmployerData)
      // define the dimensions and margins for the graph
      // use the Margin Convention to layout our graph
      var margin = {top: 0, right: 0, bottom: 0, left: 0},
          padding = {top: 60, right: 60, bottom: 60, left: 250},
          outerWidth = 960,
          outerHeight = 500,
          innerWidth = outerWidth - margin.left - margin.right,
          innerHeight = outerHeight - margin.top - margin.bottom,
          width = innerWidth - padding.left - padding.right,
          height = innerHeight - padding.top - padding.bottom;



      // // append svg element to the body of the page
      // // set dimensions and position of the svg element
      var svg = d3.select("#CasesByEmployer").append("svg")
          .attr("width", outerWidth)
          .attr("height", outerHeight)
          .append("g")
          .attr("transform", "translate(" + (margin.left + padding.left) + "," + (margin.top + padding.top) + ")");

      let data = [];
      for (let [key, value] of Object.entries(casesByEmployerData)) {
        data.push({"employer": key, "cases": value});
      }
      // console.log("processed",data)
      // create scales x & y for X and Y axis and set their ranges
      var x = d3.scaleLinear().range([0, width]).domain([0, d3.max(data, function(d) { return d.cases; })]);
      var y = d3.scaleBand().range([0, height]).domain(data.map(function(d) { return d.employer; })).padding(0.1);

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
          .attr("y", function(d) { return y(d.employer); })
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
            return y(d.employer) + y.bandwidth()/2;
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
          .attr("y", 0 - padding.left)
          .attr("x", 0 - (height / 2))
          .attr("dy", "1em")
          .style("text-anchor", "middle")
          .text("Employer");

      // svg.append("text")
      //     .attr("id", "title")
      //     .attr("transform",
      //         "translate(" + (width / 2) + "," + 0 + ")")
      //     .style("text-anchor", "middle")
      //     .text("Cases by Employer");

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

</style>

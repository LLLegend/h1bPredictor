<template>
  <div id="case_status">
  </div>
</template>

<script>
import * as d3 from "d3";
export default {
  name: "CastStatus",
  data(){
    return{
    }
  },
  created() {
    console.log("created");
    this.getCaseStatus();
  },
  methods: {
    getCaseStatus() {
      this.fetchData({
        method: "get",
        url: "/api/case_status",
        params: {},
        success: (data) => {
          console.log(data);
          this.caseStatus = data;
          this.update();
        },
      });

    },
    update(){
      let caseStatus = this.caseStatus;
      var margin = {top: 60, right: 60, bottom: 60, left: 100}
          ,outerWidth = 960
          ,outerHeight = 500
          , width = outerWidth - margin.left - margin.right // Use the window's width
          , height = outerHeight - margin.top - margin.bottom; // Use the window's height
      // 1. Add the SVG to the page and employ #2
      var svg = d3.select("#case_status").append("svg")
          .attr("id", "svg")
          .attr("width", (width + margin.left + margin.right))
          .attr("height", (height + margin.top + margin.bottom));

      // svg.append("text").attr("id", "title").attr("transform", "translate(" + (width / 2 + margin.left / 2) + "," + margin.top  / 2  + ")").text("Case Status 2017-2021");

      svg = svg.append("g")
          .attr("id", "plot")
          .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // define function to parse time in years format
      const formatData = d3.timeParse("%Y");
      // create scales x & y for X and Y axis and set their ranges
      console.log("this.case",caseStatus);
      var xScale = d3.scaleTime()
          .domain(d3.extent(caseStatus, (d, idx) => formatData(2017 + idx)))
          .range([0, width]);
      var yScale = d3.scaleLinear()
          .domain([0, d3.max(caseStatus, function (d) {
            return d3.max(Object.values(d));
          })])
          .range([height, 0]);

      //-----------------------------AXES-----------------------------//
      var yaxis = d3.axisLeft()
          .scale(yScale);

      const xaxis = d3.axisBottom()
          .ticks(d3.timeYear)
          // .tickFormat(d3.timeFormat('%Y'))
          .scale(xScale);

      //----------------------------LINES-----------------------------//
      var line = d3.line()
          .x(function (d) {
            console.log(d.year);
            return xScale(d.year);
          })
          .y(function (d) {
            return yScale(d.value);
          });
      //-------------------------2. DRAWING---------------------------//
      //-----------------------------AXES-----------------------------//
      svg.append("g")
          .attr("id", "x-axis")
          .attr("class", "axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xaxis)
          .append("text")
          .text("Year")
          .attr("transform", "translate(" + width / 2 + ",50)");

      svg.append("g")
          .attr("id", "y-axis")
          .attr("class", "axis")
          .call(yaxis)
          .append("text")
          .text("cases")
          .attr("transform", "rotate(-90)")
          .attr("dy", ".75em")
          .attr("y", 6)
          .style("text-anchor", "end");
      //----------------------------LINES-----------------------------//
      var colorArray = [d3.schemeCategory10, d3.schemeAccent];
      var colorScheme = d3.scaleOrdinal(colorArray[0]);
      let statusType = Object.keys(caseStatus[0]);
      console.log("stab1");
      const slices = statusType.map(function (element, idx) {
        let numbers =caseStatus.map(function (e, i) {
          return {
            year: formatData(2017 + i),
            value: Object.values(e)[idx],
          };
        })
        return {
          status: element,
          measurement: numbers
        }
      });
      const lines = svg.append("g").attr("id", "lines").selectAll("lines")
          .data(slices)
          .enter();
      lines.append("path")
          // .attr("class", ids)
          .attr("style", function (d, i) {
            return "fill: none; stroke:" + colorScheme(i) + ";"
          })
          .attr("d", function (d) {
            return line(d.measurement);
          });

      lines.append("rect")
          .attr("style",function (d, i) {
            console.log(i, colorScheme(i));
            return "fill:"+colorScheme(i);
          })
          .attr("width", 10).attr("height", 10)
          .attr("transform", function(d, i) {
            return "translate(" + (xScale(d.measurement[3].year))
                + "," +  15 * i + ")";})
          .attr("y", -10);
      lines.append("text")
          .attr("style",function (d, i) {
            console.log(i, colorScheme(i));
            return "fill:"+colorScheme(i) + ";font-family: Georgia;font-size: 90%;";
          })
          .attr("transform", function(d, i) {
            return "translate(" + (xScale(d.measurement[3].year))
                + "," +  15 * i + ")";})
          .attr("x", 10)
          .text(function(d) { return d.status; });
      for(let line = 0; line < 5; line++){
        if(line == 3){
          lines.append("text")
              .attr("style","font-family: Georgia;font-size: 90%;")
              .attr("transform", function(d) {
                console.log("d", d);
                return "translate(" + xScale(d.measurement[line].year)
                    + "," +  yScale(d.measurement[0].value) + ")";})
              .attr("x", 10)
              .text(function(d) { return d.measurement[line].value; });
        }
        else{
          lines.append("text")
              .attr("style","font-family: Georgia;font-size: 70%;")
              .attr("transform", function(d) {
                console.log("d", d);
                return "translate(" + xScale(d.measurement[line].year)
                    + "," +  yScale(d.measurement[line].value) + ")";})
              .attr("x", 10)
              .text(function(d) { return d.measurement[line].value; });
        }

      }

    }
  }
}


</script>

<style scoped>

</style>

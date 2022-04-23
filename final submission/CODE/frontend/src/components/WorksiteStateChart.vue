<template>
  <div id="worksiteState">
    <el-row>
      <el-col :span="5" >
        <span class="demonstration" >Select Year</span>
        <el-slider
            v-model="year"
            :min="2017"
            :max="2021"
            :step="1"
            show-stops
            @change="handleSliding">
        </el-slider>
      </el-col>
    </el-row>
    <br>
  </div>
</template>

<script>
import * as d3 from "d3";
// import {geoAlbers} from "d3-geo-projection"
import {geoAlbersUsa, geoPath} from "d3-geo"
import { legendColor } from 'd3-svg-legend'
import {feature, mesh} from 'topojson'

export default {
  name: "WorksiteState",
  data() {
    return {
      worksiteStateData: {},
      year: 2017
    }
  },
  created() {
    this.getWorksiteStateData();
  },
  methods: {
    handleSliding(year){
      let svg = d3.select("#worksiteState").select("svg")
      svg.selectAll("*").remove();
      svg.remove();
      this.updateUI(year);
      // console.log("E", e);
    },
    updateUI(idx) {
      let worksiteStateData = this.worksiteStateData[+idx - 2017];
      // console.log("updating UI...");
      // console.log("this.worksiteStateData", worksiteStateData);

      d3.json("/api/download/state.topo.json").then(function (US) {
        console.log(US);
        let svg = d3.select("#worksiteState").append("svg");
        // enter code to define margin and dimensions for svg
        const margin = {top: 100, right: 100, bottom: 100, left: 100};
        const width = 1920 - margin.left - margin.right, height = 1080 - margin.top - margin.bottom;
        svg = svg
            .attr("id", "choropleth")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("id", "states")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // enter code to create color scale
        // Data and color scale
        // var data = d3.map();
        const color = d3
            .scaleThreshold()
            .domain(d3.range(2, 8))
            .range(d3.schemeBlues[7]);

        // enter code to define projection and path required for Choropleth
        // For grading, set the name of functions for projection and path as "projection" and "path"
        const projection = geoAlbersUsa();
        var path = geoPath().projection(projection);
        // console.log(d3.values(worksiteStateData));
        let statistics = {
          high: d3.max(Object.values(worksiteStateData)),
          low: d3.min(Object.values(worksiteStateData)),
          ...worksiteStateData
        }
        // console.log("statistics", statistics);
        // create Choropleth
        const pieces = 7;
        const tenth = (statistics.high - statistics.low) / pieces;
        // var labels =
        //     [statistics.low.toFixed(2) + " to " + (statistics.low + quarter).toFixed(2),
        //       (statistics.low + quarter).toFixed(2) + " to " + (statistics.low + 2 * quarter).toFixed(2),
        //       (statistics.low + 2 * quarter).toFixed(2) + " to " + (statistics.low + 3 * quarter).toFixed(2),
        //       (statistics.low + 3 * quarter).toFixed(2) + " to " + statistics.high.toFixed(2)];
        let labels = [];
        let first = ~~statistics.low;
        let second = ~~(statistics.low + tenth);
        for(let i = 0; i < pieces; i++){
          labels.push(first + " to " + second);
          first = second;
          second = ~~(second + tenth);
        }
        console.log("before")
        svg.selectAll("path")
            .data(feature(US, US.objects.state).features)
            // .data(US.features)
            .enter()
            .append("path")
            .attr("fill", function (d) {
              // d.name = statistics[d.properties.name]
              if(d.properties.NAME10 === "District of Columbia"){
                return color(Math.ceil((statistics["District Of Columbia"] - statistics.low) / tenth));
              }
              if (!statistics[d.properties.NAME10]) {
                console.log(d.properties.NAME10, "does not exist");
                return "grey";
              }
              return color(Math.ceil((statistics[d.properties.NAME10] - statistics.low) / tenth));
            })
            .attr("d", path);
        svg.datum(mesh(US, US.objects.state, function(a, b) { return a !== b; }))
            .attr("id", "state-borders")
            .attr("style", "fill: none;" +
                "  stroke: #fff;" +
                "  stroke-width: 1.5px;" +
                "  stroke-linejoin: round;" +
                "  stroke-linecap: round;" +
                "  pointer-events: none;");
        console.log("after")
        var gLegend = d3.select("#worksiteState").select("svg")
            .append("g")
            .attr("id", "legend")
        var legend = legendColor()
            .labels(function (d) {
              return labels[d.i];
            })
            .shapePadding(4)
            .scale(color);
        gLegend.call(legend);
      })
    },
    getWorksiteStateData() {
      return this.fetchData({
        method: "get",
        url: "/api/worksite_state",
        params: {},
        success: (data) => {
          console.log(data);
          this.worksiteStateData = data;
          this.updateUI(2017);
        },
      });
    },
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

<template>
  <div class="hello">
    <img alt="GUNDAM logo" src="../assets/logo.jpeg" height="100" width="100">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://github.com/budd713/datadreamteam" target="_blank" rel="noopener">General Unlimited Networks Data Analytics and Manipulation</a>.
    </p>
    <h3>Technical Stack</h3>
    <ul>
      <li><a href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank" rel="noopener">Flask</a></li>
      <li><a href="https://vuejs.org/" target="_blank" rel="noopener">Vue.js</a></li>
    </ul>
    <h3>Explore</h3>
    <ul>
      <li><router-link to="/trends">Trends</router-link></li>
      <li><router-link to="/case_status">Case Status</router-link></li>
      <li><router-link to="/worksite_state">Worksite by State</router-link></li>

      <li><router-link to="/cases_by_employer">Cases by Employer</router-link></li>
      <li><router-link to="/cases_by_job_title">Cases by Job Title</router-link></li>
      <li><router-link to="/salary_range">Salary Range</router-link></li>
      <li><router-link to="/test">Job Titles</router-link></li>
      <li><router-link to="/test">Cities</router-link></li>
    </ul>
    <h3>Team</h3>
    <ul>
      <li><a href="https://github.com/budd713" target="_blank" rel="noopener">Alex</a></li>
      <li><a href="https://gtsi.edu.cn" target="_blank" rel="noopener">Chuanqi</a></li>
      <li><a href="https://gtsi.edu.cn" target="_blank" rel="noopener">Qinrui</a></li>
      <li><a href="https://github.com/tianshut" target="_blank" rel="noopener">Tianshu</a></li>
      <li><a href="https://github.com/terrylitianyu" target="_blank" rel="noopener">Tianyu</a></li>
    </ul>
  </div>
</template>

<script>
import "./NewSideBar"
import NewSideBar from "@/components/NewSideBar";
export default {
  name: 'HelloWorld',
  components: {NewSideBar},
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

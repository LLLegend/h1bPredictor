<template>
  <div>
    <el-form :model="form" ref="form" :rules="rules" label-width="120px">
      <el-form-item label="Company/Employer">
        <el-autocomplete
            v-model="form.employer"
            :fetch-suggestions="querySearch"
            clearable
            class="inline-input"
            placeholder="Please Input"
            @select="handleSelect"
        />
      </el-form-item>
      <el-form-item label="Job Title">
        <el-autocomplete
            v-model="form.jobTitle"
            :fetch-suggestions="querySearchJob"
            clearable
            class="inline-input"
            placeholder="Please Input"
            @select="handleSelect"
        />
      </el-form-item>
      <el-form-item label="Worksite City">
        <el-autocomplete
            v-model="form.city"
            :fetch-suggestions="querySearchCity"
            clearable
            class="inline-input"
            placeholder="Please Input"
            @select="handleSelect"
        />
      </el-form-item>
      <el-form-item label="Worksite State">
        <el-autocomplete
            v-model="form.state"
            :fetch-suggestions="querySearchState"
            clearable
            class="inline-input"
            placeholder="Please Input"
            @select="handleSelect"
        />
      </el-form-item>
      <el-form-item label="Expected Wage">
        <el-input
            v-model="form.wage"
            clearable
            class="inline-input"
            placeholder="Please Input"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit('form')">Predict</el-button>
        <el-button @click="resetForm('form')">Reset</el-button>
      </el-form-item>

    </el-form>
    <el-table
        :data="tableData"
        style="width: 100%">
      <el-table-column
          prop="employer"
          label="Employer/Company"
          width="180">
      </el-table-column>
      <el-table-column
          prop="jobTitle"
          label="Job Title"
          width="180">
      </el-table-column>
      <el-table-column
          prop="city"
          label="Worksite City">
      </el-table-column>
      <el-table-column
          prop="state"
          label="Worksite State">
      </el-table-column>
      <el-table-column
          prop="prob"
          label="Prob">
      </el-table-column>
      <el-table-column
          prop="wage"
          label="Expected Wage">
      </el-table-column>
    </el-table>
  </div>

</template>

<script>
// import { reactive } from 'vue'
export default {
  data() {
    return {
      form: {
        employer: null,
        jobTitle: null,
        city: null,
        state: null,
        wage: 0,
      },
      employer: '',
      jobTitle: '',
      city: '',
      state: '',
      wage: 0,
      employerList: [],
      jobTitleList: [],
      cityList: [],
      stateList: [],
      tableData: [],
      rules: {
        employer: [
          { required: true, message:'Please input the employer', trigger: 'change'}
        ],
        jobTitle: [
          { required: true, message:'Please input the job title', trigger: 'change'}
        ],
        city: [
          { required: true, message:'Please input the city', trigger: 'change'}
        ],
        state: [
          { required: true, message:'Please input the state', trigger: 'change'}
        ],
        wage: [
          { required: true,type: 'number', message:'Please input the wage', trigger: 'change'},
          {min: 0, message: '长度在 3 到 5 个字符', trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    onSubmit(formName){
      this.$refs[formName].validate((valid) => {
        if (valid) {
          let employerList = this.employerList.map(function(e){
            return e.value;
          })
          let cityList = this.cityList.map(function(e){
            return e.value;
          });
          let stateList = this.stateList.map(function(e){
            return e.value;
          });
          let jobTitleList = this.jobTitleList.map(function(e){
            return e.value;
          });
          if(!employerList.includes(this.form.employer)){
            // console.log("cityList", this.cityList);
            alert('Invalid employer!'+this.form.employer);
            return false;
          }
          else if(!cityList.includes(this.form.city)){
            // console.log("cityList", this.cityList);
            alert('Invalid city!'+this.form.city);
            return false;
          }
          else if(!stateList.includes(this.form.state)){
            alert('Invalid state!');
            return false;
          }
          else if(!jobTitleList.includes(this.form.jobTitle)){
            alert('Invalid job title!');
            return false;
          }
          else if(isNaN(+this.form.wage) || +this.form.wage < 0) {
            alert('Invalid wage!');
            return false;
          }

          this.fetchData({
            method: "get",
            url: "/api/predict_case_prob",
            params: this.form,
            success: (data) => {
              this.tableData.push({
                "employer": this.form.employer, "jobTitle": this.form.jobTitle,
                "city": this.form.city, "state": this.form.state, "wage": this.form.wage, "prob": data[0]
              });
            }
          });
          return true;
        } else {
          alert('error submit!!');
          return false;
        }
      });
      // console.log(vue);
      // vue.fetchData({
      //   method: "get",
      //   url: "/api/predict_case_prob",
      //   params: vue.form,
      //   success: (data) => {
      //     vue.tableData.push({"employer": vue.form.employer,"jobTitle": vue.form.jobTitle,
      //       "city": vue.form.city,"state":vue.form.state, "wage": vue.form.wage, "prob":data[0]});
      //   }
      // });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    querySearch(queryString, cb) {
      var employerList = this.employerList;
      var results = queryString ? employerList.filter(this.createFilter(queryString)) : employerList;
      // 调用 callback 返回建议列表的数据
      // console.log(results)
      cb(results);
    },
    querySearchJob(queryString, cb) {
      var jobTitleList = this.jobTitleList;
      var results = queryString ? jobTitleList.filter(this.createFilter(queryString)) : jobTitleList;
      // 调用 callback 返回建议列表的数据
      // console.log(results.sort())
      cb(results);
    },
    querySearchCity(queryString, cb) {
      var cityList = this.cityList;
      var results = queryString ? cityList.filter(this.createFilter(queryString)) : cityList;
      // 调用 callback 返回建议列表的数据
      // console.log(results)
      cb(results);
    },
    querySearchState(queryString, cb) {
      var stateList = this.stateList;
      var results = queryString ? stateList.filter(this.createFilter(queryString)) : stateList;
      // 调用 callback 返回建议列表的数据
      // console.log(results)
      cb(results);
    },
    createFilter(queryString) {
      return (entity) => {
        return (entity.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
      };
    },
    loadAll() {
      this.fetchData({
        method: "get",
        url: "/api/job_list",
        params: {},
        success: (data) => {
          for (let value of data) {
            this.jobTitleList.push({"value": value});
          }
          // console.log(data.sort());
        }
      });
      this.fetchData({
        method: "get",
        url: "/api/employer_list",
        params: {},
        success:(data) => {
          for (let value of data) {
            this.employerList.push({"value": value});
          }
          // console.log(data.sort())
        }
      });
      this.fetchData({
        method: "get",
        url: "/api/city_list",
        params: {},
        success:(data) => {
          for (let value of data) {
            this.cityList.push({"value": value});
          }
          // console.log(data.sort())
        }
      });
      this.fetchData({
        method: "get",
        url: "/api/state_list",
        params: {},
        success:(data) => {
          for (let value of data) {
            this.stateList.push({"value": value});
          }
          // console.log(data.sort())
        }
      });
    },
    loadTest(){
      return [];
    },
    handleSelect(item) {
      console.log(item);
    }
  },
  created() {
    this.loadAll()
  },
  mounted() {
  }
}

</script>
<style scoped>
</style>

<template>
  <el-table :data="salaryRangeProb" style="width: 100%">
    <el-table-column prop="salary_range" label="salary range" width="180" />
    <el-table-column prop="certified_rate" label="certified_rate" />
  </el-table>
</template>

<script>
// import { toRaw } from '@vue/reactivity'
export default {
  name: "SalaryRangeTable",
  props: ["salaryRangeProb"],
}

</script>

<style scoped>

</style>

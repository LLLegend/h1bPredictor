<template>
  <el-menu default-active="$router.path" router>
    <el-menu-item
      v-for="(value, name, index) in navObject"
      :key="index"
      :index="value.path"
      v-show="value.show"
      @click="handleClick(name)"/>
  </el-menu>
</template>

<script>
export default {
  name: "SideBar",

  data() {
    return {
      username: "",
      navObject: {
        casesByEmployer: {
          icon: "el-icon-document",
          title: "Cases by Employer",
          path: "/cases_by_employer",
          show: true,
        },
        addVehicle: {
          icon: "el-icon-truck",
          title: "Cases by Job Title",
          path: "/cases_by_job_title",
          show: true,
        },
        addCustomer: {
          icon: "el-icon-user",
          title: "Case Status",
          path: "/case_status",
          show: true,
        },
        openOrder: {
          icon: "el-icon-shopping-cart-2",
          title: "Case Trends",
          path: "/trends",
          show: true,
        },
        openRepair: {
          icon: "el-icon-setting",
          title: "Worksite State",
          path: "/worksite_state",
          show: true,
        },
        viewReports: {
          icon: "el-icon-document",
          title: "View Reports",
          path: "/reports",
          show: false,
        },
        logout: {
          icon: "el-icon-s-custom",
          title: "Logout",
          path: "/",
          show: false,
        },
      },
    };
  },

  created() {
    // this.getTabList();
  },

  methods: {
    handleClick(name) {
      if (name === "logout") {
        localStorage.clear();
        this.$router.push("/");
        // equivalent: location.reload();
        this.$router.go(0);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
</style>

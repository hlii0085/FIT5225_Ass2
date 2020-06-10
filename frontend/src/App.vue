<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
    <!-- <HelloWorld msg="ABC" /> -->
    <!-- <UploadImg /> -->
    <!-- <Dashboard /> -->
    <router-view />
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
// import UploadImg from "./components/uploadImg/UploadImg.vue";
// import Dashboard from "./components/dashboard/Dashboard.vue";

export default {
  name: "App",
  components: {
    // HelloWorld,
    // UploadImg,
    // Dashboard,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<template>
  <div>
    <!-- <el-container
      ><el-header background-color: #333;>
        <img
          src="../../assets/logo.png"
          @click="toHome"
          :style="{ cursor: 'pointer' }"
        /> </el-header
    ></el-container> -->
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          router
        >
          <el-menu-item-group>
            <template slot="title">Options</template>
            <el-menu-item index="/home">Home</el-menu-item>
            <el-menu-item index="/uploadImg">Upload image</el-menu-item>
            <el-menu-item index="/query">Query</el-menu-item>
          </el-menu-item-group>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>check</el-dropdown-item>
              <el-dropdown-item>add</el-dropdown-item>
              <el-dropdown-item>delete</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>abc</span>
        </el-header>

        <el-main> <router-view></router-view></el-main>
      </el-container>
    </el-container>
  </div>
</template>
<style>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

.header {
  background-color: #333;
}
</style>

<script>
export default {};
</script>

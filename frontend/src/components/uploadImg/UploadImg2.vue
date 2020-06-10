<template>
  <div>
    <!-- <el-upload
      class="upload-demo"
      drag
      action="https://q7ums1jp8h.execute-api.us-east-1.amazonaws.com/v1/demo2"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :file-list="fileList"
      multiple
    >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
      </div>
      <div class="el-upload__tip" slot="tip">
        jpg/png files with a size less than 500kb
      </div>
    </el-upload> -->
    <!-- <p>
      <router-link to="../HelloWorld.vue">to HelloWorld</router-link>
    </p>
    <router-view></router-view> -->

    <el-upload
      class="upload-demo"
      drag
      action="https://vr9y6qyti0.execute-api.us-east-1.amazonaws.com/tag/upload-image"
      multiple
      :headers="headers"
    >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
      </div>
      <div class="el-upload__tip" slot="tip">
        jpg/png files with a size less than 500kb
      </div>
    </el-upload>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // dialogImageUrl: "",
      // dialogVisible: false,
      // disabled: false,
    };
  },
  computed: {
    headers() {
      return {
        "Content-Type": "image/jepg",
      };
    },
  },
  methods: {
    // handlePictureCardPreview(file) {
    //   this.dialogImageUrl = file.url;
    //   this.dialogVisible = true;
    // },
  },
};
</script>

<template>
  <div>
    <el-upload
      class="upload-demo"
      action="https://vr9y6qyti0.execute-api.us-east-1.amazonaws.com/tag/upload-image/"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :file-list="fileList"
      list-type="picture"
      :headers="headers"
      :http-request="beforeUpload"
    >
      <el-button size="small" type="primary">Click to upload</el-button>
      <div slot="tip" class="el-upload__tip">
        image files with a size less than 500kb
      </div>
    </el-upload>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fileList: [
        // {
        //   name: "food.jpeg",
        //   url:
        //     "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100",
        // },
        // {
        //   name: "food2.jpeg",
        //   url:
        //     "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100",
        // },
      ],
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
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    beforeUpload(file) {
      console.log(file);
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "image/jpeg");

      var requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: file,
        redirect: "follow",
      };

      fetch(
        "https://vr9y6qyti0.execute-api.us-east-1.amazonaws.com/tag/upload-image",
        requestOptions
      )
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.log("error", error));

      // var data = file;

      // var xhr = new XMLHttpRequest();
      // xhr.withCredentials = false;

      // xhr.addEventListener("readystatechange", function() {
      //   if (this.readyState === 4) {
      //     console.log(this.responseText);
      //   }
      // });

      // xhr.open(
      //   "POST",
      //   "https://vr9y6qyti0.execute-api.us-east-1.amazonaws.com/tag/upload-image"
      // );
      // xhr.setRequestHeader("Content-Type", "image/jpeg");

      // xhr.send(data);

      // return false;
    },
  },
};
</script>

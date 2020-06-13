<template>
  <div class="main">
    <el-form :model="tagForm" ref="tagForm" label-width="100px" class="form">
      <div class="inline-items">
        <el-form-item
          v-for="(tag, index) in tagForm.tags"
          :label="'Tag' + (index + 1)"
          :key="index"
          :inline="true"
          :rules="{
            required: true,
            message: 'Tag cannot be null',
            trigger: 'blur',
          }"
        >
          <el-input
            v-model="tagForm.tags[index]"
            placeholder="tags"
            style="width:150px; margin-right:5px"
            clearable
          ></el-input>
          <el-button
            @click.prevent="removeTag(index)"
            type="danger"
            size="medium"
            >Delete</el-button
          >
        </el-form-item>
      </div>
      <el-form-item>
        <el-button type="primary" @click="submitForm('tagForm')"
          >Submit</el-button
        >
        <el-button @click="addTag()">Add Tag</el-button>
      </el-form-item>
      <!-- <el-form-item>
        <el-input
          type="textarea"
          :rows="2"
          placeholder="请输入内容"
          v-model="text"
        >
        </el-input>
      </el-form-item> -->
    </el-form>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>Results</span>
      </div>
      {{ this.text }}
    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      tagForm: {
        tags: [""],
      },
      respData: {
        links: [
          "asb",
          "dsfdsfdsfdsfdsfsdfdsfdsfdskfjldksfjhdlsfhdfjhk.png",
          "fdsfdsfdsfsdfdsfdsfsdfdsfsdfdsfs",
        ],
      },
      text:
        "Submit tags to see the result. If you wanna send multiple tags, use Add Tag.",
    };
  },
  methods: {
    addTag() {
      //   console.log(this.tagForm);
      this.tagForm.tags.push("");
      console.log("push,", JSON.stringify(this.tagForm));
    },
    removeTag(index) {
      this.$delete(this.tagForm.tags, index);
      console.log("delete,", JSON.stringify(this.tagForm));
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert("submit!");
          console.log(JSON.stringify(this.tagForm));
          //   this.$axios
          //     .$post(
          //       "https://vr9y6qyti0.execute-api.us-east-1.amazonaws.com/api/query",
          //       JSON.stringify(this.tagForm)
          //     )
          //     .then((response) => {
          //       this.text = JSON.stringify(response);
          //     });
          var myHeaders = new Headers();
          myHeaders.append("Content-Type", "text/plain");

          var raw = JSON.stringify(this.tagForm);

          var requestOptions = {
            method: "POST",
            headers: myHeaders,
            body: raw,
            redirect: "follow",
          };

          fetch(
            "https://vr9y6qyti0.execute-api.us-east-1.amazonaws.com/api/query",
            requestOptions
          )
            .then((response) => response.text())
            .then((result) => (this.text = result))
            // .then(console.log("this.text:", this.text))
            // .then((response) => this.handleResponse(response))
            .catch((error) => console.log("error", error));

          //   this.text = JSON.stringify(this.respData);
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    handleResponse(resp) {
      console.log("result:", resp);
      this.text = resp;
      console.log("this.text:", this.text);
    },
  },
};
</script>

<style>
.main {
  display: flex;
  justify-content: center;
  /* flex-direction: column; */
}
.form {
}

.table {
  margin-left: 10px;
}

.box-card {
  width: 500px;
  margin-left: 100px;
}
</style>

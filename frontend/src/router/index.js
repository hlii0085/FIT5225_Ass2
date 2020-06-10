import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/home",
  },
  {
    path: "/dashboard",
    name: "dashboard",
    meta: {
      title: "Dashboard",
    },
    component: () => import("@/components/dashboard/Dashboard.vue"),
    children: [
      {
        path: "/home",
        name: "home",
        meta: {
          title: "Home",
        },
        component: () => import("@/components/home/Home.vue"),
      },
      {
        path: "/uploadImg",
        name: "uploadImg",
        meta: {
          title: "Upload Image",
        },
        component: () => import("@/components/uploadImg/UploadImg.vue"),
      },
      {
        path: "/query",
        name: "query",
        meta: {
          title: "Query",
        },
        component: () => import("@/components/query/Query.vue"),
      },
    ],
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title;
  }
  next();
});

export default router;

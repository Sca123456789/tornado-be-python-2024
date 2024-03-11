import axios from "axios";
import createAuthRefreshInterceptor from "axios-auth-refresh";

const axiosService = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
});
axiosService.interceptors.request.use(async (config)=>{
    const {access} = JSON.parse(localStorage.getItem("auth"));
    config.headers.Authorization = `Bearer ${access}`;
    return config;
});
axiosService.interceptors.response.use(
    (res) => Promise.resolve(res),
    (err) => Promise.reject(err),
);
const refreshAuthLogic = async (failedRequest) => {
    const { refresh } = JSON.parse(localStorage.getItem("auth"));
    try {
      const resp = await axios.post("/refresh/token/", null, {
        baseURL: "http://localhost:8000",
        headers: {
          Authorization: `Bearer ${refresh}`,
        },
      });
      const { access, refresh: newRefresh } = resp.data; // renaming 'refresh' variable as 'newRefresh' to avoid conflict
      failedRequest.response.config.headers["Authorization"] = `Bearer ${access}`;
      // Update localStorage with new tokens
      localStorage.setItem("auth", JSON.stringify({ access, refresh: newRefresh }));
    } catch (error) {
      // If refresh fails, remove authentication data from localStorage
      localStorage.removeItem("auth");
    }
  };
  createAuthRefreshInterceptor(axiosService, refreshAuthLogic);
  export function fetcher(url) {
    return axiosService.get(url).then((res) => res.data);
  }

  export default axiosService;
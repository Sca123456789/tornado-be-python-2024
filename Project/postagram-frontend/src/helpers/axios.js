import axios from "axios";
import createAuthRefreshInterceptor from "axios-auth-refresh";
import { getAccessToken, getRefreshToken } from "../hooks/user.actions"; // Import getAccessToken and getRefreshToken

const axiosService = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
});

axiosService.interceptors.request.use(async (config) => {
    const token = getAccessToken(); // Get the access token
    config.headers.Authorization = `Bearer ${token}`; // Set the Authorization header with the access token
    return config;
});

axiosService.interceptors.response.use(
    (res) => Promise.resolve(res),
    (err) => Promise.reject(err),
);

const refreshAuthLogic = async (failedRequest) => {
    const refreshToken = getRefreshToken(); // Get the refresh token from localStorage
    try {
        const resp = await axios.post("/refresh/token/", null, {
            baseURL: "http://localhost:8000",
            headers: {
                Authorization: `Bearer ${refreshToken}`, // Set the Authorization header with the refresh token
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

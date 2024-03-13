import axios from "axios";
import { useNavigate } from "react-router-dom";

function useUserActions() {
  const navigate = useNavigate();
  const baseURL = "http://localhost:8000/api";

  const login = async (data) => {
    try {
      const response = await axios.post(`${baseURL}/auth/login/`, data);
      setUserData(response.data);
      navigate("/");
    } catch (error) {
      // Handle login error
      if (error.message) {
        // Handle error message
        console.error(error.message);
      }
    }
  };

  const register = (data) => {
    // Implement registration logic
  };

  const logout = () => {
    localStorage.removeItem("auth");
    navigate("/login");
  };

  return { login, register, logout };
}

// Get the user access token
const getAccessToken = () => {
  const auth = JSON.parse(localStorage.getItem("auth"));
  return auth ? auth.access : null;
};

// Get the user
const getUser = () => {
  const auth = JSON.parse(localStorage.getItem("auth"));
  return auth ? auth.user : null;
};

// Get the user refresh token
const getRefreshToken = () => {
  const auth = JSON.parse(localStorage.getItem("auth"));
  return auth ? auth.refresh : null;
};

// Set the user data in local storage
const setUserData = (data) => {
  localStorage.setItem("auth", JSON.stringify({
    access: data.access,
    refresh: data.refresh,
    user: data.user,
  }));
};

export { useUserActions, setUserData, getAccessToken, getUser, getRefreshToken };

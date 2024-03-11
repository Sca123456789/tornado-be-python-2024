import React from "react";
import { Navigate } from "react-router-dom"; // Assuming you're using React Router

function ProtectedRoute({ children }) {
  const auth = JSON.parse(localStorage.getItem("auth")); // Corrected variable name from 'user' to 'auth'
  return auth ? (
    <>{children}</>
  ) : (
    <Navigate to="/login/" /> // Changed 'auth.account' to 'auth' to check if any authentication data exists
  );
}

export default ProtectedRoute;

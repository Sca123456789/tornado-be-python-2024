import React from "react";
import { Navigate } from "react-router-dom";
import { getUser } from "../hooks/user.actions";

function ProtectedRoute(children ) {
  const user = getUser(); // Use the getUser function to check if a user is authenticated
  return user ? (
    <>{children}</>
  ) : (
    <Navigate to="/login/" />
  );
}

export default ProtectedRoute;
// import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ProtectedRoute from "./routes/ProtectedRoute";
import Home from "./pages/Home";
import Registration from "./pages/Registration";
import Login from "./pages/Login";

function App() {
  return (
    <Router>
      <Routes>
        {/* Route for protected home page */}
        <Route
          path="/"
          element={
            // <ProtectedRoute>
              <Home />
            // {/* </ProtectedRoute> */}
          }
        />
        {/* Route for login page */}
        <Route path="/login/" element={<Login />} />
        {/* Route for registration page */}
        <Route path="/register/" element={<Registration />} />
      </Routes>
    </Router>
  );
}

export default App;


import logo from "./logo.svg";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./Pages/LoginPage/LoginPagejs";
import CEO from "./Pages/CEO";
import "./App.css";
import Dashboard from "./Pages/Dashboard/Dashboard";
import SignUp from "./Pages/SignUp /SignUp";

import { ChakraProvider } from "@chakra-ui/react";

function App() {
  return (
    <ChakraProvider>
      <Router>
        <div>
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/CEO-dashboard" element={<CEO />} />
          </Routes>
        </div>
      </Router>
    </ChakraProvider>
  );
}

export default App;

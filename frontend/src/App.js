import logo from "./logo.svg";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from './Pages/LoginPage/LoginPagejs';

import "./App.css";
import Dashboard from "./Pages/Dashboard/Dashboard";

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

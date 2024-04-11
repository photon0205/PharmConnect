// src/LoginPage.js
import React, { useState } from "react";
import "./LoginPage.css"; // Import CSS for styling
import { redirect } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import image from "../LoginPage/photo1.png";
import gimage from "../LoginPage/googleIcon.png";
export default function LoginPagejs() {
  const navigate=useNavigate();
  const [Username, SetUsername] = useState("");
  const [Password, SetPassword] = useState("");
  const [isLogedin, SetisLogedin] = useState(false); // merko yeh export krna hai
  const logindata = {
    username: Username,
    password: Password,
  };
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(logindata),
      });

      if (!response.ok) {
        throw new Error("Incorrect Username or Password");
      }

      //if response is fine
      SetisLogedin(true);
      navigate('/dashboard');


    } catch (error) {
      console.log(error);
    }
  };
  return (
    <div className="login-page">
      <div className="login-container">
        <img src={image} alt="Login" className="login-image" />

        <form onSubmit={handleLogin} className="login-form">
          <img src={image} alt="" className="image" />
          <h1>Login to Your account</h1>
          <p>Welcome back, Please enter your details</p>
          {/* <input type="text" placeholder="Username" /> */}
          <input
            type="text"
            placeholder="Username"
            value={Username}
            onChange={(e) => SetUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={Password}
            onChange={(e) => SetPassword(e.target.value)}
          />
          <a href="/forgot">Forgot Password</a>
          <button type="submit">Signin</button>
          <button type="submit" id="button1">
            <div className="google">
              <div className="image12"><img src={gimage} alt="Login" className="image12"/></div>
              <div className="p1"> <span>Sign in with google</span></div>
            </div>
            
          </button>
        </form>
      </div>
    </div>
  );
}

// page mai components dal ke page app.js mai daldu?

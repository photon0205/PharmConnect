// src/LoginPage.js
import React, { useState } from "react";
import "./SignUp.css"; // Import CSS for styling
import { redirect } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import image from "../LoginPage/photo1.png";
import gimage from "../LoginPage/googleIcon.png";
export default function SignUp() {
  const navigate=useNavigate();
  const [Username, SetUsername] = useState("");
  const [Password, SetPassword] = useState("");
  const [Name, SetName] = useState("");
  const [Address, SetAddress] = useState("");
  const [PinCode, SetPinCode] = useState("");
  const [Phone, SetPhone] = useState("");
  
  const signupndata = {
    Name:Name,
    Address:Address,
    PinCode: PinCode,
    Phone_Number: Phone,
    username: Username,
    password: Password,

  };
  const handleSignUp = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(signupndata),
      });

      if (!response.ok) {
        throw new Error("Failed");
      }

      //if response is fine
    //   SetisLogedin(true);
      navigate('/dashboard');


    } catch (error) {
      console.log(error);
    }
  };
  return (
    <div className="login-page">
      <div className="login-container">
        <img src={image} alt="Login" className="login-image" />

        <form onSubmit={handleSignUp} className="login-form">
          <img src={image} alt="" className="image" />
          <h1>User Registration</h1>
          {/* <p>Welcome back, Please enter your details</p> */}
          {/* <input type="text" placeholder="Username" value={Username}/> */}
          <input
            type="text"
            placeholder="Name"
            value={Name}
            onChange={(e) => SetName(e.target.value)}
          />
          <input
            type="text"
            placeholder="Address"
            value={Address}
            onChange={(e) => SetAddress(e.target.value)}
          />
          <input
            type="number"
            placeholder="Pin Code"
            value={PinCode}
            onChange={(e) => SetPinCode(e.target.value)}
          />
          
          <input
            type="number"
            placeholder="Phone_Number"
            value={Phone}
            onChange={(e) => SetPhone(e.target.value)}
          />
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
          {/* <a href="/forgot">Forgot Password</a> */}
          <button type="submit">SignUp</button>
          <button type="submit" id="button1">
            <div className="google">
              <div className="image12"><img src={gimage} alt="Login" className="image12"/></div>
              <div className="p1"> <span>Sign up with google</span></div>
            </div>
            
          </button>
        </form>
      </div>
    </div>
  );
}

// page mai components dal ke page app.js mai daldu?

// src/LoginPage.js
import React, { useState } from "react";
import {useNavigate} from "react-router-dom";
import image from "/Users/saiyamarora/Desktop/PharmConnect/frontend/src/Pages/LoginPage/photo1.png";
import './Choose.css'
import business from "/Users/saiyamarora/Desktop/PharmConnect/frontend/src/Vector.png";
import cust from "/Users/saiyamarora/Desktop/PharmConnect/frontend/src/Group 48096315.png";
// import { useNavigate } from "react-router-dom";




export default function Choose() {
  return (
    
    
    
    <div className="login-page12">
      <div className="login-container12">
        <img src={image} alt="Login" className="login-image12" />
      </div>
      
      <div className="selectrole">
        
        <div className="customer">
          
<button class="button12" >
  <img src={business} alt="Button Image"/>
  <h1> Business </h1>
  <p>Register as the CEO of the company</p>

</button>
        </div>
        <div className="ceo12">
        <button class="button12" >
  <img src={cust} alt="Button Image"/>
  <h1> Customer </h1>
  <p>Register as the Customer to buy products</p>

</button>
        </div>
      </div>
    </div>
  );
}

// page mai components dal ke page app.js mai daldu?

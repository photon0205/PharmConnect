import * as React from "react";

import img1 from "../Pages/LoginPage/photo1.png"

export default function Navbar() {
    const divStyle = {
        width:"35px"
      };
  return (
    <>
        
        
      <nav className="navbar navbar-expand-lg bg-body-tertiary my-2 border-bottom">
        <div className="container-fluid ">
          <a className="navbar-brand mx-2" href="#">
            <img src={img1} style={divStyle} alt="MediStock" />
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link active mx-2" aria-current="page" href="/about">
                  About
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link mx-2" href="/products">
                  Products
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link mx-2" href="/contact">
                  ContactUS
                </a>
              </li>
              
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
}

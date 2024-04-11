import Navbar from "../../components/Navbar";
import SearchBar from "../../components/SearchBar";
import BottomImage from "../../components/BottomImage";
// import Footer from "../../components/Footer"
import Foot from "../../components/Foot"
import Card from "../../components/Card";
import Ads from "../../components/Ads/Ads";
import React from 'react'

export default function Dashboard() {
  return (
    <div>
      <Navbar></Navbar>
      <SearchBar></SearchBar>
      <Ads></Ads>
      <BottomImage></BottomImage>
      <Card></Card>
      <Foot></Foot>


      


    </div>
  )
}

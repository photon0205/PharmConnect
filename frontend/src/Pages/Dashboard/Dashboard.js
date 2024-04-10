import Navbar from "../../components/Navbar";
import SearchBar from "../../components/SearchBar";
import Ads from "../../components/Ads/Ads";
import React from 'react'

export default function Dashboard() {
  return (
    <div>
      <Navbar></Navbar>
      <SearchBar></SearchBar>
      <Ads></Ads>

    </div>
  )
}

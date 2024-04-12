import React, { useState } from "react";
import "./SearchBar.css";
import sicon from "../assets/searchIcon.png";

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState("");

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onSearch(query);
  };

  return (
    <form className="search-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Search for medicines and wellness products"
        value={query}
        onChange={handleInputChange}
        className="search-input"
      />
      <button type="submit" className="search-button">
        <img src={sicon} alt="search" />
      </button>
      {/* <h4 className="deliver">Deliver to : {}</h4> */}
    </form>
  );
};

export default SearchBar;

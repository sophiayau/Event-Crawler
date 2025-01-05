import React from "react";
import "./styles/Header.css";
import spider from "./images/spider.png";
import bell from "./images/bell.svg";
import bellpng from "./images/bell.png";

function Header() {
  return (
    <nav className="bar">
      <div className="titleAndLogo">
        <img className="image" src={spider} alt="spider" />
        <h3 className="title">Event Crawler</h3>
      </div>
      <div>
        <img className="bell" src={bellpng} alt="bell" />
      </div>
    </nav>
  );
}

export default Header;

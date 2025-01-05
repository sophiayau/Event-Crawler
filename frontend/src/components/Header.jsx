import React from "react";
import "./styles/Header.css";
import spider from "./images/spider.png";

function Header() {
  return (
    <div>
      <div className="image">
        <img src={spider} />
      </div>
    </div>
  );
}

export default Header;

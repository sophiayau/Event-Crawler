import React from "react";
import "./styles/Header.css";
import spider from "./images/spider.png";
import bellpng from "./images/bell.png";

function Header() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  // const subscribePopUp = () => {
  //   // write functionality to display a subscription popup
  // }

  return (
    <nav className="bar">
      <div className="titleAndLogo" onClick={scrollToTop}>
        <img className="image" src={spider} alt="spider" />
        <h3 className="title">Event Crawler</h3>
      </div>
      <div>
        <img
          className="bell"
          src={bellpng}
          alt="bell"
          // onClick={subscribePopUp}
        />
      </div>
    </nav>
  );
}

export default Header;

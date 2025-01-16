import React, { useState } from "react";
import "./styles/CalendarContainer.css";
import Calendar from "react-calendar";
import SidePanel from "./SidePanel";

function CalendarContainer() {
  // recognizes and logs which date is being selected by user
  const handleDataChange = (date) => {
    console.log("Selected Date:", date);
  };

  return (
    <div className="calendar-container">
      <Calendar onChange={handleDataChange} />
      <SidePanel></SidePanel>
    </div>
  );
}

export default CalendarContainer;

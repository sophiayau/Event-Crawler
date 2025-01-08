import React from "react";
import "./styles/CalendarContainer.css";
import Calendar from "react-calendar";
import SidePanel from "./SidePanel";

function CalendarContainer() {
  return (
    <div className="calendar-container">
      <Calendar></Calendar>
      <SidePanel></SidePanel>
    </div>
  );
}

export default CalendarContainer;

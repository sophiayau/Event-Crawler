import React from "react";
import "./styles/EventItem.css";

function EventItem({ eventDate, eventName }) {
  return (
    // <div>
    <div className="item">
      <div className="event-date">
        <p>{eventDate}</p>
      </div>
      <div className="event-name">
        <p>{eventName}</p>
      </div>
    </div>
  );
}

export default EventItem;

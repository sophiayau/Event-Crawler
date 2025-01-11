import React from "react";
import "./styles/SidePanel.css";
import EventItem from "./EventItem.jsx";

function SidePanel() {
  return (
    <div className="SidePanelContainer">
      <div className="event-title">
        <h4>Upcoming Events</h4>
      </div>
      <EventItem
        eventDate={"Jan 11, 2025 @ 6pm"}
        eventName={"Group Leetcode Session"}
      ></EventItem>
      <EventItem
        eventDate="Jan 19, 2025 @ 5pm"
        eventName="Exploring Trends in AI"
      ></EventItem>
    </div>
  );
}

export default SidePanel;

// function SidePanel() {
//   const [eventData, setEventData] = useState([]);

//   useEffect(() => {
//     fetch("/event_info.json")
//       .then((response) => response.json())
//       .then((data) => setEventData(data))
//       .catch((error) => console.error("Error fetching events:", error)); // Log any errors that occur
//   }, []);

//   return (
//     <div className="SidePanelContainer">
//       <div className="event-title">
//         <h4>Upcoming Events</h4>
//       </div>
//       {eventData.map(
//         (
//           event,
//           index // Iterate over 'eventData' and render an EventItem for each event
//         ) => (
//           <EventItem
//             key={index} // Unique key for React's reconciliation algorithm
//             eventDate={event.eventDate} // Pass event date as a prop to EventItem
//             eventName={event.eventName} // Pass event name as a prop to EventItem
//           />
//         )
//       )}
//     </div>
//   );
// }

// export default SidePanel;

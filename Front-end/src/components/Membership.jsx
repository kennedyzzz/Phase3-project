import React, { useState, useEffect } from "react";
import Navbar from "./NavBar";
import "./css/membership.css"; 

function Membership() {
  const [memberships, setMemberships] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/membership")
      .then(response => response.json())
      .then(data => {
        setMemberships(data.memberships);
      })
      .catch(error => {
        console.error("There was an error fetching the memberships!", error);
      });
  }, []);

  const handlePurchase = (membershipId) => {
    console.log("Membership bought");
    const button = document.getElementById(`purchase-button-${membershipId}`);
    button.innerText = "Membership Purchased";
    button.style.backgroundColor = "#28a745";
    button.style.color = "#fff"; 
  };

  return (
    <div>
      <Navbar />
      <div className="main">
        {memberships.map(membership => (
          <div className="card" key={membership.id}>
            <img src={membership.image_url} alt={membership.name} className="card-img" />
            <h2>{membership.name}</h2>
            <p className="desc">{membership.description}</p>
            <p className="pri">Price: {membership.price}</p>
            <button id={`purchase-button-${membership.id}`} className="purchase-button" onClick={() => handlePurchase(membership.id)}>
              Purchase
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Membership;

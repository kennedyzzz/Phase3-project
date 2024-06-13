import React from "react";
import "./css/home.css";
import Navbar from "./NavBar";

function Home() {
  return (
    <div>
      <Navbar />
      <div className="home-container">
        <div className="home">
            <div className="content"> 
          <h2 className="title" >Za Gym</h2>
          <p className="home-text">
            We believe everyone should be able to enjoy a fit and healthy
            lifestyle. So we have made it simple, AFFORDABLE & convenient for
            you to achieve your personal health goals. Whether you want to lose
            weight, tone up, gain muscle or improve strength, we have a huge
            selection of equipment and FREE Fitness Classes to help you achieve
            your fitness goals. Our gyms are designed with you in mind — clean
            facilities, low-cost memberships and conveniently open from 5am to
            10pm every day. Join Smart Gyms today, where Every Body is welcome.
          </p>
        </div>
      </div>
    </div>
    </div>
  );
}

export default Home;

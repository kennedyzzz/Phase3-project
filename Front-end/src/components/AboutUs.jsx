import React from "react";
import Navbar from "./NavBar";
import "./css/aboutus.css";

function AboutUs() {
  return (
    <div className="About">
      <Navbar />
      <div class="container px-4 text-center">
        <div class="row gx-5">
          <div class="col">
            <div class="p-3">
              <img className="img"
                src="https://www.jengaleo.co.ke/wp-content/uploads/2022/05/Frame-94.jpg"
                alt=""
              />
            </div>
          </div>
          <div class="col">
            <div class="p-3">
              <p className="text-h">
                Our goal is simple - to promote healthy living with the right
                exercise and food schedule. The versatile team at Za Gym is
                well trained and experienced to recognize the needs of
                individual customers and are able to guide them accordingly. We
                guide our users every step of the way to help them transform
                their bodies.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AboutUs;

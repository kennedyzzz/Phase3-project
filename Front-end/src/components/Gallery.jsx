import React, { useState, useEffect } from "react";
import "./css/gallery.css"; 
import Navbar from "./NavBar";

function Gallery() {
  const [images, setImages] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/gallery")
      .then(response => response.json())
      .then(data => {
        setImages(data.images);
      })
      .catch(error => {
        console.error("There was an error fetching the images!", error);
      });
  }, []);

  return (
    <div>
      <Navbar/>
      <div className="gal">
        {images.map(image => (
          <div className="sub" key={image.id}>
            <img src={image.image_url} alt="Gallery" className="sub-img" />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Gallery;

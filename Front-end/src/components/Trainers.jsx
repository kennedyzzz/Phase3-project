import React, { useEffect, useState } from 'react';
import "./css/trainers.css"
import Navbar from './NavBar';

function Trainers() {
  const [trainers, setTrainers] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/trainers')
      .then((res) => res.json())
      .then((data) => setTrainers(data.trainers))
      .catch((error) => console.error('Error fetching trainers:', error));
  }, []);

  return (
    <div>
      <Navbar />
      <div className="container mt-4">
        <div className="row">
          {trainers.map((trainer) => (
            <div className="col-md-4 mb-4" key={trainer.id}>
              <div className="card h-100">
                <img src={trainer.image_url} className="card-img-top" alt={trainer.name} />
                <div className="card-body">
                  <h3 className="card-title">{trainer.name}</h3>
                  <p className="card-text">{trainer.description}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Trainers;

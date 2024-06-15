import { Link } from "react-router-dom";
import './css/navbar.css'

function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/home">Home</Link>
      <Link to="/membership">Membership</Link>
      <Link to="/gallery">Gallery</Link>
      <Link to="/trainers">Trainers</Link>
      <Link to="/about us">About us</Link>
    </nav>
  );
}

export default Navbar;
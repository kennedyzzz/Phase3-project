import { Link } from "react-router-dom";
import './css/navbar.css'

function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/">Home</Link>
      <Link to="/membership">Membership</Link>
      <Link to="/equipment">Equipment</Link>
      <Link to="/about us">About us</Link>
    </nav>
  );
}

export default Navbar;
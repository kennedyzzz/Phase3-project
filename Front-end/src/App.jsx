import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from './components/Home';
import Membership from './components/Membership';
import Gallery from './components/Gallery';
import AboutUs from './components/AboutUs';
import Trainers from './components/Trainers';

function App() {
    return (
        <BrowserRouter>
            <div>
                <Routes>
                    <Route path="/home" element={<Home />} />
                    <Route path="/membership" element={<Membership />} />
                    <Route path="/gallery" element={<Gallery />} />
                    <Route path="/trainers" element={<Trainers />} />
                    <Route path="/about us" element={<AboutUs />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;

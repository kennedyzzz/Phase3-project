import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from './components/Home';
import Membership from './components/Membership';
import Equipment from './components/Equipment';
import AboutUs from './components/AboutUs';

function App() {
    return (
        <BrowserRouter>
            <div>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/membership" element={<Membership />} />
                    <Route path="/equipment" element={<Equipment />} />
                    <Route path="/about us" element={<AboutUs />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;

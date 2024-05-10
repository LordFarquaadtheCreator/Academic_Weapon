import React from 'react';
import './Header.css';
import logo from '/assets/academicBEAST.webp'; 
function Header() {
    return (
        <header className="header">
            <img src={logo} alt="Logo" className="logo" /> 
            <h1>Academic Weapon</h1>
        </header>
    );
}

export default Header;

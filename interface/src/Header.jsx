import React from 'react';

import logo from '/images/academic_beast.png'; 
function Header() {
    return (
        <div className="flex flex-col items-center">
            <img src={logo} alt="Logo" className="logo" style={{width: 100, height: 100}}/> 
            <h1 className='text-colorfulOrange' text>Academic Weapon</h1>
        </div>
    );
}

export default Header;

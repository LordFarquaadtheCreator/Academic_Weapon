import React from 'react';

import logo from '/images/academic_beast.png'; 
function Header() {
    return (
        <div className='flex justify-between'>
            <div>
                <img src={logo} className="w-96" alt="Logo"/> 
            </div> 
            <div className='text-center inline-block align-middle p-8'>
                <h1 className='text-colorfulOrange text-7xl'>Academic</h1>
                <h1 className='text-colorfulOrange text-7xl'>Weapon</h1>
            </div>
        </div>
    );
}

export default Header;

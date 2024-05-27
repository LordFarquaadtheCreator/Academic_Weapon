import React from 'react';

import logo from '/images/academic_beast.png'; 
function Header() {
    return (
        <>
            <div className="flex justify-center">
                <img src={logo} className="w-96" alt="Logo"/> 
                <div className='text-center inline-block align-middle'>
                    <h1 className='text-colorfulOrange text-5xl'>Academic</h1>
                    <h1 className='text-colorfulOrange text-5xl'>Weapon</h1>
                </div>
            </div> 
        </>
    );
}

export default Header;

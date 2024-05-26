import React from 'react';
import Header from './Header';
import PromptInput from '../../interface/src/PromptInput';
import FileUpload from '../../interface/src/FileUpload';

function App() {
    /*still need to polish the UI*/
    /*
    Two things on backburner until UI is polished and the uploading is successfully sent to the backend :
    - make a mock nvbar with not much other stuff besides home which we land on and a link to the about page
    - websocket for streaming the text data back to the user
    
    
    */
    return (
      <div className='flex flex-col mx-auto bg-gradient-to-br from-colorfulDarkBlue from-10% to-colorfulLightBlue to-100%  w-full justify-center min-h-screen items-center space-x-4'>
        <Header />
        <div className='p-10 max-w-fit mx-auto rounded-xl border-colorfulYellow border-2 shadow-lg flex justify-center items-center space-x-4'> 
          <div className="m-2 p-6 w-fit mx-auto bg-sky-600 rounded-xl border-colorfulPink border-2 shadow-lg flex flex-col items-center space-x-4">
            <PromptInput />
          </div>
          <div>
            <FileUpload />
          </div>
        </div>
      </div>
    );
}

export default App;

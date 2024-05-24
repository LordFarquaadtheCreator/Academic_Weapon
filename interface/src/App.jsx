import React from 'react';
import Header from './Header';
import PromptInput from '../../interface/src/PromptInput';
import FileUpload from '../../interface/src/FileUpload';

function App() {
    return (
      <div className='flex flex-col w-full justify-center min-h-screen items-center space-x-4'>
        <Header />
        <div className='p-6 max-w-lg w-full mx-auto bg-white rounded-xl shadow-lg flex flex-col justify-center items-center space-x-4'> 
          <div className="p-6 m-2 max-w-lg w-fit mx-auto bg-sky-600 rounded-xl shadow-lg flex flex-col items-center space-x-4">
            <PromptInput />
          </div>
          <div className="p-6 max-w-lg w-fit mx-auto bg-white rounded-xl shadow-lg flex flex-col items-center space-x-4">
            File upload section
            <FileUpload />
          </div>
        </div>
      </div>
    );
}

export default App;

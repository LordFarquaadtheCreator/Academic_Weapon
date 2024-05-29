import React from 'react';
import Header from './Header';
import FileUpload from './FileUpload';
import PromptInput from './PromptInput';
import ResponseField from './ResponseField';
import './index.css'; // Ensure your custom CSS is imported

const App = () => {
  return (
    <div className="app-container flex flex-col min-h-screen bg-blue-900 text-antique-white">
      <Header />
      <div className="flex flex-grow">
        <div className="flex flex-col items-start p-8">
          {/* <div className="logo bg-black text-antique-white text-2xl p-4 mb-4">Logo</div> */}
        </div>
        <div className="flex-grow flex flex-col items-center justify-center p-8">
          <FileUpload />
        </div>
        <div className="flex flex-col items-end p-8">
          {/* <h1 className="text-4xl font-bold">Academic Weapon</h1> */}
        </div>
      </div>
      <div className="p-8">
        <PromptInput />
      </div>
      <div className="p-8">
        <ResponseField />
      </div>
    </div>
  );
};

export default App;

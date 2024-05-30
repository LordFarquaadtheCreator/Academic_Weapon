import React from 'react';
import Header from './Header';
import PromptInput from './PromptInput';
import './index.css'; // Ensure your custom CSS is imported

const App = () => {
  return (
    <div className="app-container flex flex-col min-h-screen bg-blue-900 text-antique-white">
      <Header />
      <div className="flex flex-grow"/>
      <div className="p-8">
        <PromptInput />
      </div>
    </div>
  );
};

export default App;

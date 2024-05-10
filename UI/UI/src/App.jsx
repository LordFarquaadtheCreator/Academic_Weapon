import React from 'react';
import Header from './Header';
import PromptInput from './PromptInput';
import FileUpload from './FileUpload';
import './App.css';

function App() {
    return (
        <div className="app">
            <Header />
            <PromptInput />
            <FileUpload />
        </div>
    );
}

export default App;

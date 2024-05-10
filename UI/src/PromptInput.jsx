import React, { useEffect, useState } from 'react';
import './PromptInput.css';
import axios from 'axios';

function PromptInput() {
    const [input, setInput] = useState('');

    const handleChange = (e) => {
        setInput(e.target.value);
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        axios.get("http://127.0.0.1:5000/query", {
            params: {
                query: input,
                context: 5
            }
        }).then((response) => {
            console.log(response.data)
        }).catch((error) => {
            console.log(error)
        })
    }

    return (
        <div className="prompt-input">
            <textarea id="userinput" onChange={handleChange} placeholder="Enter Prompt Here"></textarea>
            <button onClick={handleSubmit}>Submit</button>
        </div>
    );
}

export default PromptInput;

import React, { useEffect, useState } from 'react';
// import './PromptInput.css';
import axios from 'axios';
import ResponseField from './ResponseField';


function PromptInput() {
    const [input, setInput] = useState('');
    const [data, setData] = useState('');

    const handleChange = (e) => {
        setInput(e.target.value);
    }

    // const handleSubmit = (e) => {
    //     e.preventDefault();

    //     axios.get("http://127.0.0.1:5000/query", {
    //         params: {
    //             query: input,
    //             context: 5
    //         }
    //     }).then((response) => {
    //         console.log(response.data)
    //         setData(response.data)
    //     }).catch((error) => {
    //         console.log(error)
    //     })
    // }
    const handleSubmit = async () => {
        setData(input)
    }

    return (
        <div className='p-6 max-w-md mx-auto bg-white rounded-xl shadow-lg flex flex-col items-center space-x-4'>
            <div className="flex flex-col">
                <textarea id="userinput" onChange={handleChange} placeholder="Enter Prompt Here" style={{ height:'auto', maxHeight: 450}}></textarea>
                <button className='bg-sky-400 rounded-md' onClick={handleSubmit}>Submit</button>
            </div>
            {data ? <ResponseField responseData={data} /> : ""}
        </div>
    );
}

export default PromptInput;

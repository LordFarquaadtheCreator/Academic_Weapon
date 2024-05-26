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

    const handleSubmit = (e) => {
        // e.preventDefault();

        // axios.get("http://127.0.0.1:5000/query", {
        //     params: {
        //         query: input,
        //         content: 5
        //     }
        // }).then((response) => {
        //     console.log(response.data)
        //     setData(response.data)
        // }).catch((error) => {
        //     console.log(error)
        //     setData("There was an error fetching data from the server. Please try again later.")
        // })
        const connection = new WebSocket('wss://127.0.0.1:5000/')
        if (connection.readyState === 1) {
            console.log('successfull connection')
        }
        else{
            console.log(`There was an error connecting to the server, ready state responded with: ${connection.readyState}`)
        }
    }
    // const handleSubmit = async () => {
    //     setData(input)
    // }

    //it is highly likely that this would not be done since I have to make a websocket server... however we can try it out tomorrow
    

    return (
            <>
                <div class="flex items-center shadow-xl px-3 py-2 rounded-lg bg-perfectGrey">
                    <textarea 
                        onChange={handleChange} 
                        style={{width: 700, height: 55}} 
                        rows="1" 
                        className="resize rounded-md block mx-auto p-2.5 text-lg text-gray-900 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                        placeholder="Input your question here...">
                    </textarea>

                    <button className="inline-flex justify-center p-2 rounded-full cursor-pointer text-lg text-deepWhite hover:bg-mutedRed" onClick={handleSubmit}>
                        <svg className="w-5 h-5 rotate-90 rtl:-rotate-90" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                            <path d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"/>
                        </svg>
                    </button>
                </div>
                {data ? <ResponseField responseData={data} /> : ""}
            </>
    );
}

export default PromptInput;

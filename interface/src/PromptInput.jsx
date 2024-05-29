import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ResponseField from './ResponseField';


function PromptInput() {
    const [input, setInput] = useState('');
    const [data, setData] = useState('');
    const [loading, setLoading] = useState(false);
    const [submitingData, setSubmitingData] = useState(false);

    const handleChange = (e) => {
        setInput(e.target.value);
    }
    const handleSubmitClick = () => {
        console.log("Submit button clicked")
        setSubmitingData(prevState => !prevState);
    }


    useEffect(() => {
        /*https://axios-http.com/docs/res_schema*/
        if(input){ //don't fire for initial render
            axios.get("http://127.0.0.1:5000/query", {
                params: {
                    query: input,
                    content: 5
                }
            }).then((response) => {
                setData(response.data)
            }).catch((error) => {
                if(error.response){
                    setData(`Request passed successfully, however there was an error with the server and responded with status: ${error.response.status}`)
                }
                else if(error.request){
                    setData(`Request was made but no response was received. Error: ${error.message}`)
                }
                else{
                    setData(`There was an error, please try again later`)
                }
            })
        };

    }, [submitingData]);

    //it is highly likely that this would not be done since I have to make a websocket server... however we can try it out tomorrow
    // https://axios-http.com/docs/api_intro look into the streamed responseType

    return (
            <>
                <div className="flex items-center shadow-xl pr-2 pl-1 py-2 rounded-2xl bg-perfectGrey hover:animate">
                    <textarea 
                        onChange={handleChange} 
                        style={{width: 700, height: 55}} 
                        rows="2" 
                        className="resize rounded-md block mx-auto p-2.5 text-lg text-gray-500 rounded-lg border border-perfectGrey focus:ring-blue-500 focus:border-deepWhite bg-perfectGrey border-gray-600 placeholder-gray-300 text-white focus:ring-blue-500 focus:border-blue-500 outline-none" 
                        placeholder="Input your question here...">
                    </textarea>

                    <button className="inline-flex justify-center p-2 rounded-full cursor-pointer text-lg text-deepWhite hover:bg-mutedRed" onClick={handleSubmitClick}>
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

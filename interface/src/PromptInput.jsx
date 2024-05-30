import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ResponseField from './ResponseField';
import { io } from "socket.io-client";


function PromptInput() {
    const [input, setInput] = useState('');
    const [data, setData] = useState('');
    const [loading, setLoading] = useState(false); // for a possible loading animation
    const [submitingData, setSubmitingData] = useState(false);
    const [files, setFiles] = useState([]);
    const[fileName, setFileName] = useState([]);
    const [dragging, setDragging] = useState(false);

    const handleDragOver = (e) => {
        e.preventDefault();
        setDragging(true);
    };

    const handleDragLeave = (e) => {
        e.preventDefault();
        setDragging(false);
    };

    const handleDrop = (e) => {
        e.preventDefault();
        setDragging(false);
        console.log(e.dataTransfer.files[0])
        if (e.dataTransfer.files.length) {
            setFileName((existingFiles) => [...existingFiles, e.dataTransfer.files[0].name]);
            setFiles((existingFiles) => [...existingFiles, e.dataTransfer.files[0]]);
        }
    };
    const handleFileChange = (e) => {
        console.log(e.target.files[0]);
        if(e.target.files.length){
            setFileName((existingFiles) => [...existingFiles, e.target.files[0].name]);
            setFiles((existingFiles) => [...existingFiles, e.target.files[0]]);
        }
    };

    const removeFile = (file_name) => {
        console.log(file_name)
        const out = fileName.filter(file => file !== file_name)
        console.log(fileName.filter(file => file !== file_name))
        setFiles(out);
    };

    const handleInputChange = (e) => {
        setInput(e.target.value);
    }

    const handleSubmitClick = (e) => {
        const ws = new WebSocket('ws://127.0.0.1:5000/ws');
        setLoading(prevState => !prevState);
        setSubmitingData(prevState => !prevState);
        e.preventDefault();
        // if (ws.readyState === WebSocket.CONNECTING || ws.readyState === WebSocket.OPEN) {

        //     ws.onopen = () => { //currently only one item at a time is sent over the websocket
        //         console.log('Connected to the server');
        //         ws.send(input);
        //     };
        //     ws.onmessage = (event) => {
        //         setLoading(prevState => !prevState);
        //         console.log(event.data);
        //         setData(event.data);
        //         ws.close();
        //     };
        //     ws.onclose = () => {
        //         console.log('Disconnected from the server');
        //     };

            

        // }
        axios.post('http://127.0.0.1:5000/add_to_db', form)
        .then(res => {
            setInput('');
            setFiles([]);
            setFileName([]);
            setData(res.data)
            setLoading(prevState => !prevState);
        })
        .catch(err => {
            setLoading(prevState => !prevState);
            if(err.response){
                setData(`Request passed successfully, however, there was an error with the server and responded with status: ${err.response.status}`)
            }
            else if(err.request){
                setData(`Request was made but no response was received. Error: ${err.message}`)
            }
            else{
                setData(`There was an error, please try again later`)
            }
        });
        const socket = io("http://127.0.0.1:5000");


        socket.emit('message', input) // sending the data
        socket.on('message', (res) => { //listening
            setLoading(prevState => !prevState); //
            console.log(res);
            const streamedRes = [];
            streamedRes.push(res);
            setData(streamedRes.join(' '));
        });

        const form = new FormData();
        files.forEach(file => {
            form.append(`multi_files_${files.indexOf(file)}`, file);
        });
        form.append('inputBody', input); //add the input to the form data   
    }

    


    return (
            <>

                <div className=" justify-center p-8">
                    {data ? <ResponseField responseData={data} /> : ""}
                </div>
                <div className="justify-center flex p-8">
                    <form onSubmit={handleSubmitClick} method='post' encType='multipart/form-data' className='flex items-center justify-center'>
                        <div className="flex items-center shadow-xl pr-2 pl-1 py-2 rounded-2xl bg-perfectGrey hover:animate mr-4">
                            
                            <textarea 
                                onChange={handleInputChange} 
                                style={{width: 700, height: 55}} 
                                rows="2" 
                                className="resize rounded-md block mx-auto p-2.5 text-lg text-gray-500 rounded-lg border border-perfectGrey focus:ring-blue-500 focus:border-deepWhite bg-perfectGrey border-gray-600 placeholder-gray-300 text-white focus:ring-blue-500 focus:border-blue-500 outline-none" 
                                placeholder="Input your question here..."> 
                            </textarea>

                            <button type="submit" className="inline-flex justify-center p-2 rounded-full cursor-pointer text-lg text-deepWhite hover:bg-mutedRed">
                                {!loading?
                                    <svg className="w-5 h-5 rotate-90 rtl:-rotate-90" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                                        <path d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"/>
                                    </svg>
                                :   <svg className="animate-spin h-6 w-5 mr-3"  viewBox="0 0 24 24">
                                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="3"></circle>
                                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                    </svg>}
                            </button>
                        </div>

                        <label
                            htmlFor="dropzone-file"
                            className={`flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer 
                            ${dragging ? 'bg-gray-200' : 'bg-gray-50'} 
                            dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600`}
                            onDragOver={handleDragOver}
                            onDragLeave={handleDragLeave}
                            onDrop={handleDrop}
                            onChange={handleFileChange}
                        >
                            <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                <svg className="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                                <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                                </svg>
                                <p className="mb-2 text-sm text-gray-500 dark:text-gray-400"><span className="font-semibold">Click to upload</span> or drag and drop</p>
                                <p className="text-xs text-gray-500 dark:text-gray-400">TXT, PDF...</p>
                            </div>
                            <input id="dropzone-file" type="file" className="hidden" multiple/>
                        </label>
                        <div className="mr-2">
                            {fileName.map((file, index) => (
                                <div key={index}>
                                    {file}
                                    <button onClick={() => removeFile('env.txt')}>X</button>
                                </div>
                            ))}
                        </div>
                    </form>
                </div>
            </>
    );
}

export default PromptInput;

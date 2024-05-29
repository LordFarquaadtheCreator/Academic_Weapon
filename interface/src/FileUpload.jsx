import React, { useState } from 'react';
import axios from 'axios';

const url = 'http://localhost:5000';

function FileUpload() {
    const [files, setFiles] = useState([]);
    const[fileName, setFileName] = useState([]);
    const [dragging, setDragging] = useState(false);

    const handleDragOver = (e) => {
        e.preventDefault(); // Prevent default behavior
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
            setFileName((existingFiles) => [...existingFiles, e.dataTransfer.files[0].name]); //displays the file that was dropped
            setFiles((existingFiles) => [...existingFiles, e.dataTransfer.files[0]]);
        }
    };
    const handleFileChange = (e) => {
        console.log(e.target.files[0]);
        if(e.target.files.length){
            setFileName((existingFiles) => [...existingFiles, e.target.files[0].name]); //displays the file that was dropped
            setFiles((existingFiles) => [...existingFiles, e.target.files[0]]); //displays the file that was dropped
        }
    };

    const removeFile = (file_name) => {
        console.log(file_name)
        const out = fileName.filter(file => file !== file_name)
        console.log(fileName.filter(file => file !== file_name))
        setFiles(out);
    };

    //going to use the formData api for this which allows for a simple implementation that doesn't have to use the legacy form attribute from html for multipart/form data
    const handleFormSubmit = (e) => {
        //https://stackoverflow.com/questions/58381990/react-axios-multiple-files-upload
        e.preventDefault();
        const form = new FormData();
        files.forEach(file => {
            form.append(`multi_files_${files.indexOf(file)}`, file);
        });
        axios.post('http://127.0.0.1:5000/upload', form)
            .then(res => console.log(res.data))
            .catch(err => console.error(`There was an error ${err.message}`));
    }

    /* Needs a lot of work */
    /*TO Do:  send file payload to backend probably going to make another area for uploading files since this is quite bad*/
    /*test with postman for file uploads*/
    /*https://axios-http.com/docs/multipart */
    return (
            <div className="flex items-center justify-center flex flex-col w-full h-full">
                <form onSubmit={handleFormSubmit} method='post' encType='multipart/form-data' className='flex items-center flex-col'>
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
                    <button type='submit' className='bg-colorfulOrange border-4 border-darkBlue p-2 rounded-xl hover:bg-deepRed'>Submit</button>
                </form>
                
                <div className="uploaded-files">
                    {fileName.map((file, index) => (
                        <div key={index}>
                            {file}
                            <button onClick={() => removeFile('env.txt')} style={{ marginLeft: '10px' }}>X</button>
                        </div>
                    ))}
                </div>
            </div>
    );
}

export default FileUpload;

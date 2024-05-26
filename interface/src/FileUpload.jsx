import React, { useState } from 'react';

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
        if (e.dataTransfer.files.length) {
            console.log('Dropped file:', e.dataTransfer.files[0].name);
            setFileName((existingFiles) => [...existingFiles, e.dataTransfer.files[0].name]); //displays the file that was dropped
            setFiles((existingFiles) => [...existingFiles, e.originalEvent.dataTransfer]);
            //here we can handle the file upload
        }
    };
    const handleFileChange = (e) => {
        setFileName((existingFiles) => [...existingFiles, e.target.files[0].name]); //displays the file that was dropped
    };

    const removeFile = (file_name) => {
        console.log(file_name)
        const out = fileName.filter(file => file !== file_name)
        console.log(fileName.filter(file => file !== file_name))
        setFiles(out);
    };

    /* Needs a lot of work */
    /*TO Do:  send file payload to backend probably going to make another area for uploading files since this is quite bad*/
    return (
            <div className="flex items-center justify-center flex flex-col w-full h-full">
                {console.log(files[0])}
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
                        <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                        </svg>
                        <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                        <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
                    </div>
                    <input id="dropzone-file" type="file" className="hidden" />
                </label>
                <div id='payload' className="">
                    <button></button>
                </div>
                
                <div className="uploaded-files">
                    {console.log(fileName)}
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

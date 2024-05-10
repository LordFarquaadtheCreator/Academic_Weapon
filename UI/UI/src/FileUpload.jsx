import React, { useState } from 'react';
import './FileUpload.css';

function FileUpload() {
    const [files, setFiles] = useState([]);

    const handleFileChange = (event) => {
        setFiles([...files, ...event.target.files]);
    };

    const removeFile = (fileName) => {
        setFiles(files.filter(file => file.name !== fileName));
    };

    return (
        <div>
            <div className="file-upload">
                <input type="file" onChange={handleFileChange} style={{ width: '100%', height: '100%', opacity: 0 }} />
            </div>
            <div className="uploaded-files">
                {files.map((file, index) => (
                    <div key={index}>
                        {file.name}
                        <button onClick={() => removeFile(file.name)} style={{ marginLeft: '10px' }}>X</button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default FileUpload;

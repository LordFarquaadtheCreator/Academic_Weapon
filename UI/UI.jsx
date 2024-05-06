import React, { useState } from 'react';
import './App.css'; // This is where your styles.css content will be placed

const FileUploader = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      // You'll add your upload logic here
      console.log('File selected:', file.name);
    }
  };

  return (
    <div className="container my-5">
      <h1 className="text-center mb-4">Academic Weapon</h1>
      <div className="row">
        <div className="col-lg-5">
          <div className="logo-container mb-3">
            <img src="temp Academic Weapon logo.webp" alt="Logo" className="logo" /> {/* fahad edit this code please when you get the chance my lord */}
            <p>Ever wanted to study for a class but had limited resources? Just upload the resources and let our bot work its magic and make you additional study material!</p>
          </div>
          <textarea id="prompt-input" className="form-control" rows="8" placeholder="Enter your prompt and what class you want resources for!"></textarea>
        </div>
        <div className="col-lg-7">
          <div className="upload-container" onClick={() => document.getElementById('file-upload').click()}>
            <input type="file" id="file-upload" className="file-input" hidden accept="image/*,.pdf" onChange={handleFileChange} />
            <label htmlFor="file-upload" className="file-label d-flex justify-content-center align-items-center">
              <div className="upload-instructions">
                <span>Upload File Here</span>
                <span className="upload-icon">&#8613;</span>
              </div>
            </label>
            {selectedFile && <div className="file-details">File selected: {selectedFile.name}</div>}
          </div>
        </div>
      </div>
    </div>
  );
};

export default FileUploader;

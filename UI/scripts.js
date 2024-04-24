document.getElementById('file-upload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        // eventually this is where I'll Add the code to handle the file upload and send it to the databse.
        console.log('File selected:', file.name);
    }
});

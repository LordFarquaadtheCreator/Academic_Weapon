import { useState } from "react";
//here we want to stream the data from the backend to the frontend
// for the websocket we would need to change the server from using Quart for async ops to using Flask-SocketIO
// this is because quart does not support websockets

const ResponseField = () => {
  return (
    <div className="response-field bg-[#E3AFBC] text-[#5D001E] p-6 rounded-lg shadow-md my-4">
      <p>Response will be shown here.</p>
    </div>
  );
};

export default ResponseField;

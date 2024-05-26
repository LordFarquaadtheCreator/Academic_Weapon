import { useState } from "react";
//here we want to stream the data from the backend to the frontend
// for the websocket we would need to change the server from using Quart for async ops to using Flask-SocketIO
// this is because quart does not support websockets


const ResponseField = ({responseData}) => {

    return (
        <article className='flex flex-col p-6 w-6/12 mx-auto space-x-4 text-pretty text-deepWhite'>
            <h2 className="text-4xl">Response: </h2>
            <h3 className="text-xl">{responseData}</h3>
        </article>
    );
}

export default ResponseField;

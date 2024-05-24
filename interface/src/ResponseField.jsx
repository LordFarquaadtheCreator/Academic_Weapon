import { useState } from "react";
//here we want to stream the data from the backend to the frontend
// we have two possibilities: an SSE (server sent event) or a websocket
// the SSE is easier to implement and goes in one direction only from the server to the client
//on the other hand the websocket is bidirectional and can be used for more complex applications and goes from the 
//client to the server and vice versa

//for the SSE we could use the EventSource API https://developer.mozilla.org/en-US/docs/Web/API/EventSource
//for the websocket we could use the WebSocket API https://developer.mozilla.org/en-US/docs/Web/API/WebSocket

const ResponseField = ({responseData}) => {

    return (
        <article className='p-6 w-6/12 mx-auto flex items-center space-x-4 text-pretty'>
            <h3>{responseData}</h3>
        </article>
    );
}

export default ResponseField;

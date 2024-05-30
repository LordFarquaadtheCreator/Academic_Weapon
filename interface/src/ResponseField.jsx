import { useState } from "react";

const ResponseField = ({responseData}) => {
  return (
    <div className="bg-[#E3AFBC] text-[#5D001E] p-6 rounded-lg shadow-md my-4">
      <p>{responseData}</p>
    </div>
  );
};

export default ResponseField;

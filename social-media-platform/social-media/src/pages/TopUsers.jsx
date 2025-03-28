import { useState } from "react";

function App() {
  return (
    <>
      <div className="flex flex-col justify-center items-center h-dvh w-dvw">
        <button className="bg-black text-white h-20 w-100 mb-10">
          Top Users
        </button>
        <button className="bg-black text-white h-20 w-100 mb-10">
          Tranding Posts
        </button>
        <button className="bg-black text-white h-20 w-100 mb-10">Feeds</button>
      </div>
    </>
  );
}

export default App;

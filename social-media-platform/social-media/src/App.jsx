import { useState } from "react";
import { Link } from "react-router-dom";

function App() {
  return (
    <>
      <div className="flex flex-col justify-center items-center h-dvh w-dvw">
        <Link to="/top_user">
          <button className="bg-black text-white h-20 w-100 mb-10">
            Top Users
          </button>
        </Link>

        <button className="bg-black text-white h-20 w-100 mb-10">
          Tranding Posts
        </button>

        <button className="bg-black text-white h-20 w-100 mb-10">Feeds</button>
      </div>
    </>
  );
}

export default App;

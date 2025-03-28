import { useEffect } from "react";

function TopUser() {
  const fetchData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/users/");
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="flex flex-col justify-center items-center h-dvh w-dvw">
      <button className="bg-black text-white h-20 w-100 mb-10">
        Top Users
      </button>
    </div>
  );
}

export default TopUser;

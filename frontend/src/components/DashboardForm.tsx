import { useState } from "react";
import "./DashboardForm.css";
import axios from "axios";

export default function DashboardForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [hobbies, setHobbies] = useState("");

  const handleSubmit = async () => {
    let payload = {
      name,
      email,
      hobbies: hobbies
        .split(",")
        .map((h) => h.trim())
        .filter((el) => el),
    };
    console.log(payload.hobbies);
    //// check to see if provided inputs are valid and then send it to FASTAPI
    console.log("Submitting:", payload);
    //send to FASTAPI using axios
    try {
      const response = await axios.post("http://127.0.0.1:8000/person", {
        name: payload.name,
        email: payload.email,
        hobbies: payload.hobbies,
      });
      console.log(response);
    } catch (error) {
      console.error(error);
    }
    alert("Submitted! Check console for data.");
  };

  return (
    <div className="dashboard-container">
      <h2>User Playground</h2>

      <input
        type="text"
        placeholder="Enter Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <input
        type="email"
        placeholder="Enter Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="text"
        placeholder="Enter Hobbies (comma separated)"
        value={hobbies}
        onChange={(e) => setHobbies(e.target.value)}
      />

      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./routes/HomeDoc";
import Patient from "./routes/HomePaciente";
import Login from "./routes/Login";

function App() {
  return (
        <Routes>
          <Route path="/" element={<Login/>} />
          <Route path="/doctor" element={<Home/>} />
          <Route path="/patient" element={<Patient/>} />

          
        </Routes>
      
      
  );
}

export default App;


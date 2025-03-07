import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DoctorPage from "./routes/loginDoc";
import PatientPage from "./routes/loginPaciente"
import Home from "./routes/Home";

function App() {
  return (
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/doctor" element={<DoctorPage />} />
          <Route path="/patient" element={<PatientPage />} />
      </Routes>
  );
}

export default App;


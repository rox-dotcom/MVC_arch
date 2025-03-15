import React from "react";
import { useState } from "react";
import '../Styles/viewPatient.css'
import { getUser, agendarCita } from "../../backend_connection";

function AppointForm(){

    const [formData, setFormData] = useState({
        date: "",
        time: "",
        reason: "",
        doctorEmail: "",
        patientEmail: "",
      });
    
    const generateTimeSlots = (startHour, endHour, intervalMinutes) => {
    const slots = [];
    for (let hour = startHour; hour < endHour; hour++) {
        for (let minute = 0; minute < 60; minute += intervalMinutes) {
        const formattedHour = hour.toString().padStart(2, "0");
        const formattedMinute = minute.toString().padStart(2, "0");
        slots.push(`${formattedHour}:${formattedMinute}`);
        }
    }
    return slots;
    };

    const timeSlots = generateTimeSlots(8, 17, 30);

    const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!formData.date || !formData.time || !formData.reason || !formData.doctorEmail) {
          alert("Please fill in all fields.");
          return;
        }

        const citaData = {
          hora: formData.time,
          estado: "pendiente", // Default status
          correo_medico: formData.doctorEmail,
          correo_paciente: formData.patientEmail, // Should be fetched dynamically from auth
        };
    
        try {
          const result = await agendarCita(citaData);
          if (result) {
            alert("Appointment scheduled successfully!");
            setFormData({ date: "", time: "", reason: "", doctorEmail: "", patientEmail: "" });
          } else {
            alert("Failed to schedule appointment.");
          }
        } catch (error) {
          console.error("Error scheduling appointment:", error.response?.data || error.message);
          alert("Error connecting to the server.");
        }
      
    
  };


    return(
        <>
        <div className="appointment-form">
        <h2>Schedule an Appointment</h2>
        <form onSubmit={handleSubmit}>
          <label>Date:</label>
          <input type="date" name="date" value={formData.date} onChange={handleChange} required />

          <label>Time:</label>
          <select name="time" value={formData.time} onChange={handleChange} required>
            <option value="">Select a time</option>
            {timeSlots.map((slot) => (
              <option key={slot} value={slot}>
                {slot}
              </option>
            ))}
          </select>


          <label>Reason:</label>
          <input type="text" name="reason" value={formData.reason} onChange={handleChange} required />

          <label>Choose your doctor: </label>


          <button type="submit">Schedule</button>
        </form>
      </div>
        </>
    )

}

export default AppointForm;
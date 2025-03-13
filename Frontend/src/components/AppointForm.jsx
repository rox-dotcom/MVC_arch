import React from "react";
import { useState } from "react";
import '../Styles/viewPatient.css'

function AppointForm(){

    const [formData, setFormData] = useState({
        date: "",
        time: "",
        reason: "",
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

    const handleSubmit = (e) => {
        e.preventDefault();
        if (formData.date && formData.time && formData.reason) {
          setAppointments([...appointments, { id: appointments.length + 1, ...formData }]);
          setFormData({ date: "", time: "", reason: "" });
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

          <button type="submit">Schedule</button>
        </form>
      </div>
        </>
    )

}

export default AppointForm;
import React from "react";
import "../Styles/patientsList.css"; // Import external CSS

const PatientList = () => {
  const patients = [
    { id: 1, name: "John Doe", age: 45, condition: "Diabetes" },
    { id: 2, name: "Jane Smith", age: 37, condition: "Hypertension" },
    { id: 3, name: "Robert Brown", age: 29, condition: "Asthma" },
  ];

  return (  
    <div className="patient-container">
      <h2 className="title">Patient List</h2>
      <ul className="patient-list">
        {patients.map((patient) => (
          <li key={patient.id} className="patient-item">
            <div className="patient-info">
              <p className="patient-name">{patient.name}</p>
              <p className="patient-details">
                Age: {patient.age} | Condition: {patient.condition}
              </p>
            </div>
            <button className="view-button">View Details</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PatientList;

import React, { useState } from "react";
import { getUser } from "../../backend_connection";
import { useNavigate } from "react-router-dom";


function Form(){
    
    const navigate = useNavigate()
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    async function handleLogin(){
        if(!email || !password){
            alert("Complete all fields");
            return;
        }

        try {
            const data = await getUser(email);
            console.log(data)
            if (data.password === password) {
                console.log("Login successful");
                if(data.role === 'paciente' || 'patient'){
                    navigate('/patient')
                }
                if(data.role === 'doctor' ||'medico'){
                    navigate('/doctor')
                }

            } else {
            alert("Invalid password");
            }
        } catch (error) {
            alert("Error connecting to the server");
        }
        
        

    };
    

    return(
        <>
        <div>
            <input
            type="text"
            placeholder="Correo"
            className="text-holder"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            />
        </div>
        <div>
            <input
            type="password"
            placeholder="Contraseña"
            className="text-holder"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            />
        </div>
        <div className="button-container">
            <button onClick={handleLogin} >Login</button>
        </div>
        
        
        </>
    )
}

export default Form;
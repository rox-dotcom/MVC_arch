import React from "react";
import { useNavigate } from "react-router-dom";

function Button({name, route}){
    const navigate = useNavigate();
    
    return(
        < >
        <button
        className="button"
        onClick={() => navigate(route)}
             >

            {name} </button>
        </>
    )

}

export default Button
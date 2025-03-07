import React from "react";
import Form from '../components/Form'
import '../App.css'
import Button from "../components/Button";

function Doctor(){

    return(
        <>
        <div className="container">
            <h1  className="text">Doctor</h1>
            <Form/>
            <Button name="Log in" />

            <a href="/" className="text"> Regresar </a>
        </div>

        </>
    )
}

export default Doctor
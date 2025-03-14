import React  from 'react'
import '../App.css'
import  Form  from '../components/Form'
import logo from '../assets/img/medicinaLogo.png'


function Login() {
  

  return (
    <>
      
      <div className='container'>
        <img src={logo} className='image-format'/>
        <h2 className='text'>Bienvenido a CheckMed</h2>
        <div >
            <Form/> 
        </div>
        

      </div>
  
      
    </>
  )
}

export default Login

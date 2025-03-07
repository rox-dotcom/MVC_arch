import React  from 'react'
import Button from '../components/Button'
import '../App.css'


function Home() {
  

  return (
    <>
      
      <div className='container'>
        <h2 className='text'>Bienvenido a CheckMed</h2>
        <h3 className='text'>Selecciona una opción</h3>
        
        <div className='button-container'>
            <Button name="Doctor" route="/doctor" />
            <Button name="Paciente" route="/patient" />
        </div>

      </div>
  
      
    </>
  )
}

export default Home

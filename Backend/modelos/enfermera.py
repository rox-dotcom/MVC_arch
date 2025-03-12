from modelos.usuario import Usuario

class Enfermera(Usuario):
    def __init__(self, nombre, role, correo):
        super().__init__(nombre, role, correo)
    
    def actualizarCita(self):
        print("Actualizando cita")
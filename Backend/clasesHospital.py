class Usuario:
    
    def __init__(self, nombre, role, correo):
        self.nombre = nombre
        self.role = role
        self.password = "1234"
        self.correo = correo
        
    def show_info(self):
        print(f"Nombre: {self.nombre}, Role: {self.role}")
        
    def get_name(self):
        return self.nombre
        
class Administrador(Usuario):
    
    def __init__(self, nombre, role):
        super().__init__(nombre, role)
        
    def gestionar_citas(self, medico):
        op = int(print("¿Qué desea hacer?\n(1) Ver citas\n(2) Borrar cita\n(3) Modificar cita\n"))
        
        if op == 1:
            medico.revisarCitas()
            
        elif op == 2:
            index = int(input("Que cita desea borrar?"))
            medico.citasMedico.delete(index - 1)
            
        elif op == 3:
            index = int(input("Que cita desea modificar?"))
            print("Cita a modificar:")
            medico.citasMedico[index - 1].show_info()
            medico.citasMedico[index - 1].estado = "Pendiente" if (medico.citasMedico[index - 1].estado == "Confirmada")  else "Confirmada"
        
    def gestionar_horarios(self, medico):
        op = int(print("¿Qué desea hacer?\n(1) Ver citas\n(2) Borrar cita\n(3) Modificar horario\n"))
        
        if op == 1:
            medico.revisarCitas()
            
        elif op == 2:
            index = int(input("Que cita desea borrar?"))
            medico.citasMedico.delete(index - 1)
            
        elif op == 3:
            index = int(input("Que cita desea modificar?"))
            print("Cita a modificar:")
            medico.citasMedico[index - 1].show_info()
            horario = input("Nuevo horario: ")
            medico.citasMedico[index - 1].horario = horario
        
    def ver_citas(self):
        print("Viendo citas")
        
class Enfermera(Usuario):
    
    def __init__(self, nombre, role):
        super().__init__(nombre, role)
        self.signosVitales = []
        
    def actualizarCita(self):
        print("Actualizando cita")
        
    def registrarSV(self, paciente):
        print("Registrando signos vitales de " + paciente.get_name())
        
    def asistirMedico(medico):
        print("Asistiendo al médico: " + medico)
        
class Medico(Usuario):
    
    def __init__(self, nombre, role):
        super().__init__(nombre, role)
        self.citasMedico = []
        
    def revisarCitas(self):
        print("Revisando citas de Dr. " + self.get_name())
        
        print("\tLista de citas previas")
        for index, cita in enumerate(self.citasMedico):
            if cita.get_estado() == "Confirmada":
                print(f"Cita {index + 1}:")
                cita.show_info()
                
        for index, cita in enumerate(self.citasMedico):
            if cita.get_estado() == "Pendiente":
                self.actualizarEstadosCitas(cita)
                
        print("\tLista de citas actualizada")
        for index, cita in enumerate(self.citasMedico):
            if cita.get_estado() == "Confirmada":
                print(f"Cita {index + 1}:")
                cita.show_info()
            
    
    def actualizarEstadosCitas(self, cita):
        print("Cita pendiente de " + cita.get_paciente() + " a las " + cita.hora)
        
        op = int(input("(1) Aceptar cita\n(2) Rechazar cita\n"))
        
        if op == 1:
            cita.estado = "Confirmada"
            print("Cita confirmada")
        else:
            cita.estado = "Rechazada"
       



class Usuario:
    
    def __init__(self, nombre, role):
        self.nombre = nombre
        self.role = role
        self.signosVitales = []
        
    def show_info(self):
        print(f"Nombre: {self.nombre}, Role: {self.role}")
        
    
        
    def get_name(self):
        return self.nombre
    
    def get_signosVitales(self):
        return self.signosVitales
        
class Administrador(Usuario):
    
    def __init__(self, nombre, role):
        super().__init__(nombre, role)
        
    def gestionar_citas(self):
        print("Gestionando citas")
        
    def gestionar_horarios(self):
        print("Gestionando horarios")
        
    def ver_citas(self):
        print("Viendo citas")
        
class Enfermera(Usuario):
    
    def __init__(self, nombre, role):
        super().__init__(nombre, role)
        
    def actualizarCita(self):
        print("Actualizando cita")
        
    def registrarSV(self, paciente):
        print("Registrando signos vitales de " + paciente.get_name())
        paciente.signosVitales = ["Pulso: 80", "Temperatura: 36.5", "Presión: 120/80", self.get_name()]
        
    def asistirMedico(medico):
        print("Asistiendo al médico: " + medico)
        
class Medico(Usuario):
    
    
    def __init__(self, nombre, role):
        super().__init__(nombre, role)
        self.citasMedico = []
        
        
    def revisarCitas(self):
        print("Revisando citas de Dr. " + self.get_name())
        
        print("\tLista de citas previas")
        for cita in self.citasMedico:
            if cita.get_estado() == "Confirmada":
                cita.show_info()    
                
        for cita in self.citasMedico:
            if cita.get_estado() == "Pendiente":
                self.actualizarEstadosCitas(cita)
                
        print("\tLista de citas actualizada")
        for cita in self.citasMedico:
            if cita.get_estado() == "Confirmada":
                cita.show_info()   
            
    
    def actualizarEstadosCitas(self, cita):
        print("Cita pendiente de " + cita.get_paciente())
        
        op = int(input("(1) Aceptar cita\n(2) Rechazar cita\n"))
        
        if op == 1:
            cita.estado = "Confirmada"
            print("Cita confirmada")
        else:
            cita.estado = "Rechazada"
            print("Cita rechazada")
        
        
    def anadirCita(self, cita):
        self.citasMedico.append(cita)
        
        
class Paciente(Usuario):
    
    def __init__(self, nombre, role):
        super().__init__(nombre, role)
        
    def agendarCita(self, medico):
        print("Agendando cita con doctor: " + medico.get_name())
        
        cita = Cita(self.nombre, "12/12/2021", "10:00", "Pendiente", "Consulta general", medico)
        self.citasPaciente = cita
        medico.anadirCita(cita)
        
    def verEstadoDeCita(self):
        print("Viendo estado de la cita de " + self.get_name())
        print(self.citasPaciente.estado)
        
    def show_SV(self):
        print(f"Signos vitales de {self.nombre}: {", ".join(self.signosVitales)}")
        
class Cita:
    
    def __init__(self, paciente, fecha, hora, estado, motivo, medico):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.estado = estado 
        self.motivo = motivo
        self.medico = medico
        
    def show_info(self):
        print(f"Fecha: {self.fecha}, Hora: {self.hora}, Estado: {self.estado}, Motivo: {self.motivo}, Médico: {self.medico.get_name()}")
        
    def get_estado(self):
        return self.estado
    
    def get_paciente(self):
        return self.paciente
        
    
medico1 = Medico("Juan", "Medico")
paciente1 = Paciente("Pedro", "Paciente")
enfermera1 = Enfermera("Maria", "Enfermera")
admin1 = Administrador("Ana", "Administrador")

doctores = []
citas = []
pacientes = []
enfermeras = []

print("INFO FROM USERS")
print("_"*30)

medico1.show_info()
doctores.append(medico1)

paciente1.show_info()
pacientes

enfermera1.show_info()
enfermeras

admin1.show_info()


print("_"*30)
print("\n"*3)
print("AGENDAR CITA DE " + paciente1.get_name())
print("_"*30)



paciente1.agendarCita(medico1)
print("_"*30)
print("\n"*3)
print("REVISAR CITAS")
print("_"*30)

medico1.revisarCitas()
print("_"*30)
print("\n"*3)

print("VER ESTADO DE CITA")
print("_"*30)
paciente1.verEstadoDeCita()
print("_"*30)
print("\n"*3)

print("REPORTAR SIGNOS VITALES")
print("_"*30)
enfermera1.registrarSV(paciente1)
print("_"*30)
print("\n"*3)

print("MOSTRAR SIGNOS VITALES")
print("_"*30)
paciente1.show_SV()
print("_"*30)
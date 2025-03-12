class Usuario:
    
    def __init__(self, nombre, role, correo):
        self.nombre = nombre
        self.role = role
        self.password = "1234"
        self.correo = correo
        self.signos_vitales = []  # Lista de signos vitales para los pacientes
        self.citas = []  # Lista de citas para los pacientes
    
    def show_info(self):
        print(f"Nombre: {self.nombre}, Role: {self.role}, Correo: {self.correo}")
        
    def get_name(self):
        return self.nombre

    def agregar_signos_vitales(self, signos):
        self.signos_vitales.append(signos)
        
    def agregar_cita(self, cita_id):
        self.citas.append(cita_id)

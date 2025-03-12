from modelos.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, role, correo):
        super().__init__(nombre, role, correo)
    
    def ver_citas(self):
        print("Viendo citas")
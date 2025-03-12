from dao.conexion_firebase import ConexionFirebase

class UsuarioDAO:
    def __init__(self):
        self.db = ConexionFirebase().get_db()

    def agregar_usuario(self, usuario):
        usuario_ref = self.db.collection("usuarios").document(usuario.correo)
        usuario_ref.set({
            "nombre": usuario.nombre,
            "role": usuario.role,
            "correo": usuario.correo,
            "password": usuario.password,
            "signos_vitales": usuario.signos_vitales,
            "citas": usuario.citas  # Lista de referencias a citas
        })
        print("Usuario agregado correctamente")
    
    def obtener_usuario(self, correo):
        usuario_ref = self.db.collection("usuarios").document(correo)
        usuario = usuario_ref.get()
        if usuario.exists:
            return usuario.to_dict()
        return None
    
    def actualizar_usuario(self, correo, datos_actualizados):
        usuario_ref = self.db.collection("usuarios").document(correo)
        usuario_ref.update(datos_actualizados)
        print("Usuario actualizado correctamente")
    
    def eliminar_usuario(self, correo):
        usuario_ref = self.db.collection("usuarios").document(correo)
        usuario_ref.delete()
        print("Usuario eliminado correctamente")


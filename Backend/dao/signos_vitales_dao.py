from dao.conexion_firebase import ConexionFirebase
from google.cloud import firestore

class SignosVitalesDAO:
    
    def __init__(self):
        self.db = ConexionFirebase().get_db()

    def agregar_signos_vitales(self, correo_paciente, signos_vitales):
        paciente_ref = self.db.collection("usuarios").document(correo_paciente)
        paciente_ref.update({
            "signos_vitales": firestore.ArrayUnion([signos_vitales])  # Agrega los signos vitales a la lista
        })
        print(f"Signos vitales agregados a {correo_paciente} correctamente")

    def obtener_signos_vitales(self, correo_paciente):
        paciente_ref = self.db.collection("usuarios").document(correo_paciente)
        paciente = paciente_ref.get()
        if paciente.exists:
            return paciente.to_dict().get("signos_vitales", [])
        return None

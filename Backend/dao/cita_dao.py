from dao.conexion_firebase import ConexionFirebase
from google.cloud import firestore
import uuid

class CitaDAO:
    def __init__(self):
        self.db = ConexionFirebase().get_db()

    def agregar_cita(self, cita, correo_medico, correo_paciente):
        # Generar un ID único para la cita
        cita_id = str(uuid.uuid4())

        # Verificar si el médico existe y tiene el rol adecuado
        medico_ref = self.db.collection("usuarios").document(correo_medico)
        medico_doc = medico_ref.get()

        if medico_doc.exists and medico_doc.to_dict().get("role") == "medico":
            # Agregar la cita en la colección "citas"
            cita_data = {
                "paciente": correo_paciente,
                "hora": cita.hora,
                "estado": cita.estado,
                "medico": correo_medico  # Asociamos el correo del médico a la cita
            }
            citas_ref = self.db.collection("citas")
            citas_ref.document(cita_id).set(cita_data)

            # Agregar el ID de la cita al médico
            medico_ref.update({
                "citas": firestore.ArrayUnion([cita_id])  # Guardamos el ID de la cita como string
            })
            print(f"Cita asignada al médico {correo_medico}.")
        else:
            print(f"No se encontró al médico con correo {correo_medico} o no tiene rol de 'medico'.")

        # Verificar si el paciente existe
        paciente_ref = self.db.collection("usuarios").document(correo_paciente)
        paciente_doc = paciente_ref.get()

        if paciente_doc.exists:
            # Agregar el ID de la cita al paciente
            paciente_ref.update({
                "citas": firestore.ArrayUnion([cita_id])  # Guardamos el ID de la cita como string
            })
            print(f"Cita asignada al paciente {correo_paciente}.")
        else:
            print(f"No se encontró al paciente con correo {correo_paciente}.")
        
        print("Cita agregada correctamente.")

    def obtener_citas(self, correo_medico):
        # Obtener las citas del médico especificado desde la colección "citas"
        medico_ref = self.db.collection("usuarios").document(correo_medico)
        medico_doc = medico_ref.get()

        if medico_doc.exists and medico_doc.to_dict().get("role") == "medico":
            # Obtener las citas de la colección "citas"
            citas_ref = self.db.collection("citas").where("medico", "==", correo_medico)
            citas = citas_ref.stream()

            # Retornar las citas como una lista de diccionarios
            citas_list = []
            for cita in citas:
                cita_data = cita.to_dict()
                cita_data["id"] = cita.id  # Agregar el ID de la cita
                citas_list.append(cita_data)

            return citas_list
        else:
            print(f"No se encontró al médico con correo {correo_medico} o no tiene rol de 'medico'.")
            return []

    def obtener_cita_por_id(self, cita_id):
        if cita_id is None:
            print("Error: ID de cita no válido.")
            return None
        
        cita_ref = self.db.collection("citas").document(cita_id)
        cita = cita_ref.get()
        if cita.exists:
            return cita.to_dict()
        else:
            return None


    def actualizar_cita(self, cita_id, nuevos_datos):
        # Buscar la cita en la colección "citas"
        cita_ref = self.db.collection("citas").document(cita_id)
        cita_doc = cita_ref.get()

        if cita_doc.exists:
            # Actualizar los datos de la cita con los nuevos valores
            cita_ref.update(nuevos_datos)
            print(f"Cita con ID {cita_id} actualizada correctamente.")
        else:
            print(f"No se encontró la cita con ID {cita_id}.")

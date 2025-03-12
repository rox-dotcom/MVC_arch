from dao.usuario_dao import UsuarioDAO
from dao.cita_dao import CitaDAO
from dao.signos_vitales_dao import SignosVitalesDAO
from modelos.usuario import Usuario
from modelos.cita import Cita

# Crear instancias de los DAO
usuario_dao = UsuarioDAO()
cita_dao = CitaDAO()
signos_vitales_dao = SignosVitalesDAO()

# Crear un paciente y agregarlo
paciente = Usuario(nombre="Carlos López", role="paciente", correo="carlos@email.com")
usuario_dao.agregar_usuario(paciente)

# Crear un médico y agregarlo
medico = Usuario(nombre="Juan Pérez", role="medico", correo="juanperez@email.com")
usuario_dao.agregar_usuario(medico)

# Crear una cita
cita1 = Cita(paciente="Carlos López", hora="10:00 AM", estado="Pendiente")
cita_id = cita_dao.agregar_cita(cita1, correo_medico="juanperez@email.com", correo_paciente="carlos@email.com")

# Agregar signos vitales al paciente
signos = {"presion": "120/80", "frecuencia": "72", "temperatura": "36.5"}
signos_vitales_dao.agregar_signos_vitales("carlos@email.com", signos)

# Ver signos vitales de un paciente
signos_vitales = signos_vitales_dao.obtener_signos_vitales("carlos@email.com")
print("Signos vitales de Carlos:", signos_vitales)

# Obtener las citas del médico
citas_medico = cita_dao.obtener_citas("juanperez@email.com")
print("Citas del médico Juan Pérez:", citas_medico)

# Obtener una cita por su ID
cita_details = cita_dao.obtener_cita_por_id(cita_id)
print("Detalles de la cita:", cita_details)

# Actualizar la cita
nuevos_datos = {"hora": "11:00 AM", "estado": "Confirmada"}
cita_dao.actualizar_cita(cita_id, nuevos_datos)

# Verificación: Obtener la cita actualizada
cita_actualizada = cita_dao.obtener_cita_por_id(cita_id)
print("Cita actualizada:", cita_actualizada)

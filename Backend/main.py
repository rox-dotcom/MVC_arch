from flask import Flask, request, jsonify
from flask_cors import CORS
from dao.usuario_dao import UsuarioDAO
from modelos.usuario import Usuario
from modelos.cita import Cita
from dao.cita_dao import CitaDAO

app = Flask(__name__)
CORS(app)

usuario_dao = UsuarioDAO()
cita_dao = CitaDAO()

@app.route('/')
def home():
    return "API funcionando con Firebase"

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if not data or "nombre" not in data or "role" not in data or "correo" not in data or "password" not in data:
        return jsonify({"error": "Faltan datos del usuario"}), 400
    
    new_user = Usuario(
        data["nombre"], data["role"], data["correo"], data["password"], 
        signos_vitales=data.get("signos_vitales", {}), 
        citas=data.get("citas", [])
    )
    
    usuario_dao.agregar_usuario(new_user)
    return jsonify({"message": "Usuario agregado correctamente"}), 201

# Get a user by email
@app.route('/users/<correo>', methods=['GET'])
def get_user(correo):
    usuario = usuario_dao.obtener_usuario(correo)
    if usuario:
        return jsonify(usuario)
    return jsonify({"error": "Usuario no encontrado"}), 404

# Update user data
@app.route('/users/<correo>', methods=['PUT'])
def update_user(correo):
    data = request.json
    if not data:
        return jsonify({"error": "Faltan datos para actualizar"}), 400
    
    usuario_dao.actualizar_usuario(correo, data)
    return jsonify({"message": "Usuario actualizado correctamente"})

# Delete a user
@app.route('/users/<correo>', methods=['DELETE'])
def delete_user(correo):
    usuario_dao.eliminar_usuario(correo)
    return jsonify({"message": "Usuario eliminado correctamente"})

#Agendar cita
@app.route('/citas', methods=['POST'])
def agendar_cita():
    data = request.json

    # Validate request data
    required_fields = ["hora", "estado", "correo_medico", "correo_paciente"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltan datos en la cita"}), 400

#get docs
@app.route('/users/doctors', methods=['GET'])
def get_doctors():
    doctors_ref = db.collection("usuarios").where("rol", "==", "medico", "||", "doctor").stream()
    doctors = [{"correo": doc.id, **doc.to_dict()} for doc in doctors_ref]
    return jsonify(doctors), 200


    # Extract data
    cita = Cita(hora=data["hora"], estado=data["estado"])
    correo_medico = data["correo_medico"]
    correo_paciente = data["correo_paciente"]

    try:
        cita_dao.agregar_cita(cita, correo_medico, correo_paciente)
        return jsonify({"message": "Cita agregada correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


if __name__ == '__main__':
    app.run(debug=True)

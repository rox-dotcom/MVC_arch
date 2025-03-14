from flask import Flask, request, jsonify
from flask_cors import CORS
from dao.usuario_dao import UsuarioDAO
from modelos.usuario import Usuario

app = Flask(__name__)
CORS(app)

usuario_dao = UsuarioDAO()

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




if __name__ == '__main__':
    app.run(debug=True)

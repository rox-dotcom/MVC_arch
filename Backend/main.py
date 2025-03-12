from flask import Flask
from dao.usuario_dao import UsuarioDAO
from modelos.usuario import Usuario

app = Flask(__name__)

@app.route('/')
def home():
    return "API funcionando"

if __name__ == '__main__':
    usuario_dao = UsuarioDAO()
    usuario = Usuario("Juan Perez", "admin", "juan@example.com")
    usuario_dao.agregar_usuario(usuario)
    app.run(debug=True)
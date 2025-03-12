import firebase_admin
from firebase_admin import credentials, firestore

class ConexionFirebase:
    def __init__(self):
        # Solo inicializa Firebase si no ha sido inicializado aún
        if not firebase_admin._apps:
            self.cred = credentials.Certificate('dao/firebaseConfig.json')
            firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def get_db(self):
        return self.db

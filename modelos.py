from flask_login import UserMixin
from database import obter_conexao

class User(UserMixin):
    def __init__(self, nome, id=None):
        self.nome = nome
        self.id = id

    @staticmethod
    def get(user_id):
        conn = obter_conexao()
        cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()

        if user:
            usuario = User(nome=user['email'], id=user['id'])
            return usuario
        return None

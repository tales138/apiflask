
from werkzeug.security import generate_password_hash, check_password_hash
from app.server import db

#modelo para criar um usuários
class Usuario(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
    
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
        return True
    #retorna os dados do usuário no formato JSON    
    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email}
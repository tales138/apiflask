from app.models.usuario import Usuario
from app.utils.validators import is_valid_email,is_valid_name,is_password_strong
from werkzeug.security import generate_password_hash, check_password_hash

def user_create(name,email,password):
    if(is_valid_name(name) and is_valid_email(email) and is_password_strong(password=password)):
        password = generate_password_hash(password)
        user = Usuario(name=name,email=email,password=password)
        print("oi")
        user.save_user()
        return True
    return False

def user_delete(id):
    user = Usuario.query.filter_by(id=id).first()
    user.delete_user()

def is_user_valid(email):
    user = Usuario.query.filter_by(email=email).first()
    if not user:
        return False
    return True
def is_user_valid_id(uid):
    user = Usuario.query.filter_by(email=uid).first()
    if not user:
        return False
    return True
def get_user_id(email):
    user = Usuario.query.filter_by(email=email).first()
    return user.id
def get_all_users():
        usuarios_objetos = Usuario.query.all()
        usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
        return usuarios_json
def check_password(email,password):
    user = Usuario.query.filter_by(email=email).first()
    if(check_password_hash(user.password, password)):
        return True
    

def edit_user(uid, name, email):
    user = Usuario.query.filter_by(id=uid).first()

    if(is_valid_name(name=name) and is_valid_email(email=email)):
        user.name = name
        user.email = email
        user.save_user()

    return True

def delete_user(uid):
   user = Usuario.query.filter_by(id=uid).first()
   user.delete_user()
   return True
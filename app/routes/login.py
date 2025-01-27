from flask import  jsonify,request,make_response
from app.models.usuario import Usuario
from werkzeug.security import  check_password_hash
from app.services.auth.jwt_token.token_singleton import token_creator
from flask import Blueprint
from app.services.usuario_services.usuarios_services import *

route_login = Blueprint('route_login', __name__)
@route_login.route("/login",methods=["POST"])
def login():
    """
    Login de usuário (retorna token JWT e id do usuário(uid))
    ---
    tags:
      - Autenticação
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              description: Email do usuário
              example: user@example.com
            password:
              type: string
              description: Senha do usuário
              example: senha123
    responses:
      201:
        description: Login bem-sucedido, retorna o token de autenticação
        schema:
          type: object
          properties:
            message:
              type: string
              example: Login successful
            auth_token:
              type: string
              description: Token JWT para autenticação
              example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
            uid:
              type: integer
              description: id usuário
              example: 123
      400:
        description: Erro de validação, campos obrigatórios não enviados
        schema:
          type: object
          properties:
            error:
              type: string
              example: Email and password are required
      401:
        description: Erro de autenticação, email ou senha inválidos
        schema:
          type: object
          properties:
            error:
              type: string
              example: Invalid email or password
    """



    
    try:
            request_data = request.get_json()

            # Validar se os campos foram enviados
            if 'email' not in request_data or 'password' not in request_data:
                return make_response(jsonify({"error": "Email e senha são requeridos"}), 400)

            email = request_data['email']
            pwd = request_data['password']

            if( not is_user_valid(email=email) or not check_password(email=email,password=pwd)):
                return make_response(jsonify({"error": " email ou senha inválidos"}), 401)

            # Login bem-sucedido
            uid =  get_user_id(email=email)
            
            auth_token =  token_creator.generate_token(uid) 

            return make_response(jsonify({"message": "Login sbem sucedido", "auth_token":auth_token,"uid":uid}), 201)
    except:
            return make_response(jsonify({"error": "não foi possível fazer login"}), 401)
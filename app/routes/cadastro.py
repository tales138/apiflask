from flask import  jsonify,request,make_response
from app.services.usuario_services.usuarios_services import user_create
from flask import Blueprint
from sqlalchemy.exc import IntegrityError
#defininindo a bluprint da rota
route_bp_register_user = Blueprint('route_bp_register_user', __name__)

#rota para cadastrar/criar um novo usuário
@route_bp_register_user.route("/cadastrar",methods=["POST"])
def cadastrar():
    #DESCRIÇÃO SWAGGER
    """
    Cadastrar um novo usuário
    ---
    tags:
      - Usuários
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Nome do usuário
              example: João Silva
            email:
              type: string
              description: Email do usuário
              example: joao.silva@example.com
            password:
              type: string
              description: Senha do usuário
              example: senha123
    responses:
      201:
        description: Usuário cadastrado com sucesso
        schema:
          type: object
          properties:
            Success:
              type: string
              example: Usuario cadastrado com sucesso
      400:
        description: Requisição inválida
        schema:
          type: object
          properties:
            Error:
              type: string
              example: Campos obrigatórios ausentes ou inválidos
      401:
        description: Dados fora do padrão aceito
        schema:
          type: object
          properties:
            Error:
              type: string
              example: Erro ao cadastrar usuário
    """


    try:    
        request_data = request.get_json()
        
        name = request_data['name']
        email = request_data['email']
        pwd = request_data['password']
        print(email)

        if(user_create(name=name,email=email,password=pwd)):
              return make_response(jsonify({"Success": "Usuario cadastrado com suscesso"}), 201)
        return  make_response(jsonify({"Error": "Erro ao cadastrar usuário"}), 401)
    except:
          return  make_response(jsonify({"Error": "Campos obrigatórios ausentes ou inválidos"}), 400)
    

      
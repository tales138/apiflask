
from app.services.auth.jwt_token.token_verifier import verify_token
from app.models.usuario import Usuario
from app.models.admin import Admin
from app.services.admin_services.verify_admin import admin_required
from flask import Blueprint
from app.services.usuario_services.usuarios_services import get_all_users
from flask import  make_response,jsonify
route_list_users = Blueprint('route_list_users', __name__)
@route_list_users.route("/usuarios", methods=["GET"])

#rota para listar usuários. restrito a admins
@verify_token#decorator para verificar se o token de autenticação é válido
@admin_required(Admin)#decorator para verificar se o usuário é admin
def listar_usuarios():
    #DESCRIÇÃO SWAGGER
    """
Retornar a lista de usuários (Permitido apenas para admins)
---
tags:
  - Usuários
parameters:
  - name: Authorization
    in: header
    type: string
    required: true
    description: "Token de autenticação JWT"
    schema:
          type: string
          example: Bearer your_token_here
  - name: uid
    in: header
    type: integer
    required: true
    description: "ID do usuário logado"
    schema:
        type: integer
        example: 123 
responses:
  200:
    description: Lista de usuários retornada com sucesso
    schema:
      type: object
      properties:
        users_list:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: "Pedro"
              email:
                type: string
                example: "pedro@example.com"
  401:
    description: Erro ao tentar listar os usuários, pode ser relacionado a permissões ou falhas de autenticação
    schema:
      type: object
      properties:
        Error:
          type: string
          example: "não foi possível retornar a lista de usuários"
"""
    try:
        return make_response(jsonify({"users list": get_all_users()}), 201)
    except:
        return make_response(jsonify({"Error": "não foi possível retornar a lista de usuários"}), 401)
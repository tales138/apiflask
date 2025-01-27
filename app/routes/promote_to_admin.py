
from flask import  jsonify,request,make_response
from app.models.admin import Admin
from app.services.admin_services.verify_admin import admin_required
from app.services.auth.jwt_token.token_verifier import verify_token
from flask import Blueprint
from app.services.usuario_services.usuarios_services import *
from app.services.admin_services.admin_services import *

route_bp_promote_admin = Blueprint('route_bp_promote_admin', __name__)
@route_bp_promote_admin.route("/promoteadmin", methods=["POST"])

@verify_token
@admin_required(Admin)
def promote_to_admin():
    #DESCRIÇÃO SWAGGER
    """
    Promover usuário a admin. Disponível apenas para admins. Rota real.
    ---
    tags:
      - Admin
    parameters:
      - name: id
        in: body
        required: true
        schema:
          type: integer
          properties:
            uid:
              type: integer
              description: ID do usuário a ser promovido
              example: 123
      - name: Authorization
        in: header
        required: true
        description: Token de autenticação JWT a ser invalidado
        schema:
          type: string
          example: Bearer <your_token_here>
      - name: uid
        in: header
        type: integer
        required: true
        description: "ID do usuário logado"
        schema:
            type: integer
            example: 123 
    responses:
      201:
        description: Usuário promovido a admin com sucesso
        schema:
          type: object
          properties:
            message:
              type: string
              example: User promoted to admin successfully
      400:
        description: Erro de validação, falta o campo `uid` ou formato inválido
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'User not found' 
      401:
        description: Erro de autenticação ou já é admin
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'User is already an admin'
      403:
        description: Erro de permissão, usuário não é admin
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'Permission denied, only admins can promote users'
    """
    try:
        data = request.get_json()
        usuario_id = data.get('id')
        if not is_user_valid_id(usuario_id):

            return  make_response(jsonify({'error': 'User not found'}), 404)

        # Verifica se o usuário já é admin
        if is_admin(usuario_id):
            return make_response(({'error': 'User is already an admin'}), 401)

        promote_user_to_admin(uid=usuario_id)

        return make_response(jsonify({'message': 'User promoted to admin successfully'}), 201)
    except:
        return make_response(jsonify({'Error': 'Não foi possível conceder o priveligio de admin ao ussuario'}), 401)


@route_bp_promote_admin.route("/promoteadmintest", methods=["POST"])
@verify_token
def add_admin_test():
     #SWAGGER DESCRIPTION 
    """
    Rota para cadastrar um admin de teste no cenário que o banco ainda estiver vazio. Usuario precisa está logado.
    ---
    tags:
      - Admin
    parameters:
      - name: id
        in: body
        required: true
        schema:
          type: integer
          properties:
            id:
              type: integer
              description: ID do usuário a ser promovido
              example: 123
      - name: Authorization
        in: header
        type: string
        required: true
        description: "Token de autenticação JWT"
        schema:
          type: string
          example: Bearer your_token_here"
    responses:
      201:
        description: Usuário promovido a admin com sucesso
        schema:
          type: object
          properties:
            message:
              type: string
              example: User promoted to admin successfully
      400:
        description: Erro de validação, falta o campo `uid` ou formato inválido
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'User not found' 
      401:
        description: Erro de autenticação ou já é admin
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'User is already an admin'
      403:
        description: Erro de permissão, usuário não é admin
        schema:
          type: object
          properties:
            error:
              type: string
              example: 'Permission denied, only admins can promote users'
    """
    try:
        data = request.get_json()
        usuario_id = data.get('uid')
        if not is_user_valid_id(usuario_id):

            return  make_response(jsonify({'error': 'usuário não encontrado'}), 404)

        # Verifica se o usuário já é admin
        if is_admin(usuario_id):
            return make_response(({'error': 'usuário já é admin'}), 401)

        promote_user_to_admin(uid=usuario_id)

        return make_response(jsonify({'message': 'usuário promovido a admin com sucesso'}), 201)
    except:
        return make_response(jsonify({'Error': 'Não foi possível conceder o privelegio de admin ao ussuario'}), 401)
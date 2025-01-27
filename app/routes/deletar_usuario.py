
from flask import  jsonify,request,make_response
from app.models.admin import Admin
from app.services.admin_services.verify_admin import admin_required
from app.services.auth.jwt_token.token_verifier import verify_token
from flask import Blueprint
from app.services.usuario_services.usuarios_services import delete_user

route_bp_delete_user = Blueprint('route_bp_delete_user', __name__)
# Método para deletar um usuário
@route_bp_delete_user.route("/usuario/<id>", methods=["DELETE"])
@verify_token
@admin_required(Admin)
def deleta_usuario():
    """
    Excluir um usuário
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        required: true
        description: ID do usuário a ser excluído
        schema:
          type: integer
          example: 123   
      - name: Authorization
        in: header
        type: string
        required: true
        description: "Token de autenticação JWT"
        schema:
          type: string
          example: Bearer <your_token_here>'"
      - name: uid
        in: header
        type: integer
        required: true
        description: "ID do usuário logado"
        schema:
            type: integer
            example: 123 '
    responses:
      200:
        description: Usuário deletado com sucesso
        schema:
          type: object
          properties:
            Success:
              type: string
              example: Usuario deletado com sucesso
      401:
        description: Erro ao tentar excluir o usuário, verifique o id, permissões ou falha de autenticação
        schema:
          type: object
          properties:
            Error:
              type: string
              example: Erro ao deletar usuario
      404:
        description: Usuário não encontrado
        schema:
          type: object
          properties:
            Error:
              type: string
              example: Usuário não encontrado
    """
    try:  
        id = request.view_args['id']
        delete_user(id)
        return make_response(jsonify({"Success": "Usuario deletado com sucesso"}), 201)
    except:
        return make_response(jsonify({"Error": "Erro ao deletar usuario"}), 401)
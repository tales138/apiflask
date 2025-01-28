
from flask import  jsonify,request,make_response
from app.services.auth.jwt_token.token_verifier import verify_token
from app.services.usuario_services.usuarios_services import edit_user
from flask import Blueprint


route_bp_edit_user = Blueprint('route_bp_edit_user', __name__)
# Método para atualizar os dados de um usuário
@route_bp_edit_user.route("/usuarios", methods=["PUT"])
@verify_token
def atualiza_usuario():
    #DESCRIÇÃO SWAGGER
    """
    Atualizar dados de um usuário existente
    ---
    tags:
      - Usuários
    parameters:
      - name: body
        in: body
        required: true
        description: Dados do usuário a serem atualizados
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Novo Nome"
            email:
              type: string
              example: "novonome@example.com"
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
    responses:
      200:
        description: Usuário atualizado com sucesso
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Dados atualizados com sucesso"
      400:
        description: Dados inválidos ou faltando campos obrigatórios
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Dados inválidos, campos 'name' e 'email' são obrigatórios"
      401:
        description: Erro ao tentar atualizar o usuário, devido a falha de permissão ou erro de autenticação
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Erro ao atualizar dados do usuário"
    """
    try:
        body = request.get_json()
        uid = request.headers.get("uid")
        if(body['name'] and body['email']):
            edit_user(uid,body['name'],body['email'])

        return make_response(jsonify({"error": "Dados atualizados com sucesso"}), 201)
    except:
         return make_response(jsonify({"error": "Erro ao atualizar dados do usuário"}),401)
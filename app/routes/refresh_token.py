from flask import  jsonify,request,make_response
from app.services.auth.jwt_token.token_verifier import verify_token
from flask import Blueprint
from app.services.auth.jwt_token.token_singleton import token_creator

route_refresh_token = Blueprint('route_refresh_token', __name__)
@verify_token
@route_refresh_token.route("/refreshtoken",methods=["POST"])
def resfresh_token_route():
    #DESCRIÇÃO SWAGGER
    """
    Renovar o token de autenticação. Se token estiver expirado, retorna um novo token. Caso contrário o mesmo token.
    ---
    tags:
      - Autenticação
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token de autenticação atual
        example: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
      - name: uid
        in: header
        type: integer
        required: true
        description: ID do usuário associado ao token
        example: "123"
    responses:
      201:
        description: Token de autenticação renovado com sucesso
        schema:
          type: object
          properties:
            Success:
              type: string
              example: "Token de autenticação renovado"
            auth_token:
              type: string
              description: Novo token JWT gerado
              example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
      400:
        description: Falha ao renovar o token de autenticação
        schema:
          type: object
          properties:
            Error:
              type: string
              example: "Falha ao renovar token de autenticação"
      401:
        description: Não autorizado. Pode ser causado por
            - Token inválido
            - Token expirado
            - Token bloqueado
            - ID do usuário não autorizado
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Not authorized"
    """
    try:
        token = request.headers.get("Authorization")
        token = token.split()[1]
        new_auth_token = token_creator.refresh(token)

        return make_response(jsonify({"Sucess": "Token de autenticação renovado", "auth_token":new_auth_token}), 201)
    except:
        return make_response(jsonify({"Error": "Falha ao renovar token de autenticação"}), 400)


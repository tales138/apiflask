
from flask import  jsonify,request,make_response
from app.services.auth.jwt_token.token_verifier import verify_token
from app.models.token_blocklist import TokenBlocklist
from flask import Blueprint
route_bp_logout = Blueprint('route', __name__)

@route_bp_logout.route("/logout",methods=["POST"])
@verify_token#decorator para verificar se o token de autenticação é válido
def logout():
    #DESCRIÇÃO SWAGGER
    """
    Logout de usuário (bloqueio do token)
    ---
    tags:
      - Autenticação
    parameters:
      - name: Authorization
        in: header
        required: true
        description: Token de autenticação JWT a ser invalidado
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
      201:
        description: Logout bem-sucedido, token invalidado
        schema:
          type: object
          properties:
            Success:
              type: string
              example: Usuario deslogado com sucesso
      400:
        description: Erro de requisição, token não encontrado ou inválido
        schema:
          type: object
          properties:
            error:
              type: string
              example: Token não encontrado no cabeçalho Authorization
      401:
        description: Erro de autenticação, token inválido ou expirado
        schema:
          type: object
          properties:
            error:
              type: string
              example: Token inválido ou expirado
    """
    try:
        request_data = request.headers.get("Authorization")
        tok = request_data.split()[1]
        blocked_token = TokenBlocklist()
        blocked_token.jwt_t(jwt=tok)
        blocked_token.block_token()
        return make_response(jsonify({"Success": "Usuario deslogado com sucesso"}), 201)
    except:
        return make_response(jsonify({"Error": "Erro ao deslogar usuário"}), 401)
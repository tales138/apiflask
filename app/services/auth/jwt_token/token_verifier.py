from functools import wraps
from flask import jsonify,request,make_response
import jwt
from app.services.auth.jwt_token import token_creator
from app.models.token_blocklist import TokenBlocklist
def verify_token(function:callable) -> callable:
    @wraps(function)
    def decorated(*arg, **kwargs):
        raw_token = request.headers.get("Authorization")
        uid = request.headers.get("uid")
        
        token = raw_token.split()[1]
        blokec_token =  TokenBlocklist()
        blokec_token.jwt_t(jwt=token)
        if(not  raw_token or not uid):
             return make_response(jsonify({"error": "não autorizado"}), 401)
        
        try:
            token_information = jwt.decode(token,key='1234',algorithms='HS256')
            token_uid = token_information["uid"]
            
        except jwt.InvalidSignatureError:
            return make_response(jsonify({"error": "token inválido"}), 401)
        except jwt.InvalidAlgorithmError:
            return make_response(jsonify({"error": "token inválido"}), 401)
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({"error": "token expirado"}), 401)
        except KeyError as e:
            return make_response(jsonify({"error": "token inválido"}), 401)
        if(blokec_token.is_token_blocked()):
            return make_response(jsonify({"error": "token inválido"}), 401)
        if int(token_uid) != int(uid):
            return make_response(jsonify({"error": "usuário não autorizado"}), 401)
        
        return function(*arg,**kwargs)
    return decorated
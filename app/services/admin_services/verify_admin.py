from functools import wraps
from flask import jsonify,request,make_response
import jwt
SECRET_KEY = "1234"

def admin_required(adm):
    """
    Decorator para verificar se o usuário autenticado é administrador.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Obtém o token do cabeçalho Authorization
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                return jsonify({'error': 'Token is missing or invalid'}), 401
            
            token = auth_header.split(" ")[1]  # Obtém o token (Bearer <token>)
            
            try:
                # Decodifica o token
                payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                user_id = payload.get('uid')
                
                # Verifica se o usuário é admin
                is_admin = adm.query.filter_by(usuario_id=user_id).first()
                if not is_admin:
                    return jsonify({'error': 'Admin access required'}), 403

            except jwt.ExpiredSignatureError:
                return jsonify({'error': 'Token has expired'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'error': 'Invalid token'}), 401
            
            # Token válido e usuário é admin
            return f(*args, **kwargs)
        
        return decorated_function
    return decorator
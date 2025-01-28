from app.server import db

#modelo para criar e salvar um token na lista de bloqueados(expirados), quando o usuário faz logout
class TokenBlocklist(db.Model):
    __tablename__ = 'token_blocklist'

    token_id = db.Column(db.Integer, autoincrement=True,primary_key=True)  # ID único para cada registro
    jwt = db.Column(db.String(116), nullable=False, unique=True)  # Identificador único do token (JTI)
    created_at = db.Column(db.DateTime,default=db.func.now())  # Data de revogação
    
    def jwt_t(self,jwt):
        self.jwt = jwt 

    def __repr__(self):
        return f"<TokenBlocklist id={self.token_id} jti={self.jwt}> created_at={self.created_at}"
    
    def block_token(self):
        db.session.add(self)
        db.session.commit()
        return True
    
    def is_token_blocked(self):
         blocked_token = TokenBlocklist.query.filter_by(jwt=self.jwt).first()
         return blocked_token is not None  # Retorna True se o token foi bloqueado
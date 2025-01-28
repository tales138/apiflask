from app.server import db
class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('admin', uselist=False))

    # Campos adicionais (opcional)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def save_admin(self):
        db.session.add(self)
        db.session.commit()
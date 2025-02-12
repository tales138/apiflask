from app.models.admin import Admin

def promote_user_to_admin(uid):
    admin = Admin(usuario_id=uid)
    admin.save_admin()
    return True

def is_admin(uid):
    user = Admin.query.filter_by(usuario_id=uid).first()
    if user:
        return True
    return False
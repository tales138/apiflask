def register_routes(app):
    from app.routes.login import route_login
    from app.routes.logout import route_bp_logout
    from app.routes.listar_usuarios import route_list_users
    from app.routes.promote_to_admin import route_bp_promote_admin
    from app.routes.editar_usuario import route_bp_edit_user
    from app.routes.deletar_usuario import route_bp_delete_user
    from app.routes.cadastro import route_bp_register_user
    from app.routes.refresh_token import route_refresh_token
    app.register_blueprint(route_bp_logout)
    app.register_blueprint(route_login)
    app.register_blueprint(route_list_users)
    app.register_blueprint(route_bp_promote_admin)
    app.register_blueprint(route_bp_edit_user)
    app.register_blueprint(route_bp_delete_user)
    app.register_blueprint(route_bp_register_user)
    app.register_blueprint(route_refresh_token)
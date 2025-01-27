from flask import Flask
from .extensions.db_connection import *
from app.routes import register_routes
from flasgger import Swagger
#from .routes.login import route_bp_login
app = Flask(__name__)

swagger = Swagger(app)
db = start_postgres_connection(app)

with app.app_context(): 
    db.create_all()
    
register_routes(app)



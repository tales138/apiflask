from flask_sqlalchemy import SQLAlchemy
from os import environ
def start_postgres_connection(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    
    #sem necessidade de realizar alterações para execução docker ou no ambiente python local.
    if(environ.get('DB_URL')):
        app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345@localhost:5432/postgres"
   
    db_connection = SQLAlchemy(app)
    
    return db_connection


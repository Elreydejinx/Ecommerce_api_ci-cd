from flask import Flask
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
import os
import psycopg2

app = Flask(__name__)
api = Api(app)

SWAGGER_URI = '/swagger'
API_URL = '/swagger/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URI,
    API_URL,
    config={'app_name': 'Flask API'}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URI)

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    conn.close()
    return 'Hello, world!'

if __name__ == '__main__':
    app.run
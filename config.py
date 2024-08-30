import os
import app


DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://flask_api_150_gt4k_user:vqkhuEGJeVoddVdb83SIktC4LKzv35zC@dpg-cr4avcjv2p9s73cpie8g-a/flask_api_150_gt4k')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

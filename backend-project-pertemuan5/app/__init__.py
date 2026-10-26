from flask import Flask
from app.routes.v1.product_routes import product_bp_v1

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(product_bp_v1)
    
    return app
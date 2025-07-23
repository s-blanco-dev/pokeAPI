from flask import Flask
from routes.favoritos_bp import favoritos_bp
from routes.horoscopo_bp import horoscopo_bp
from routes.pokemon_bp import pokemon_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(horoscopo_bp)
    app.register_blueprint(favoritos_bp)
    app.register_blueprint(pokemon_bp)
    return app

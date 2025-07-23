from flask import Blueprint, request, jsonify
from models.horoscopo import obtenerPokemon

horoscopo_bp = Blueprint("horoscopo", __name__)

@horoscopo_bp.route("/horoscopo", methods=["POST"])
def horoscopo():
    data = request.get_json()
    nombre = data.get("nombre")
    fecha = data.get("fecha")

    # ambos campos son obligatorios
    if not nombre or not fecha:
        return jsonify({"error": "Faltan datos"}), 400

    try:
        resultado = obtenerPokemon(nombre, fecha)
        return jsonify(resultado.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500



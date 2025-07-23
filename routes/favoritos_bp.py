from flask import Blueprint, request, jsonify
from models.favoritos import Favoritos

favoritos_bp = Blueprint("favoritos", __name__)

@favoritos_bp.route("/favoritos", methods=["POST"])
def guardarFavorito():
    data = request.get_json()

    if not data or "usuario" not in data or "pokemon" not in data:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    usuario = data["usuario"]
    nombre_pokemon = data["pokemon"]

    try:
        Favoritos.guardar(usuario, nombre_pokemon)
        return jsonify({"mensaje": f"{nombre_pokemon} guardado en favoritos de {usuario}"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

@favoritos_bp.route("/favoritos", methods=["DELETE"])
def eliminarFavorito():
    data = request.get_json()
    if not data or "usuario" not in data or "pokemon" not in data:
        return jsonify({"todo mal": "Se requiere 'usuario' y 'nombre' del Pokémon"}), 400

    usuario = data["usuario"]
    nombre_pokemon = data["pokemon"]

    eliminado = Favoritos.eliminar(usuario, nombre_pokemon)

    if eliminado:
        return jsonify({"ojo": f"{nombre_pokemon} eliminado de los favoritos de {usuario}"}), 200
    else:
        return jsonify({"ojo": f"{nombre_pokemon} no se encontraba en los favoritos de {usuario}"}), 404


@favoritos_bp.route("/favoritos", methods=["GET"])
def listar_favoritos():
    usuario = request.args.get("usuario")
    if not usuario:
        return jsonify({"te falla?": "Falta el parámetro 'usuario'"}), 400

    favoritos = Favoritos.obtenerPokemonesUsuario(usuario)
    return jsonify(favoritos), 200

@favoritos_bp.route("/favoritos/<int:id_pokemon>", methods=["GET"])
def buscarFavorito(id_pokemon):
    usuario = request.args.get("usuario")
    
    if not usuario:
        return jsonify({"hacé las cosas bien": "Debe especificarse el usuario"}), 400

    resultado = Favoritos.buscar_por_id(usuario, id_pokemon)

    return jsonify(resultado), 200

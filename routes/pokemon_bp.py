from flask import Blueprint, request, jsonify
import requests
from utils.apiUtils import obtenerPokemonPorNombre

pokemon_bp = Blueprint("pokemon", __name__)

@pokemon_bp.route("/pokemon", methods=["GET"])
def buscar_pokemon():
    nombre = request.args.get("nombre")
    tipo = request.args.get("tipo")
    resultados = []

    if not nombre and not tipo:
        return jsonify({"error": "Debe especificar al menos 'nombre' o 'tipo'"}), 400

    if nombre:
        pokemon = obtenerPokemonPorNombre(nombre)
        if pokemon:
            if not tipo or tipo.lower() in [t.lower() for t in pokemon.tipos]:
                resultados.append(pokemon.to_dict())
        return jsonify(resultados)

    if tipo:
        url = f"https://pokeapi.co/api/v2/type/{tipo.lower()}"
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify([])

        data = response.json()
        for entry in data["pokemon"]:
            nombre_pokemon = entry["pokemon"]["name"]
            poke = obtenerPokemonPorNombre(nombre_pokemon)
            if poke:
                resultados.append(poke.to_dict())

    return jsonify(resultados)


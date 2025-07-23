from models.pokemon import Pokemon
from utils.apiUtils import obtenerPokemonPorNombre
import json
import os

ARCHIVITO = "favoritos.json"

class Favoritos:
    @staticmethod
    def guardar(usuario: str, nombre_pokemon: str):
        datos = {}
        if os.path.exists(ARCHIVITO):
            with open(ARCHIVITO, "r") as f:
                datos = json.load(f)

        if usuario not in datos:
            datos[usuario] = []

        pokemon = obtenerPokemonPorNombre(nombre_pokemon)

        if not pokemon:
            raise ValueError(f"No se encontró el Pokémon '{nombre_pokemon}'")

        pokemon_dict = pokemon.to_dict()

        if not any(p["nombre"] == pokemon_dict["nombre"] for p in datos[usuario]):
            datos[usuario].append(pokemon_dict)

            with open(ARCHIVITO, "w") as f:
                json.dump(datos, f, indent=2)
        else:
            print("El Pokémon ya está en favoritos")   

    @staticmethod
    def eliminar(usuario: str, pokemon: str) -> bool:
        if not os.path.exists(ARCHIVITO):
            return False

        with open(ARCHIVITO, "r") as f:
            datos = json.load(f)

        if usuario not in datos:
            return False
        
        favoritos_archivo = len(datos[usuario])
        datos[usuario] = [p for p in datos[usuario] if p["nombre"] != pokemon]
                

        if len(datos[usuario]) == favoritos_archivo:
            return False  # no se eliminó nada

        with open(ARCHIVITO, "w") as f:
            json.dump(datos, f, indent=2)

        return True

    @staticmethod
    def obtenerPokemonesUsuario(usuario: str):
        if not os.path.exists(ARCHIVITO):
            return []

        with open(ARCHIVITO, "r") as f:
            datos = json.load(f)

        return datos.get(usuario, [])
        
        

        
    @staticmethod
    def buscar_por_id(usuario: str, id_pokemon: int):
        if not os.path.exists(ARCHIVITO):
            return {}

        with open(ARCHIVITO, "r") as f:
            datos = json.load(f)

        if usuario not in datos:
            return {}

        for p in datos[usuario]:
            if p["id"] == id_pokemon:
                return p

        return {}

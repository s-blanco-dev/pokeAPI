import requests
from models.pokemon import Pokemon
import random

def obtenerPokemonPorNombre(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        return {}

    data = response.json()
    return Pokemon(
            id=data["id"],
            nombre=data["name"],
            imagen=data["sprites"]["front_default"],
            tipos=[t["type"]["name"] for t in data["types"]],
            altura=data["height"],
            peso=data["weight"],
            habilidades=[h["ability"]["name"] for h in data["abilities"]]
            ) 
    
def obtenerRandomPorTipo(tipo):
    url = f"https://pokeapi.co/api/v2/type/{tipo.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"No se pudo obtener el tipo '{tipo}' de la PokéAPI.")

    data = response.json()
    lista_pokemon = data["pokemon"]
    if not lista_pokemon:
        raise ValueError(f"No hay Pokémon del tipo '{tipo}'.")

    pokemon_aleatorio = random.choice(lista_pokemon)["pokemon"]["name"]

    return obtenerPokemonPorNombre(pokemon_aleatorio)

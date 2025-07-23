from flask import Flask
from datetime import datetime
import utils.apiUtils


SIGNO_TIPO = {
    "Aries": "fire",
    "Tauro": "grass",
    "Géminis": "electric",
    "Cáncer": "water",
    "Leo": "fire",
    "Virgo": "bug",
    "Libra": "flying",
    "Escorpio": "dark",
    "Sagitario": "fighting",
    "Capricornio": "rock",
    "Acuario": "psychic",
    "Piscis": "dragon"
}

def calcularSigno(fecha_str):
    fecha = datetime.strptime(fecha_str, "%d-%m-%Y")
    dia = fecha.day
    mes = fecha.month

    # arreglo con inicio:(mes, dia), fin:(mes,dia)
    # le pedí a ChatGPT que me hiciera el diccionario
    signos = [
        ((1, 20), (2, 18), "Acuario"),
        ((2, 19), (3, 20), "Piscis"),
        ((3, 21), (4, 19), "Aries"),
        ((4, 20), (5, 20), "Tauro"),
        ((5, 21), (6, 20), "Géminis"),
        ((6, 21), (7, 22), "Cáncer"),
        ((7, 23), (8, 22), "Leo"),
        ((8, 23), (9, 22), "Virgo"),
        ((9, 23), (10, 22), "Libra"),
        ((10, 23), (11, 21), "Escorpio"),
        ((11, 22), (12, 21), "Sagitario"),
        ((12, 22), (1, 19), "Capricornio"),
    ]

    for ee in signos:
        if mes >= ee[0][0] & mes <= ee[1][0]:
            if dia >= ee[0][1] & dia <= ee[1][1]:
                return ee[2]

def obtenerRandomPorSigno(signo):
    return utils.apiUtils.obtenerRandomPorTipo(SIGNO_TIPO[signo])

def obtenerPokemon(nombre, fecha):
    return obtenerRandomPorSigno(calcularSigno(fecha))

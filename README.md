# pokeAPI Mini proyecto

## 🚀 Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## 🧑‍💻 Instrucciones del año XIII 

1. **Cloná el repositorio**:

   ```bash
   git clone https://github.com/s-blanco-dev/pokeAPI.git
   cd pokeAPI 
   ```

2. **Construí y ejecutá el contenedor**:

   ```bash
   docker compose up --build
   ```

Ahora debería estar ejecutandose y escuchando en `http://localhost:5000`

## 🧪 Endpoints

- `GET /horoscopo` -> Devuelve un Pokemon aleatorio del tipo que coincide con tu signo (`nombre`, `fecha: dd-mm-YYYY`)
- `POST /favoritos` -> Guarda un Pokemon favorito (`usuario`, `pokemon`)
- `GET /favoritos?usuario=Ash` -> Devuelve lista de Pokemon guardados como favorito para el usuario dado
- `GET /favoritos/<id>?usuario=Ash`  
- `DELETE /favoritos/` -> Elimina Pokemon de favoritos (`usuario`, `pokemon`)
- `GET /pokemon?nombre=charizard&tipo=fire` -> Devuelve chorizard desde la PokéAPI
- `GET /pokemon?tipo=fire` -> Devuelve todos los Pokemon tipo fire desde la PokéAPI (Puede tardar unos cuantos meses)

## 🧹 Limpiar

Para detener y eliminar el contenedor, podés usar:

```bash
docker compose down
```
## Pruebas con Postman
Recibe un nombre (por ahora no sirve para nada) y una fecha en formato dd-mm-YYYY. `20-12` corresponde a Sagitario, que está mapeado arbitrariamente al tipo de Pokemon "fighting" -> Devuelve un Pokemon al azar del tipo dado desde la PokeAPI
<img width="1459" height="694" alt="1753303863" src="https://github.com/user-attachments/assets/0a161793-f56c-4796-8635-b26e917bc8de" />
Agrega a favoritos de un usuario. Los datos se guardan en `favoritos.json`:
<img width="1439" height="539" alt="1753304234" src="https://github.com/user-attachments/assets/80a35c55-2fd8-44cb-a47f-b34c22a1a580" />
Habiendole agregado a Pikachu y Charizard, obtengo los favoritos para un usuario dado:
<img width="1446" height="797" alt="1753304393" src="https://github.com/user-attachments/assets/d86c2f04-996c-452e-b186-d0caf6bd626d" />


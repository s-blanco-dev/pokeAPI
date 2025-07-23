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

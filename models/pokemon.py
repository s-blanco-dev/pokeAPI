class Pokemon:
    def __init__(self, id, nombre, imagen, tipos, altura, peso, habilidades):
        self.id = id
        self.nombre = nombre # string
        self.imagen = imagen
        self.tipos = tipos  # array de strings (odio python) 
        self.altura = altura
        self.peso = peso
        self.habilidades = habilidades  # otro array de strings 

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "imagen": self.imagen,
            "tipos": self.tipos,
            "altura": self.altura,
            "peso": self.peso,
            "habilidades": self.habilidades,
        }

    # toString
    def __str__(self):
        return f"{self.nombre.capitalize()}\n - (ID {self.id})\n - Tipo: {', '.join(self.tipos)}\n - Altura: {self.altura}\n - Peso: {self.peso}\n - Habilidades: {', '.join(self.habilidades)}"

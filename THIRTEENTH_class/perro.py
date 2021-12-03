class Perro:
    """Una clase basica que representa a un perro """
    # init siver para establecer el estado de la clase
    def __init__(self,nombre,edad) -> None:
        """ inicializando el nombre y la edad del perro, que serian los atributos"""
        self.name = nombre
        self.old = edad
        self.raza = "No aplica"
        self.numero_de_juegos_restantes = 3

    def bark(self):
        print(f"Hola soy {self.name} y digo guau")

    def play(self):
        if self.numero_de_juegos_restantes > 0 :
            print(f"Hola soy un perro de la raza {self.raza} y me divierto buscando la pelota")
            self.numero_de_juegos_restantes -= 1

        else:
            print(f"Hola soy un perro de la raza {self.raza} y ya no puedo jugar")

    def saludar_otro_perro(self, otro_perro):
        print(f"Hola soy {self.nombre} y estoy saludando a mi amigo {otro_perro.name}")



#Crear una instancia (instance), casos, eventos, hechos
mi_primer_perro = Perro("Perrry", 2)

print(mi_primer_perro.name)

mi_primer_perro.bark()

for i in range(5):
    mi_primer_perro.play()
        
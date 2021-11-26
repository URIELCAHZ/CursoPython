def describe_animal(tipo_de_animal, nombre_de_animal):
    print("tu tipo de animal es"+ tipo_de_animal + " y se llama " + nombre_de_animal)

animals_names = [("gato", "garfield") , ("conejo" , "Bunny") , ("perro" , "firulais")]

for mascota in animals_names:
    describe_animal(mascota[0] , mascota[1])

""" Arguments default"""
def describe_animal_default(tipo_de_animal = "pez", nombre_de_animal = "tiburon"):
    print("tu tipo de animal es"+ tipo_de_animal + " y se llama " + nombre_de_animal)

print()
describe_animal_default()


""" Arguments default"""
def describe_animal_arbitrary(*animales):
    print( f"tu tipo de animal es {animales[0][0]} y se llama {animales[0][1]}")

print()
for mascota in animals_names:

    describe_animal_arbitrary(mascota)
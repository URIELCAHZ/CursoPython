colores_base = ["Blanco", "Azul", "Negro", "Verde", "Violeta", "Verde olivo", "Turquesa", "Gris", "Azul Marino", "Magenta", "Rosa"]

colores_favoritos = ["Verde olivo", "Rojo", "Negro"]

for x in colores_favoritos:
    if x in colores_base:
        print(x, "se encuentra en lista")
    else:
        print(x, "no se encuentra en la lista")
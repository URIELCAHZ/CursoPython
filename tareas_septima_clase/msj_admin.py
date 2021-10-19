nombres=["Guadalupe Mendez", "Sergio Clara", "Alfredo Carbaja", "Brianda Lizeht", "Ivan Mauricio", "Alfredo Robledo", "admin"]

for x in nombres:
    if x == "admin":
        print(f"Hola {x}, quieres visualisar el reporte de uso? ")
        Yes = input(" Y para Si, cualquier otra tecla para No ")
        if Yes == "Y" : print(" Por el momento no hay reporte")
    else:
        print(f"Hola, {x}, bienvenido")
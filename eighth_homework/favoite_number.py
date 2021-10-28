
favorite_numbers = {}

while len(favorite_numbers) < 5:
    
    name = input("Ingresa tu nombre: ")
    name = name.lower()
    number=0
    while True:
        number = input("Ingresa tu numero favorito (solo enteros): ")
        if number.isdigit():
            number=int(number)
            break
        else:
            print("no escribiste un numero entero, vuelve a intentar")

    if name in favorite_numbers:
        print("ya te encuentras, se sobreescribira tu numero favorito")
        favorite_numbers[name] = number
    else:
        print("has sido agregado a la lista")
        favorite_numbers[name] = number



print(favorite_numbers)
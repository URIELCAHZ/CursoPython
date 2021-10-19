import random

aleatorio = int(random.uniform(1,101))
print("Adivina el numero entero que se encuentra entre el 1 y el 100")

i = True
while i :
    adivina = input("Ingresa tu numero:")
   
    if not adivina.isdecimal():
       print("tienes que ingresar un numero entero, vuelve a intentar") 
       continue   
       
    adivina = int(adivina)

    if adivina ==  aleatorio: break
    print("numero incorrecto, vuelve a intentar")

print("Felicidades, has adivinado el numero")
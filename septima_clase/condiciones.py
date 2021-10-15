# carros = ["audi","bmw", "subaru", "toyota"]

# for carro in carros:
#     if carro == "bmw":
#       print(carro.upper())
#       print("Es un buen carro")
#     else:
#         print(carro.title())

# print(not True)

"""Operadores para if"""
#!=
# ==         (and or not) modificadores booleanos
# <
# >
# <=
# >=

"""Multiples condiciones"""
# edad=15
# if edad >= 12 and edad <= 18: print("Eres un adolecente")

# if edad < 12 or edad >18: print("No eres un adolecente")

#Version 2 de Paco
# numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# busqueda = 87
# # if busqueda in numeros: print("si se encontro") 
# # else: print("no se encontro")

# print("si se encontro") if busqueda in numeros else print ("no se encontro")

""" if elfi else"""
edad = 45
costo = 0

if edad < 4:
    costo=0
elif edad < 18:
    costo = 80
else:
    costo = 100

print("Te toca pagar", costo)
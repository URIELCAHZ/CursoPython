import sys


# lista = []
# tuple = ()

# print(type(lista))
# print(type(tuple))

"""Saber el tamaño de una lista o un tuple"""

# print(f"Tamaño en memoria de la lista: {sys.getsizeof(lista)}")
# print(f"Tamaño en memoria de la lista: {sys.getsizeof(tuple)}")


""" Acceder a los valores de una lista o un tuple"""
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#Acceder a un valor de la lista o el tuple
print(lista1[2])
print(tuple1[3])

#Acceder al ultimo valor
print(lista1[-1])
print(tuple1[-1])

#Saber el largo de la lista y el tuple
print(len(lista1))
print(len(tuple1))

#Editar valores de una lista
lista2 = [5, 4, 3, 2, 1]
tuple2 = (5, 4, 3, 2, 1)

lista2[0] = 1
#tuple2[-1] = 5
lista2.insert(1,2)
lista2.append(10)

print(lista2, "\n", tuple2)





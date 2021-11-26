def genera_lista():
    participantes = ["juan" , "luis" , "maria"]
    return participantes

modificar = genera_lista()
modificar.append("ultimo")

print(modificar)
print(genera_lista())


def genera_diccionario():
    participantes = {"nombre" : "juan" , "apellido": "Perez"}
    return participantes

print(genera_diccionario)

def genera_funcion(funcion_):
    return funcion_()

print(genera_funcion(genera_diccionario))
print(genera_funcion(genera_lista))


valor = 15
lista = [1 , 2 , 3]

def haz_algo(x):
    x = 25

def haz_algo_mas(x):
    x.append(10)

haz_algo(valor)
haz_algo_mas(lista)

print(valor)
print(lista)

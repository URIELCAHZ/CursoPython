print("1 diccionario duplicado") # No se permiten duplicados
duplicate_dict = {
    "1" : 85,
    "1" : 99,
}
print(duplicate_dict) #imprime el ultimo


print("2 diccionario variado ")
varied_dict = {
    "integer" : 1,
    "string" : "Buenos dias",
    "boolean" : False,
    "float" : 38.56,
    "list" : [1, 2.5, "tres", True],
    "tuple" : ("adios",),
    "another_dict": {"month" : "octubre", "year" : 2021},
    "set" : {"primero", "segundo", "tercero", "cuarto"}
}
print(varied_dict)


print("3 copiar diccionario")
duplicate = varied_dict.copy()
print(duplicate, "\n", varied_dict)


print("4 Vaciar dictionario")
duplicate.clear()
print(duplicate)


print("5 acceder a diccionario")
integer = varied_dict["integer"]

print("especificanto la clave :integer", integer)

print("con get si no existe puedes especificar valor de regreso",varied_dict.get("extra", "no existia"))
print(varied_dict)

print("6 Valores de una lista")
value = varied_dict.values()
print(value)

print("7 obtener las claves")
key = varied_dict.keys()
print(key)

print("7 imprimor clave y valor")
for clave, valores in varied_dict.items():
    print(clave,valores)

print(varied_dict.items())


print("9 insertar valor y modificar")
varied_dict.update({"extra": "extras"})
print(varied_dict)

print("10 modificar valor")
varied_dict.update({"integer": 85})
print(varied_dict)


print("11 insertar clave y valor si no existe, si existe lo retorno, no lo edita")
varied_dict.setdefault("dobleExtra", "doble Extra")
varied_dict.setdefault("dobleExtra", "ya existe")

print(varied_dict)


# print("12 insertar clave y valor si no existe, si existe lo retorno, no lo edita")
# varied_dict = {** varied_dict, **{"tripleExtra","Triple Extra"}}  # destructurizar
# print(varied_dict)

print("13 Editar clave")
varied_dict["INTEGER"] = varied_dict.pop("integer")
print(varied_dict)

print("14 retornar un diccionario de los valores declarados")
campo = ["keys", "keys2"]
valor = ""
nuevo_diccionario = varied_dict.fromkeys(valor, campo)

print(nuevo_diccionario)
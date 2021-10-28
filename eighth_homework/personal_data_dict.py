personal_data={
    "Nombre" : "Jonathan",
    "Apellido paterno" : "Picazo",
    "Apellido materno" : "Cortez",
    "Edad":"31" 
}

print("Buenas tardes estos son sus datos personales")
for key in personal_data.keys():
    print(key, ": ", personal_data[key])

nationality = input("agregue su nacionalidad: ")
personal_data.setdefault("Nacionalidad",nationality)

print("\n Datos actualizados")
for key in personal_data.keys():
    print(key, ": ", personal_data[key])
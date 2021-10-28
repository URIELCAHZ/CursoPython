names =["Guadalupe Mendez", "Sergio Clara", "Alfredo Carbaja", "Brianda Lizeht", "Ivan Mauricio", "Alfredo Robledo", 
       "Jonathan Cortez", "Mauricio Gonzales", "Karen Moncerrat", "Belen Rosales"]

records = {}
# obtener la primera letra en un for
for name in names:
    #verificar si existe la letra y  agregar a la lista
    if name[0] in records:
       records[name[0]].append(name) 
    else:
        records[name[0]] = [name]
    
for key in records:
   print(key,": ", records[key])
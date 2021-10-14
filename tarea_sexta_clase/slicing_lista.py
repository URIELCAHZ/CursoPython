marcas=[ "Nissan", "General Motors", "Volkswagen", "Toyota", "KIA", "Mazda", "Chrysler", "Honda","Hyundai", "Ford", "Fiat", "Audi", "JAC", "BMW"]

print("primeros", marcas[:4])
print("ultimos", marcas[-3:])

x=int((len(marcas)/2)-1)
y=x + 3
print("elementos de la mitad", marcas[x:y])
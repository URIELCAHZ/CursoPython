#4.1
invitados=["Carl Sagan", "Niel deGrasse Tyson", "Lynn Margulis", "Isaac Asimov"]
for x in invitados:
    print(f"Es un placer invitarlo a celebrar con buena comida y pasar un bien tiempo en honor a la difusión de la ciencia, nos acompañaria {x}? ")

#4.2
invitado_sustituto= "Nikola Tesla"
print(f"\nLamentamos mecionar que {invitados.pop(1)} no nos podra acompañar en la cena, su lugar lo tomara {invitado_sustituto}")
invitados.insert(1,invitado_sustituto)

print(f"\nLos espero con gusto y sé qué tendrán una cena maravillosa con {invitados}\n")


# 4.3  Agrega 3 nuevos invitados a tu cena, agrega a uno de ellos al inicio, otro a la mitad y al tercero al final de la lista. Al final muestra los mensajes de invitacion para todos los invitados.

invitados_extra= ["Guadalupe Mendez", "Sergio Clara", "Alfredo Carbaja"]
for x in invitados_extra:
  print(f"Tenemos el privilegio de conseguir una mesa más grande para cenar en honor a la difusión de la ciencia, " + 
        f"por lo que nos complace poder invitarte: {x} ")

invitados.insert(0, invitados_extra[0])
invitados.append(invitados_extra[2])       
invitados.insert((int(len(invitados)/2)), invitados_extra[1] )

print()
for x in invitados:
    print(f"{x} será un placer tenerte en nuestra cena, espero disfrutes la comida y disfrutes el tiempo juntos")

# 4.4  
print()
while  2 != len(invitados):
    print(f"{invitados.pop()} lamentamos informarle que debido a problemas de reservación solo se podrá tener dos invitados y tendremos que cancelar su invitación")

print()
for x in invitados:
    print(f"Debido a problemas de reservacion, solo se tendra a dos invitados y nos complace informarle {x}, qué eres uno de ellos ")

print()
i=0
while i < len(invitados):
    print(f"Buenos días {invitados[i]}, ¿que te pareció la cena? ") 
    i+=1   

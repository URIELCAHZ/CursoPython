cumple_dia = 20
cumple_mes = "abril"

print ("Adivina mi cumpleaños")

while True:
  dia = input("ingresa el dia, solo numeros enteros:")
  dia = dia.strip()
  if not dia.isdecimal():
    print(dia, "no es un numero entero, vuelve a intentar")
    continue
  break

while True:
    mes = input("ingresa el mes, solo letras del alfabeto (a-z):")
    mes = mes.strip()
    if not mes.isalpha():
        print(mes, "no son letras del alfabeto (a-z)")
        continue
    break

dia = int(dia)
mes= mes.lower()

if dia == cumple_dia and mes == cumple_mes: 
    print("Ese es justamente mi cumpleaños ", cumple_dia, cumple_mes)
   
else: 
    print(dia, mes, "No es mi cumpleañs")
palindromo = input("Ingresa tu palindromo: ")
palindromo_invertido = ""

for x in range((len(palindromo)-1),-1,-1 ): 
 
 palindromo_invertido += palindromo[x]


if palindromo_invertido == palindromo: print(f"\' {palindromo}\'Si es un palindromo")
else: 
    print(f"No es un palindromo: \'{palindromo}\' es diferente a \'{palindromo_invertido}\'")
    print("esta prueba es sensible a mayusculas y minusculas")
    
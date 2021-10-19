numeros_primos=[2]
print(numeros_primos)
# x son los numeros a revisar
for x in range(2,1001):
 es_primo = True
 
 for primos in numeros_primos:
     if x%primos==0 : es_primo = False

 if es_primo : numeros_primos.append(x)

print(numeros_primos)

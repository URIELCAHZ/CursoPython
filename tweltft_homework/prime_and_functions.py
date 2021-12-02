
# 	a - es_divisor(a, b) : Una funcion que reciba como parametro 2 enteros y retorne True cuando 'a' pueda dividir 'b'
def es_divisor(dividendo,divisor):
    
    if dividendo%divisor: return False

    return True

# 	b - es_primo(x): Una funcion que reciba un entero x que retorne True cuando x es un numero primo y False cuando no

def es_primo(numero):

    numeros_primos = [2]
    for x in range(3,numero +1,2):
      es_primo = True
      
      for num_primo in numeros_primos:
          if es_divisor(x,num_primo) : es_primo = False

      if es_primo : numeros_primos.append(x)

    # print(numeros_primos)  
    if numero == numeros_primos[-1]: return (True , numeros_primos)

    return (False , numeros_primos)


# 	c - genera_primos(inicio, fin): Una funcion que reciba un rango (inicio y fin) y retorne una lista con los numeros primos que existan en el rango definido.
def genera_primos(incio , ultimo):

    lista_num_primos = [x for x in range(incio, ultimo + 1) if es_primo(x)[0]]
   
    return lista_num_primos


def segundo_generador_primos(inicio,ultimo):

    list_num_primos = es_primo(ultimo)[1]
    
    for x in range(len(list_num_primos)-1 , -1 , -1):
        
        if list_num_primos[x] >= inicio: continue

        list_num_primos=list_num_primos[x+1:]
        break
    return list_num_primos




print(genera_primos(105,2054))
print("\n")
print(segundo_generador_primos(105,2054))
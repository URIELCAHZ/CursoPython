
def factorial(numero):
    x = 1
    for i in range( 1 , numero + 1):
        x *= i
    
    return x


def segundo_factorial(numero):
    if numero == 1: return 1
    numero *= segundo_factorial( numero - 1)

    return numero



print( factorial(10) )

print(segundo_factorial(10))
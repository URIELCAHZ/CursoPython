
def factorial(numero):
    x = 1
    for i in range( 1 , numero + 1):
        x *= i
    
    return x


print( factorial(10) )
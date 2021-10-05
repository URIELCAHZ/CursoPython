# 5.1 -  
lugares=["Skógafoss", "Reykjavik", "Bremen", "Moscu", "Edimburho", "Inverness"]
print("\nlista de lugares original", lugares)
print("impresion con orden alfabetico", sorted(lugares)) #lista ordenada alfabeticamente
print("comprobando que no se modifico", lugares)  #lista sin modificar
# 5.2 
print("\nimprimiendo en orden alfabetico invertido", sorted(lugares,reverse=True)) #reverse=true para invertir el orden alfanumerico
print("comprobando que no se modifico", lugares)
# 5.3 
lugares.reverse()
print("\nComprobando que se invirtio la lista", lugares)
# 5.4 - 
lugares.reverse()
print("\nComprobando que se invirtio la lista a su acomodo inicial", lugares)
# 5.5 
lugares.sort()
print("\nComprobando que se modifico el orden alfanumericamente", lugares)
# 5.6 - Nuevamente utiliza el metodo sort para ordenar la lista en orden inverso (Por ejemplo: "Viena", "Paris", "Nueva York" ...).
lugares.sort(reverse=True)
print("\nComprobando que se modifico el orden alfanumericamente inverso", lugares)
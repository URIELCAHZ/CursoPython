#6.1
al_diez = list(range(0,11))

print(al_diez)

#6.2
for x in range(len(al_diez)):
    al_diez.append(al_diez.pop((x*-1)-1))   
 
print(al_diez) 

#6.3
invertir_denuevo=[al_diez[(x*-1)-1] for x in range(len(al_diez))]
print("nueva lista a base de invertir la original invertida\n",invertir_denuevo)
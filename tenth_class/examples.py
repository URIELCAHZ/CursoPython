text="texto en el cual se buscaran las letras y se cuenten las letras"


def cont_letter(text1):
    

    ocurrences={}
    for chart in text1:
        if chart in ocurrences:
            ocurrences[chart] += 1
        else:
            ocurrences [chart] = 1
    
    return ocurrences

def cont_one_letter():

    global text
    letter = input("Que letra desea buscar? ")
    cont = 0

    for chart in text:
        if chart == letter: cont +=1
            

    return cont


print(cont_letter(text))

print(cont_one_letter())

from restaurant_class import Restaurant

restaurantes = []

def add_restaurant(name, cuisine_type):
    restaurantes.append( Restaurant(name, cuisine_type))
    
    
add_restaurant("Olive", "Italiana")

add_restaurant("Das kleine Mädchen", "Alemana")

add_restaurant("Don Bigotes", "Mexicana")

for x in restaurantes:
    x.restaurant_description()

class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.open = False

    def restaurant_description(self):
        print( f"El restanrante {self.name} le servira esquisita comida {self.cuisine}")

    def open_restaurant(self):
        self.open = True
        print("El restaurante se encuentra abierto")

    def close_restautant(self):
        self.open = False
        print("El restaurante se encuetra cerrado")

    # def __repr__(self) -> str:
    #     return f"El restanrante {self.name} le servira esquisita comida {self.cuisine}, y el restauran esta open = {self.open}"
       
    def __str__(self) -> str:
        return f"El restanrante {self.name} le servira esquisita comida {self.cuisine}, y el restauran esta open = {self.open}"


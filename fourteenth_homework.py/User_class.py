from typing import AsyncGenerator


class Usuario:
    def __init__(self, firts_name, last_name) -> None:

        self.first_name = firts_name
        self.last_name = last_name
        self.age = None
        self.address = None
        self.phone_number = None
        self.gender = None

    def describe_user(self):
        print("Estos son los datos del usuario ")
        print(f"""Nombre completo: {self.first_name} {self.last_name}
        edad: {self.age}
        domicilio: {self.address}
        numero de telefono: {self.phone_number}
        genero: {self.gender} """)
        
    def get_user(self):
        print(f"Bienvenido {self.first_name}, es bueno tenerte de regreso")

    def complete_data(self, age, address, phone_number, gender):
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.gender = gender


usuarios = []

def complite_register(user_numb):
    edad = int( input("Cual es su edad? "))
    direccion = input("Cual es su direccion? ")
    numero_de_telefono = input("Cual es tu numero de telefono? ")
    genero = input("Cual es tu genero? ")
    usuarios[user_numb].complete_data(edad, direccion, numero_de_telefono, genero)
 

def new_user():
    first_name = input("Cual es tu primer nombre: ")
    last_name = input("Cual es tu apellido: ")

    usuarios.append( Usuario(first_name, last_name))

    complite_data = input("Desea completar todo el registro? -> Y para si / Cualquier otro dato para No ")

    complite_register(len(usuarios) - 1) if complite_data == "Y" else print("puedes completar tu registro despues")
    
 

new_user()

print()
usuarios[0].get_user()
print()
usuarios[0].describe_user()
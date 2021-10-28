records ={
"Guadalupe":"123456789", 
"Sergio" : "abcdefg",
"Alfredo":"hijklmn", 
"Brianda":"opqrst",
"Ivan":"",
"Alfonso":"xyz",
"Jonathan":"a1s2d3",
"Mauricio":"x9c8v7",
}

user = input("ingrese su usuario: ")
user= user.lower().title()

password= input("ingrese su contraseña: ")

if  user in records and password == records[user]:
    print("Bien venido, es bueno tenerte de regreso", user)
else:
    print("tu contraseña o usuario son incorrectas, adios")

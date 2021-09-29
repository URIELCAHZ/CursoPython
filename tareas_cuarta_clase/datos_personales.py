print("\nIngrese los datos que se le solicitan\n")

nombre=input("Nombre: ")
edad=input("Edad: ")
telefono=int(input("Telefono: "))
direccion=input("Direccion: ")
email=input("Email: ")
pais=input("Pais: ")

print(f"\nHola {nombre} consideramos que con tu edad: {edad} disfrutaras de nuestro producto, el envío se realizara a {direccion}, los "+
      f"paquetes tarda una semana en llegar a {pais} mas el tiempo que pueda estar en aduana, tu numero de guia sera enviado al " +
      f"numero de telefono {telefono} y al correo {email}, que difrutes tu día y gracias por tu compra")
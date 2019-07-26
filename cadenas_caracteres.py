saludo = "Hola a todos los presentes, "
bienvenida = "y bienvenidos a un workshop mas de Nodeschool"

mensaje = saludo + bienvenida
print("Saludo y bienvenida: ", mensaje)

ciudad = "Villahermosa"
print("La palabra '{palabra}', tiene {caracteres} caracteres".format(
   palabra = ciudad,
   caracteres = len(ciudad)
   )
)

clave = "      AB003         "
print("Clave sin strip: ", clave)
print("Clave con strip: ", clave.strip())

equipoA = "America"
equipoB = "Tigres"

print("Todo mayusculas: ", equipoA.upper())
print("Todo minuscula: ", equipoB.lower())

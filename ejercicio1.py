import math

#Cuadrado
lado = 20
area_cuadrado = lado * lado
#area_cuadrado = pow(lado, 2)

mensaje_cuadrado = """
   El area del cuadrado de lado {lado}cm es igual a {area_cuadrado}cm2
""".format(
   lado = lado,
   area_cuadrado = area_cuadrado
)

print(mensaje_cuadrado)


base = 5.90
altura = 15.75
area_triangulo = round((base * altura) / 2, 2)
print(area_triangulo)

import math
print("Si fuera una esfera")
pi = math.pi
radio = 100
volumen_esfera = round(4 * (pi * pow(radio, 3)) / 3, 2)
print(volumen_esfera)
print("Si fuera un circulo")
area_circulo = pi * (radio * radio)
print(area_circulo)
import math
datos = []
producto = {
   "clave": "AB014",
   "nombre": "Aceite Comestible 50ml",
   "precio": 25.50,
   "marca": "Capullo"
}
producto2 = {
   "clave": "AB015",
   "nombre": "Aceite No Comestible 50ml",
   "precio": 45.50,
   "marca": "Bardhall"
}
#Agregar producto
datos.append(producto)
datos.append(producto2)
print(datos)

#Eliminar producto
# En este caso el producto con clave "AB014"
for indice, producto in enumerate(datos):
   if producto["clave"] == "AB014":
      datos.pop(indice)

print(datos)


#Editar producto
# En este caso el producto con clave "AB015" precio 100
for indice, producto in enumerate(datos):
   if producto["clave"] == "AB015":
      producto["precio"] = 100.00

print(datos)

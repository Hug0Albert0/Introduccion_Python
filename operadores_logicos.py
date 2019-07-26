print("Comprendiendo operadores lógicos")

edad_pablo = 12
edad_karla = 26

print(edad_pablo > edad_karla) #False
print(edad_pablo < edad_karla) #True
print(edad_pablo == edad_karla) #False
print(edad_pablo != edad_karla) #True
print(edad_pablo >= edad_karla) #False
print(edad_pablo <= edad_karla) #True


print("Comprendiendo and, or y not")

if edad_pablo > 18 and edad_karla > 18:
   print("Ambos son mayores de 18 años")
elif edad_pablo > 18 or edad_karla > 18:
   print("Al menos uno es mayor de 18 años")
elif edad_pablo < 18 and edad_karla < 18:
   print("Ninguno es mayor de 18 años")


verde = True
rojo = False

if not rojo:
   print("Puede pasar")
if not verde:
   print("No puede pasar")

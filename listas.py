print("Listas")

lista = ["1995", "1989", "2007", "1996", "1969", "1955", "2018", "2017"]
print("Lista: ", lista)
print("Numero de elementos: ", len(lista))
lista.sort()
print("Lista ordenada: ", lista)
lista.reverse()
print("Lista en reversa: ", lista)
lista.append("2019")
print("Lista con 2019 insertado", lista)
print(lista.index("1995"))
print("Indice 6 de la lista: ", lista[6])
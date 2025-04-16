# Conversión de lista a conjunto para eliminar duplicados
lista = [1, 2, 2, 3, 4, 4, 5]
conjunto_desde_lista = set(lista) #set agarra una lista y la transforma en conjunto, por ende si tiene repetidos, los elimina.
print("Lista original:", lista)
print("Lista convertida en conjunto (sin duplicados):", conjunto_desde_lista)

#agregar un elemento en el conjunto conjunto_desde_lista
conjunto_desde_lista.add(6) #agrega el 6 al conjunto
print("Conjunto después de agregar un elemento:", conjunto_desde_lista)
conjunto_desde_lista.add(6)
print("Conjunto después de intentar agregar un duplicado:", conjunto_desde_lista) #no se agrega el 6 porque ya estaba
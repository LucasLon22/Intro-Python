# LIST - crea una lista
# LEN - cuenta la cantidad de elementos de una lista (seria como el .length)
# APPEND - agrega un elemento a la lista
# INSERT - agrega un elemento a la lista en el indice especificado
# EXTEND - agrega varios elementos a la lista
# POP - elimina un elemento de una lista y pide indice y devuelve valor
# REMOVE - remueve un elemento de la lista, pide valor
# CLEAR - elimina todo los elementos de una lista
# SORT - ordena una lista de forma ascendente o desd
# REVERSE - invierte los elementos de una lista


# list
# lista = list(["lucas", 5])
# print(lista)

#len
# profesores = list(["lucas", "yolanda", "COlo"])
# cuantos = len(profesores)
# print(cuantos)

# APPEND
# profesores = list(["lucas", "yolanda", "COlo"])

# agregar = profesores.append("Gabriel")

# print(profesores)

# EXTEND
# profesores = list(["lucas", "yolanda", "COlo"])

# extender = profesores.extend("Gabriel")

# print(profesores)

#insert
# profesores = list(["lucas", "yolanda", "COlo"])

# insertar = profesores.insert(2, "gian")
# print(profesores)

#extends 

# profesores = list(["lucas", "yolanda", "COlo"])

# extender = profesores.extend([2, "gian"]) #tengo que agregar los [] sino no me lo toma, ya que es como agregar una lista dentro de otra lista
# print(profesores)

#pop elimina por su indice
# profesores = list(["lucas", "yolanda", "COlo"])

# insertar = profesores.pop(-1) #si pongo -1 se elimina el ultimo elemento de la lista, -2 para eliminar el anteultimo y asi viceversa
# cuantos = len(profesores)
# print(profesores)
# print(cuantos)

#remove
# profesores = list(["lucas", "yolanda", "COlo"])

# remover = profesores.remove("yolanda")
# cuantos = len(profesores)
# print(profesores)
# print(cuantos)

#clear el nazi
# profesores = list(["lucas", "yolanda", "COlo"])
nuevaLista = list([1, 2, 3, 5])
remover = nuevaLista.sort()
cuantos = len(nuevaLista)
print(nuevaLista)
print(cuantos)

#reverse
nuevaLista = list([1, 2, 3, 5])
remover = nuevaLista.reverse()
cuantos = len(nuevaLista)
print(nuevaLista)
print(cuantos)

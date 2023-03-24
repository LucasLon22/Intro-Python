# diccionarios es como un array

#keys() devuelve las claves si no encuentra el programa separa
#get() devuelve el valor de una clave, si no encuentra no se detiene el programa simplemente larga una excepcion
#clear() elimina todos los elementos
#pop() elimina un determinado elemento
#items() para iterar el dic, es decir me devuelve el mismo diccionario
diccionario = {
    "nombre": "lucas",
    "edad": 30,
    "pelo": "castaño"
}

# claves = diccionario.keys()

# claves = diccionario.get("nombre")
# claves = diccionario.clear()
# claves = diccionario.pop("edad")
claves = diccionario.items()
print(claves)

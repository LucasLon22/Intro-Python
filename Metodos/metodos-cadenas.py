cadena1 = "1992"
cadena2 = "Bienvenido maquina"

#METODOS
#DIR: DEVUELVE LA LISTA DE ATRIIBUTOS VALIDOS DEL OBJETO PASADO, es una funcion de python
#UPPER: CONVIERTE EN MAYUSCULA
#LOWER: CONVIERTE EN MINUSCULA
#CAPITALIZE: PRIMER LETRA EN MAYUSC
#FIND:BUSCAMOS UN VALOR QUE LE PEDIMOS, si no encuentra devuelve -1
#INDEX: BUSCA LA POSICION DEL VALOR QUE BUSCAMOS, sino encuentra devuelve una excepcion
#ISNUMERIC:CONSULTA SI ALGO ES NUMERICO O ALFANUMERICO
#
# resultado = dir(cadena1) #nos devuelve todas las cosas que podemos hacer con este objeto que pasamos

resultado = cadena1.isnumeric()

print(resultado)
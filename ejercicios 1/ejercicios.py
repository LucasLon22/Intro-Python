# cursoactual = 1.5
# cursomasrapido = 2.5
# cursomaslento = 7
# promedioCursos = 4
# crudoPromedio = 5
# crudoCursoActual = 3.5


# # diferenciEnPorcentaje1 = 100 - cursoactual / cursomasrapido * 100
# # diferenciEnPorcentaje2 = int(100 - cursoactual / cursomaslento * 100)

# # diferenciEnPorcentaje3 = int(100 - cursoactual / promedioCursos * 100)



# # print(f'el curso de dalto dura un {diferenciEnPorcentaje1} % menos que el mas rapido')
# # print(f'el curso de dalto dura un {diferenciEnPorcentaje2} % menos que el mas lento')
# # print(f'el curso de dalto dura un {diferenciEnPorcentaje3} % menos que el promedio de los cursos')


# # porcentaje = 100 - promedioCursos / crudoPromedio * 100
# # porcentaje2 = int(100 - cursoactual / crudoCursoActual * 100)


# queda ejercicio 2

diga = input("Deci cualquier texto capo: ")

metodoSplit = diga.split()

qPalabras = (len(metodoSplit))*0.5
qPalabrasDalto = (len(metodoSplit))*0.35

print(f'la cantidad de segundos que tardaria una persona en decir {len(metodoSplit)} palabras seria de {qPalabras} segundos')
if(qPalabras > 60):
    print("para flaco tampoco te pedi un testamento")

print(f'dalto tarda en decir {len(metodoSplit)}  palabras {qPalabrasDalto} segundos')






# # print(f'el porcentaje de material inservible es del {porcentaje} %')
# # print(f'el porcentaje de material inservible es del {porcentaje2} %')

# equiv1 = int((promedioCursos / cursoactual / 10) *100)
# equiv2 = int((cursomaslento / cursoactual / 10) * 100)

# equiv3 = int((cursoactual / promedioCursos / 10) * 100)


# print(f'ver 10 horas del curso de dalto equivalen a {equiv1} horas del curso mas rapido')
# print(
#     f'ver 10 horas del curso de dalto equivalen a {equiv2} horas del curso mas rapido')
# print(
#     f'ver 10 horas del curso de dalto equivalen a {equiv3} horas del curso mas rapido')


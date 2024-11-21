print("Programa para definir si el estudiante aprueba la materia según su promedio, igrese las 3 notas entre 0 y 5")
n1 = float(input("Por favor ingrese la nota #1 del estudiante: "))
if  n1 >= 0 and n1 <= 5:
    n2 = float(input("Por favor ingrese la nota #2 del estudiante: "))
else:
    print("Por favor introduzca un valor correcto.")
if n2 >= 0 and n2 <= 5:
    n3 = float(input("Por favor ingresa la nota #3 del estudiante: "))
else:
    print("Por favor introduzca un valor correcto.")
if n3 >= 0 and n3 <= 5:
    prom = (n1+n2+n3)/3
    print("Su promedio es: ",prom)
    if prom >= 3:
        print('Aprobó.')
    else:5
    print('Reprobó')
else: print('Por favor indtroduzca un valor correcto.')
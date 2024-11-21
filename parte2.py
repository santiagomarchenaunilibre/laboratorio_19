#Bucle While
n = int(input("Cuantos empleados tiene la empresa: "))
x = 1
conta1 = 0
conta2 = 0
gastos = 0

while x <= n:
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    if sueldo <= 3000000:
        conta1 = conta1+1
    else:
        conta2 = conta2+1 
    gastos = gastos+sueldo
    x = x+1 
print("La cantidad de empleados que gana menos de 3 millones es: ",conta1)
print("La cantidad de empleados que ganan mas de 3 millones es: ",conta2)
print("El gasto total es: ",gastos)

#Bucle For
cant1 = 0
cant2 = 0
cant3 = 0
cant4 = 0
n = int(input("Cantidad de puntos: "))
for f in range(n):
    x = int(input("Ingrese coordenada x: "))
    y = int(input("Ingrese coordenada y: "))
    if x>0 and y>0:
        cant1 = cant1+1 
    else:
        if x<0 and y>0:
            cant2 = cant2+1 
        else:
            if x<0 and y<0:
                cant3 = cant3+1 
            else:
                if x>0 and y<0:
                    cant4 = cant4+1 
print("Cantidad de puntos en el primer cuadrante: ", cant1)
print("cantidad de puntos en el segundo cuadrante: ",cant2)
print("Cantidad de puntos en el tercer cuadrante: ",cant3)
print("Cantidad de puntos en el cuarto cadrante: ",cant4)
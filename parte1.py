#Determinar si el número es par o impar.
numero = int(input("Ingrese un número: "))
if numero %2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

#Cantidad de dígitos
numero = int(input("Ingrese un número de: 0 a 999: "))
if numero < 10:
    print("El número",numero,"tiene 1 dígito.")
elif numero >= 10 and numero < 100:
    print("El número",numero,"tiene 2 dígitos.")
else:
    print("El número",numero,"tiene 3 dígitos.")

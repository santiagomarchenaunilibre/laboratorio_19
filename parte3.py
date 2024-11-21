#calificaciones
calificaciones={
    "pedro":4.7,
    "paco":3.5,
    "luis":5.0,
}
nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")
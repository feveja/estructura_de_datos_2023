estudiantes = {}  # Diccionario para almacenar la información de los estudiantes

# Ingresar información de los estudiantes
for i in range(3):
    nombre = input("Ingrese el nombre del estudiante: ")
    asignatura = input("Ingrese el nombre de la asignatura: ")
    lab1 = float(input("Ingrese la nota del Laboratorio N°1: "))
    lab2 = float(input("Ingrese la nota del Laboratorio N°2: "))
    
    # Calcular el promedio ponderado
    promedio = (lab1 * 0.3) + (lab2 * 0.7)
    
    # Guardar la información en el diccionario
    estudiantes[nombre] = {
        'Asignatura': asignatura,
        'Laboratorio 1': lab1,
        'Laboratorio 2': lab2,
        'Promedio Ponderado': round(promedio, 1)  # Redondear a 1 decimal
    }

# Mostrar la información ingresada
for nombre, info in estudiantes.items():
     'Asignatura': asignatura,
        'Laboratorio 1': lab1,
        'Laboratorio 2': lab2,
        'Promedio Ponderado': round(promedio, 1)

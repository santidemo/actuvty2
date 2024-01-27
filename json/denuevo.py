import json

def guardar_datos(alumnos):
    with open('datos_alumnos.json', 'w') as archivo:
        json.dump(alumnos, archivo)

def cargar_datos():
    try:
        with open('datos_alumnos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def muestra_alu(alu):
    print(f"Datos del alumno:")
    print(f"Nombre: {alu['Nombre']}")
    print(f"Apellido: {alu['Apellido']}")
    print(f"DNI: {alu['DNI']}")
    print(f"Fecha de nacimiento: {alu['Fecha de nacimiento']}")
    print(f"Tutor: {alu['Tutor']}")
    print(f"Notas: {alu['Notas']}")
    print(f"Faltas: {alu['Faltas']}")
    print(f"Amonestaciones: {alu['Amonestaciones']}")

def all_alu(alumnos):
    for i in range(len(alumnos)):
        print(f"Datos del alumno {i + 1}:")
        print(f"Nombre: {alumnos[i]['Nombre']}")
        print(f"Apellido: {alumnos[i]['Apellido']}")
        print(f"DNI: {alumnos[i]['DNI']}")
        print(f"Fecha de nacimiento: {alumnos[i]['Fecha de nacimiento']}")
        print(f"Tutor: {alumnos[i]['Tutor']}")
        print(f"Notas: {alumnos[i]['Notas']}")
        print(f"Faltas: {alumnos[i]['Faltas']}")
        print(f"Amonestaciones: {alumnos[i]['Amonestaciones']}")

def modificar_datos_alumno(alumnos, indice_alumno, nuevo_nombre, nuevo_apellido, nueva_fecha_nacimiento,
                           nuevo_tutor, nuevas_notas, nuevas_faltas, nuevas_amonestaciones):
    alumno = alumnos[indice_alumno]
    alumno["Nombre"] = nuevo_nombre
    alumno["Apellido"] = nuevo_apellido
    alumno["Fecha de nacimiento"] = nueva_fecha_nacimiento
    alumno["Tutor"] = nuevo_tutor
    alumno["Notas"] = nuevas_notas
    alumno["Faltas"] = nuevas_faltas
    alumno["Amonestaciones"] = nuevas_amonestaciones

def agregar_alumno(alumnos, nombre, apellido, dni, fecha_nacimiento, tutor, notas, faltas, amonestaciones):
    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }
    alumnos.append(nuevo_alumno)

def expulsar_alumno(alumnos, indice_alumno):
    if 0 <= indice_alumno < len(alumnos):
        alumno_expulsado = alumnos.pop(indice_alumno)
        print(f"Se ha expulsado al alumno {alumno_expulsado['Nombre']} {alumno_expulsado['Apellido']}.")
    else:
        print("No se encontró el índice.")

def cuerpo():
    # Cargar datos al inicio del programa
    alumnos = cargar_datos()

    while True:
        print("Menú:")
        print("a Mostrar datos de un alumno")
        print("b Mostrar datos de todos los alumnos")
        print("c Modificar datos de un alumno")
        print("d Agregar un nuevo alumno")
        print("e Expulsar un alumno")
        print("sali: Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            indice = int(input("Ingrese el índice del alumno (empezando desde 1): ")) - 1
            muestra_alu(alumnos[indice])
        elif opcion == "b":
            all_alu(alumnos)
        elif opcion == "c":
            indice = int(input("Ingrese el índice del alumno a modificar (empezando desde 1): ")) - 1
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_apellido = input("Ingrese el nuevo apellido: ")
            nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento: ")
            nuevo_tutor = input("Ingrese el nuevo tutor: ")
            nuevas_notas = input("Ingrese las nuevas notas (separadas por comas): ").split(",")
            nuevas_faltas = int(input("Ingrese la nueva cantidad de faltas: "))
            nuevas_amonestaciones = int(input("Ingrese la nueva cantidad de amonestaciones: "))
            modificar_datos_alumno(alumnos, indice, nuevo_nombre, nuevo_apellido, nueva_fecha_nacimiento,
                                   nuevo_tutor, nuevas_notas, nuevas_faltas, nuevas_amonestaciones)
        elif opcion == "d":
            nombre = input("Ingrese el nombre del nuevo alumno: ")
            apellido = input("Ingrese el apellido del nuevo alumno: ")
            dni = input("Ingrese el DNI del nuevo alumno: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del nuevo alumno: ")
            tutor = input("Ingrese el nombre y apellido del tutor del nuevo alumno: ")
            notas = input("Ingrese las notas del nuevo alumno (separadas por comas): ")
            faltas = int(input("Ingrese la cantidad de faltas del nuevo alumno: "))
            amonestaciones = int(input("Ingrese la cantidad de amonestaciones del nuevo alumno: "))
            agregar_alumno(alumnos, nombre, apellido, dni, fecha_nacimiento, tutor, notas, faltas, amonestaciones)
        elif opcion == "e":
            indice = int(input("Ingrese el índice del alumno a expulsar (empezando desde 1): ")) - 1
            expulsar_alumno(alumnos, indice)
        elif opcion == "sali":
            # Guardar datos antes de salir
            guardar_datos(alumnos)
            print("Programa finalizado")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

cuerpo()

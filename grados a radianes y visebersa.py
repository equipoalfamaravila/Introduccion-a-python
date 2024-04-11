import math

# Función para convertir de grados a radianes
def grados_a_radianes(grados):
    radianes = math.radians(grados)
    return radianes

# Función para convertir de radianes a grados
def radianes_a_grados(radianes):
    grados = math.degrees(radianes)
    return grados

# Menú de selección
while True:
    print("\\n1. Convertir grados a radianes")
    print("2. Convertir radianes a grados")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        grados = float(input("Ingrese los grados: "))
        print(f"{grados} grados es igual a {grados_a_radianes(grados)} radianes.")
    elif opcion == 2:
        radianes = float(input("Ingrese los radianes: "))
        print(f"{radianes} radianes es igual a {radianes_a_grados(radianes)} grados.")
    elif opcion == 3:
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")

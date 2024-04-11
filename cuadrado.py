# Este algoritmo dibuja un cuadrado con asteriscos.
N = int(input("Escribe la dimensión N>= 2 del cuadrado a dibujar: "))
# Escribe la primera línea de asteriscos
for i in range(N):
    print("* ", end="")
print()  # Salto de línea

# Dibuja las partes laterales
for j in range(N - 2):
    print("*", end=" ")  # Asterisco inicial
    for k in range(N - 2):
        print(" ", end=" ")  # Espacios interiores
    print("*")  # Asterisco final

# Dibuja la última línea de asteriscos
for i in range(N):
    print("* ", end="")
print()  # Salto de línea

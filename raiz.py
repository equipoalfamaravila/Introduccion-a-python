x = 1.0 # Inicializamos x a la unidad.
a = float(input("Dame el valor de a:\n"))
# Se inicia el cálculo de la raíz de a.
for k in range(1, 10):
    x = (x + a/x)/2
print("La raíz después de", k, "iteraciones es ", x)

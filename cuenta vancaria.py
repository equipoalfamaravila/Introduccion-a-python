# Intereses de una cuenta bancaria
capital = float(input("capital inicial: "))
tea = float(input("tasa efectiva anual: "))
n = int(input("numero de dias: "))

float_Intereses = (((1+tea)**(n/360)-1))*capital
print("el interes es", float_Intereses)

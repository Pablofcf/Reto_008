# Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

n = int(input("Digite el valor de n: "))
x = float(input("Digite el valor de x: "))
resultado = 1.0
for _ in range(n):
    resultado *= x
print(f"{x} elevado a la potencia {n} es {resultado}")
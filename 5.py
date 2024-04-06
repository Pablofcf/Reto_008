#Calcular el valor de 2 elevado a la potencia n usando ciclos for.

n = int(input("Ingrese numero de potencia para el numero 2: "))
i:int=2
potencia:int=0
for i in range(1, n+1):
 potencia=i**2
 print("El resultado es " + str(potencia)) 
#Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

n= int(input("Ingrese la tabla de multiplicar que quiere saber: "))
multiplicacion:int=0
for i in range (1,11):
 multiplicacion=i*n
 print("Las tabla de " + str(n) + " es " + str(multiplicacion)) 
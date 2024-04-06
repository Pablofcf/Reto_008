#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

n=int(input("ingrese un numero"))
for i in range(-n,-2): 
   if i % 2 ==0:
    print("El número es: " + str(-i) )  

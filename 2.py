#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000..

for i in range(1,1000):
   if i % 2 !=0:
     print("El número impar es: " + str(i) )  
for i in range(2,1001):
   if i % 2 ==0:
     print("-El número par es: " + str(i) )  
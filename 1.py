#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

cuadrado:int=0
for i in range(1,101):
    cuadrado=i**2
    print("El número es: " + str(i) + " y su cuadrdo es " + str(cuadrado))  
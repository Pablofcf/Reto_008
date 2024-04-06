# Reto_008
1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
cuadrado:int=0
for i in range(1,101):
    cuadrado=i**2
    print("El número es: " + str(i) + " y su cuadrdo es " + str(cuadrado))  
```

2.Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000..
```python
for i in range(1,1000):
   if i % 2 !=0:
     print("El número impar es: " + str(i) )  
for i in range(2,1001):
   if i % 2 ==0:
     print("-El número par es: " + str(i) )  
```

3.Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
n=int(input("ingrese un numero"))
for i in range(-n,-2): 
   if i % 2 ==0:
    print("El número es: " + str(-i) )  
```

4.Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
n=int(input("ingrese un numero"))
factorial:int=1
for i in range(1,n+1): 
 factorial *= i
 print("El factorial del numero  " + str(i) +  " es "   + str(factorial)) 
```

5.Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```python
n = int(input("Ingrese numero de potencia para el numero 2: "))
i:int=2
potencia:int=0
for i in range(1, n+1):
 potencia=i**2
 print("El resultado es " + str(potencia)) 
```

6.Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```python
n = int(input("Digite el valor de n: "))
x = float(input("Digite el valor de x: "))
resultado = 1.0
for _ in range(n):
    resultado *= x
print(f"{x} elevado a la potencia {n} es {resultado}")
```
7.Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
n= int(input("Ingrese la tabla de multiplicar que quiere saber: "))
multiplicacion:int=0
for i in range (1,11):
 multiplicacion=i*n
 print("Las tabla de " + str(n) + " es " + str(multiplicacion)) 
```

8.Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

[![image.png](https://i.postimg.cc/brc6HGX7/image.png)](https://postimg.cc/hzsbKtts)
```python
import math

def aprox_exp(x, n):
    suma = 0.0
    for i in range(n + 1):
        suma += x ** i / math.factorial(i)
    return suma
x = float(input("Digite el valor de x para calcular e^x: "))
n = int(input("Digite el numero de terminos n para la aproximacion: "))
aprox = aprox_exp(x, n)
valor_real = math.exp(x)
print(f"Aprox de e^{x} usando {n} terminos: {aprox}")
print(f"Valor real de e^{x}: {valor_real}")
print(f"Diferencia: {abs(valor_real - aprox)}")
```
9.Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

[![image.png](https://i.postimg.cc/v8rXwZwm/image.png)](https://postimg.cc/MXG1yxTk)

```python
import math

def introducir():
    #Le damos nombre a nuestras variables
    x : float = float(input("Ingrese un valor para x: "))
    y : int = int(input("Ingrese el número de términos para trabajar: "))
    desarrollo(x,y)

def desarrollo(x,y):
    serie_mc(x,y)
    #Ponemos 3 variables de resultado
    aproximacion : float
    valorReal : float
    direfencia : float
    aproximacion, valorReal, direfencia = serie_mc(x, y)
    print(f"La aproximación usando {y} términos de la serie  es: {aproximacion}")
    print(f"Valor real de la función seno: {valorReal}")
    print(f"Diferencia entre la aproximación y el valor real: {direfencia}")
    menor(x)

def serie_mc(x,y):
    #Declaramos la variable
    aproximacion : float = 0
     #repetir los terminos que se van a emplear
    for i in range(y):
        a : int = factorial_numero(2*i + 1)
        aproximacion += ((-1)*i) * (x*(2*i+1)) / a
    #calcular el valor real
    valor_real : float = math.sin(x)
    #calcular la diferencia entre los dos valores
    diferencia : float = valor_real - aproximacion
    #valor absoluto al restar los 2 valores iniciales
    diferencia_abs = diferencia if diferencia >= 0 else -diferencia
    return aproximacion, valor_real, diferencia_abs

def factorial_numero(i):
    #Variable para el valor concreto o final
    factorial : int = 1
    #se repite i veces
    for z in range(1,i+1):
        factorial *= i
        i -=1
    return factorial

def menor(x):
    #Para calcular el número de terminos necesarios para que el error sea menor al 0.1%
    m : int = 0
    #Se halla el error máximo
    error = 0.001 * math.sin(x)
    #Se repite el ciclo hasta que la diferencia sea menor al error
    while True:
        aproximacion, valorReal, direfencia = serie_mc(x, m)
        if direfencia < error:
            break
        m += 1
    print(f"¿quiere obtener un digito menor a 0.1? necesita minimo {m} términos.")
        

if __name__ == "__main__":
    print("Programa para calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros y términos de la serie de serie_mc.")
    #El programa se repeitrá hasta que el usuario lo desee
    while True:
        introducir()
        break
```

10.Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

[![image.png](https://i.postimg.cc/DfBj4NWd/image.png)](https://postimg.cc/jCnQGZ4L)


Disclaimer: Para las aproximaciones de series determine con que valor n se obtiene menos del 0.1% de error.

```python
import math

def introducir():
    #Le damos nombre a nuestras variables
    x : float = float(input("Ingrese un valor para x en un rango entre -01 , 0.1: "))
    y : int = int(input("Ingrese el número de términos para trabajar: "))
    desarrollo(x,y)

def desarrollo(x,y):
    serie_mc(x,y)
    #Ponemos 3 variables de resultado
    aproximacion : float
    valorReal : float
    direfencia : float
    aproximacion, valorReal, direfencia = serie_mc(x, y)
    print(f"La aproximación usando {y} términos de la serie  es: {aproximacion}")
    print(f"Valor real de la función seno: {valorReal}")
    print(f"Diferencia entre la aproximación y el valor real: {direfencia}")
    menor(x)

def serie_mc(x,y):
    #Declaramos la variable
    aproximacion : float = 0
     #repetir los terminos que se van a emplear
    for i in range(y):
        a : int = factorial_numero(2*i + 1)
        aproximacion += ((-1)*i) * (x*(2*i+1)) / a
    #calcular el valor real
    valor_real : float = math.sin(x)
    #calcular la diferencia entre los dos valores
    diferencia : float = valor_real - aproximacion
    #valor absoluto al restar los 2 valores iniciales
    diferencia_abs = diferencia if diferencia >= 0 else -diferencia
    return aproximacion, valor_real, diferencia_abs

def factorial_numero(i):
    #Variable para el valor concreto o final
    factorial : int = 1
    #se repite i veces
    for z in range(1,i+1):
        factorial *= i
        i -=1
    return factorial

def menor(x):
    #Para calcular el número de terminos necesarios para que el error sea menor al 0.1%
    m : int = 0
    #Se halla el error máximo
    error = 0.001 * math.atan(x)
    #Se repite el ciclo hasta que la diferencia sea menor al error
    while True:
        aproximacion, valorReal, direfencia = serie_mc(x, m)
        if direfencia < error:
            break
        m += 1
    print(f"¿quiere obtener un digito menor a 0.1? necesita minimo {m} términos.")
        

if __name__ == "__main__":
    print("Programa para calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros y términos de la serie de serie_mc.")
    #El programa se repeitrá hasta que el usuario lo desee
    while True:
        introducir()
        break
```

#Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

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
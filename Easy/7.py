#Realiza un programa que calcule el numero factorial de un numero
#Usa arreglos
#1 2 6 24 120 720
#1 2 3  4  5   6
#0 1 2  3  4   5

print("Calcular el numero factorial de un numero")
n = int(input("Ingresa un numero: "))

def fact(n):
    array = [1]
    i = 0
    j = 2
    while i <= n:
        array.append(array[i] * j)
        i += 1
        j += 1
    return(array[n])

print(fact(n))


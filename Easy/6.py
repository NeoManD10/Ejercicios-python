#Realiza un programa que calcule el numero factorial de un numero
#Usa recursividad

print("Calcular el numero factorial de un numero")
n = int(input("Ingresa un numero: "))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(n))


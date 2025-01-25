#Escribe un programa que tome una lista de números y un valor N, e 
#imprima solo los números de la lista que sean mayores que N.

# Entrada esperada:
# Lista: [1, 5, 8, 10, 3]
# Valor: 5
# Salida esperada: 8, 10

# Solicitar al usuario que ingrese una lista de números
lista = input("Ingresa una lista de números separados por comas: ")
lista = [int(x) for x in lista.split(",")]

# Solicitar al usuario que ingrese el valor N
n = int(input("Ingresa el valor N: "))

# Filtrar los números mayores que N
numeros_mayores = [x for x in lista if x > n]

# Imprimir los números mayores que N
print("Números mayores que", n, ":", ", ".join(map(str, numeros_mayores)))


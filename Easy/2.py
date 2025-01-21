# Programa que imprime todos los números pares desde 1 hasta N

# Solicitar el número N al usuario
num = int(input("Ingrese un número: "))

# Iterar desde 1 hasta N
print(f"Números pares desde 1 hasta {num}:")
for i in range(2, num + 1, 2):  # Comenzar en 2, incrementar de 2 en 2
    print(i)

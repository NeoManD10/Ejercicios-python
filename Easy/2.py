# Programa que imprime todos los números divsibles por 3 desde 1 hasta N
#agrega comentario

# Solicitar el número N al usuario
num = int(input("Ingrese un número: "))

# Iterar desde 1 hasta N
print(f"Números divisibles por 3 desde 0 hasta {num}:")
for i in range(0, num, 3):  # comienza desde 0 hasta num , aumentando en 3 cada iteracion
    print(i)



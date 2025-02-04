# Escribe un programa que genere los primeros N números de la secuencia de Fibonacci, 
# donde N es ingresado por el usuario.

# Entrada esperada:
# Ingresa el número de términos: 6
# Salida esperada: 0, 1, 1, 2, 3, 5

numero = int(input("Ingresa un numero: "))

def fibo(numero):
    lista = [0,1]
    i = 2

    while i < numero:
        lista.append(lista[i-2] + lista[i-1])
        i += 1
    return lista

print(fibo(numero))

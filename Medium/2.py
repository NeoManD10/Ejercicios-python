#Escribe un programa que determine si un número ingresado por el usuario es primo.
#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 97...

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1): #Si un número no tiene divisores menores o iguales a su raíz cuadrada, entonces no tendrá ningún otro divisor (excepto él mismo y 1).
        if numero % i == 0: #Si retorna un resto 0 en la division no es primo
            return False
    return True 

# Solicitar al usuario un número
num = int(input("Ingrese un número: "))
if es_primo(num): # Si el resultado es true
    print(f"{num} es un número primo.")
else: # Si el resultado es false
    print(f"{num} no es un número primo.")


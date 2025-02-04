# Escribe un programa que tome una lista de números ingresada por el usuario y 
# la ordene de menor a mayor sin usar la función sorted.

# Entrada esperada:
# Ingresa una lista de números separados por comas: 5,2,9,1,5
# Salida esperada: [1, 2, 5, 5, 9]

lista = input("Ingresa una lista de números separados por comas: ")
lista = [int(x) for x in lista.split(",")]

#Usando sorted
lista_ordenada = sorted(lista)

print(lista_ordenada)

# Implementación del algoritmo de burbuja
for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            # Intercambiar elementos si están en el orden incorrecto
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("Lista ordenada de menor a mayor:", lista)
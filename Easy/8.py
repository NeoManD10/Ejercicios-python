# Algoritmo de ordenamiento Insertion Sort
array = [5, 3, 4, 8, 7, 5, 1, 2, 3]
print("Array original:", array)

for j in range(1, len(array)):
    actual = array[j]
    i = j - 1

    # Desplazar los elementos mayores hacia la derecha
    while i >= 0 and array[i] > actual:
        array[i + 1] = array[i]
        i -= 1
    
    # Insertar el elemento actual en su posición correcta
    array[i + 1] = actual

print("Array ordenado:", array)


        
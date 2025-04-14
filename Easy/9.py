#Alggoritmo de ordenamiento Burbuja

array = [5, 3, 4, 8, 7, 5, 1, 2, 3]

for i in range(len(array)):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print(array)
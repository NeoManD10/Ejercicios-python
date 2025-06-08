#Escribe un programa que tome una cadena ingresada por el usuario y la imprima al revés.

cadena = input("Ingresa una cadena: ")
arreglo = [5,8,23,1,4,99]

# Invertir la cadena
cadena_invertida = cadena[::-1] #utiliza el operador de slicing para recorrer la cadena en orden inverso.
arreglo_invertido = list(reversed(arreglo))

# Imprimir la cadena invertida
print("La cadena invertida es:", cadena_invertida)
print(f"\nEl arreglo original es: {arreglo}")
print(f"\nEl arreglo invertido es: {arreglo_invertido}")

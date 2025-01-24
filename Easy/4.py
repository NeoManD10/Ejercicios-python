#Escribe un programa que tome una cadena ingresada por el usuario y la imprima al revés.

cadena = input("Ingresa una cadena: ")

# Invertir la cadena
cadena_invertida = cadena[::-1] #utiliza el operador de slicing para recorrer la cadena en orden inverso.

# Imprimir la cadena invertida
print("La cadena invertida es:", cadena_invertida)

# Escribe un programa que verifique si una palabra ingresada por el usuario es un palíndromo 
# (se lee igual de adelante hacia atrás).

# Entrada esperada:
# Ingresa una palabra: radar
# Salida esperada: Es un palíndromo

def es_palindromo(cadena):
    #Convertir palabra a minusculas
    cadena = cadena.lower()

    if cadena == cadena[::-1]:
        return True
    else:
        return False

palabra = input("Escribe cualquier palabra (solo una palabra): ")

if es_palindromo(palabra):
    print("Es palindromo.")
else:
    print("No es palindromo.")




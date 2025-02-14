# Crea un programa que permita al usuario jugar al ahorcado. 
# El programa seleccionará una palabra aleatoria de una lista predefinida y permitirá al 
# usuario adivinar una letra a la vez. Muestra el progreso del usuario (palabra incompleta) y 
# termina cuando el usuario adivina la palabra o se queda sin intentos.

# Entrada esperada:
# Palabra: _ _ _ _ (Palabra: "casa")
# Ingresa una letra: a
# _ a _ a

import random

def elegir_palabra():
    palabras = ["montaña", "sol", "nube", "mar", "ciudad", "perro", "gato", "coche","puerta", "ventana", "cielo", "bosque", "río", "lago", "estrella","planeta", "computadora", "teléfono", "luz", "sombra", "flor", "árbol","pájaro", "tigre", "elefante", "ratón", "tren", "avión", "bicicleta","zapato", "camisa", "pantalón", "reloj", "mesa", "silla", "pared","espejo", "puente", "taza", "juguete"]
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6
    
    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra:")
    
    while intentos_restantes > 0:
        print("\nPalabra: ", mostrar_progreso(palabra, letras_adivinadas))
        letra = input("Ingresa una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya intentaste con esa letra. Prueba otra.")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra not in palabra:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")
        
        if set(palabra).issubset(letras_adivinadas):
            print("\n¡Felicidades! Has adivinado la palabra:", palabra)
            return
    
    print("\nHas perdido. La palabra era:", palabra)

if __name__ == "__main__":
    jugar_ahorcado()



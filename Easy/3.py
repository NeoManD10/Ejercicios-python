#Escribe un programa que convierta una temperatura en grados Celsius a Fahrenheit. Usa la fórmula:
# F=C×95+32F=C×59​+32.

num_grados = float(input("Ingrese un valor (en grados): "))

num_far = ((num_grados * (9/5)) + 32)

print(f"Grados en fahrenheit: {num_far}")


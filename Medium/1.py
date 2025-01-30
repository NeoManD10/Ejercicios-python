# Escribe un programa que implemente una calculadora básica con las operaciones suma, resta, 
# multiplicación y división. Permite al usuario elegir la operación.

def suma():
    print("INGRESA LOS NUMEROS A SUMAR\n")
    num1 = int(input("Numero A: "))
    num2 = int(input("Numero B: "))

    return print(f"LA SUMA DE LOS NUMEROS ES: {num1+num2}\n")

def resta():
    print("INGRESA LOS NUMEROS A RESTAR\n")
    num1 = int(input("Numero A: "))
    num2 = int(input("Numero B: "))

    return print(f"LA RESTA DE LOS NUMEROS ES: {num1-num2}\n")

def multiplicacion():
    print("INGRESA LOS NUMEROS A MULTIPLICAR\n")
    num1 = int(input("Numero A: "))
    num2 = int(input("Numero B: "))

    return print(f"LA MULTIPLICACION DE LOS NUMEROS ES: {num1*num2}\n")

def division():
    print("INGRESA LOS NUMEROS A DIVIDIR\n")
    num1 = int(input("Numero A: "))
    num2 = int(input("Numero B: "))

    if num2 == 0:
        return print("NO EXISTE.")

    return print(f"LA DIVISION DE LOS NUMEROS ES: {num1/num2}\n")

opcion = 0
while opcion != 5: #Se ejecuta mientras op sea diferente de 4
    print('1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir\n') #Muestra las opciones
    opcion = int(input('Ingresa una opcion: ')) # Usuario ingresa opcion
    
    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    elif opcion == 5:
        print('Salio...')
    else:
        print('Ingrese una opcion valida')     



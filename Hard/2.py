# Diseña un programa que simule las operaciones básicas de un cajero automático.
# Requisitos:

#    Usa un sistema basado en menús.
#    Implementa funciones para consultar saldo, retirar dinero, depositar dinero y salir.
#    Simula un saldo inicial y controla errores como:
#    Intentar retirar más dinero del saldo disponible.
#    Ingresar montos no válidos (negativos o no numéricos).

saldo_disponible = 180000

def consultar_saldo():
    print(f"\nSaldo disponible: {saldo_disponible}")
    print("----------------------------------------")
    print("\n\n")
#end def

def retirar_dinero():
    global saldo_disponible #Nos permite usar la variable global saldo disponible
    saldo_a_retirar = int(input("\n¿Cuanto dinero necesita retirar?: "))
    if saldo_a_retirar > saldo_disponible:
        print("\nLo siento, pero superaste el saldo disponible.")
        print("----------------------------------------")
        print("\n\n")
    elif saldo_a_retirar < 0:
        print("\nIngresa un monto valido. ")
        print("----------------------------------------")
        print("\n\n")
    else:
        saldo_disponible -= saldo_a_retirar
        print(f"\nSaldo retirado: {saldo_a_retirar}")
        print(f"Saldo disponible: {saldo_disponible}")
        print("----------------------------------------")
        print("\n\n")
#end def

def depositar_dinero():
    global saldo_disponible #Nos permite usar la variable global saldo disponible
    saldo_a_depositar = int(input("\n¿Cuanto dinero neecesita depositar?: "))
    if saldo_a_depositar < 0:
        print("\nIngresa un monto valido. ")
        print("----------------------------------------")
        print("\n\n")
    elif saldo_a_depositar > 1000000:
        print("\nSuperaste el límite de depósito. ")
        print("----------------------------------------")
        print("\n\n")
    else:
        saldo_disponible += saldo_a_depositar
        print(f"\nSaldo depositado: {saldo_a_depositar}")
        print(f"Saldo disponible: {saldo_disponible}")
        print("----------------------------------------")
        print("\n\n")

#end def

opcion = 0
while opcion != 4:

    print('1.Consultar saldo\n2.Retirar dinero\n3.Depositar dinero\n4.Salir\n') #Muestra las opciones
    opcion = int(input('Ingresa una opcion: ')) # Usuario ingresa opcion
    
    if opcion == 1:
        consultar_saldo()
    elif opcion == 2:
        retirar_dinero()
    elif opcion == 3:
        depositar_dinero()
    elif opcion == 4:
        print('Hasta luego...')
    else:
        print('\nIngrese una opcion valida')   
        print("----------------------------------------")
        print("\n\n")  




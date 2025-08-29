#Ejercicio 2 para practicar Python#
#Adivina el numero por computadora en python#
import random
print(f"")
print(f"")
print("===================================")
print("   Juego: Adivina el Número")
print("===================================")
print("¡Bienvenido al juego de Adivina el Número!")
print(f"")
intentosPerimitidos = input("¿Cuantos intentos deseas tener? ")
if not intentosPerimitidos.isdigit() or int(intentosPerimitidos) <= 0:
    print("Por favor, ingresa un número válido de intentos (un entero positivo).")
    exit()   
numero_secreto = 5  # Número fijo para pruebas
intentos = 0
intentosPerimitidos = int(intentosPerimitidos)
while True:
    intento = input("Adivina un número entre 1 y 100: ")
    try:
        intento = int(intento)
        intentos += 1
        if intentos > intentosPerimitidos:
            print(f"Lo siento, has excedido el número máximo de intentos. El número era {numero_secreto}.")
            break
        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")

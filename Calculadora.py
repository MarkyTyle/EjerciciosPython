#Ejercicio numero 3 para practicar Python
# Calculadora simple en Python
#Autor: Marcos Delgado
#Fecha: 2024-10-03
##
print(f"")
print(f"")
print("===================================")
print("   Calculadora Simple en Python Ejercicio 3")
print("===================================") 
print("!Bienvenido a la Calculadora Simple de Marcos!")
print(f"")
def sumar(x, y):
    return int(x) + int(y)
def restar( x,y):
    return int(x)-int(y)
def multiplicar(x, y):  
    return float(x)*float(y)

if __name__ =="__main__":
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    opcion = input("Ingresa la Opción (1, 2 o 3): ")
    if opcion in ['1', '2', '3']:
        if opcion== '1':
            print(f"")
            print("Has seleccionado Sumar. (+)")
            num1 = input("Ingresa el primer número: ")
            num2 = input("ingresa el segundo número: ")
            if not num1.isdigit() or not num2.isdigit():
                print("Ambos valores deben ser números.")
                exit()
            print(f"")
        elif opcion =='2':
            print(f"")
            print("Has seleccionado Restar. (-)")
            num1 = input("Ingresa el primer número: ")
            num2 = input("ingresa el segundo número: ")
            if not num1.isdigit() or not num2.isdigit():
                print("Ambos valores deben ser números.")
                exit()
            print(f"")
        elif opcion =='3':
            print(f"")
            print("Has seleccionado Multiplicar. (*)")
            num1 = input("Ingresa el primer número: ")
            num2 = input("ingresa el segundo número: ")
            if not num1.isdigit() or not num2.isdigit():
                print("Ambos valores deben ser números.")
                exit()
            print(f"")
        if opcion=='1':
            print(f"La suma es: {sumar(num1, num2)}")
        if opcion=='2':
            print(f"La resta es: {restar(num1, num2)}")
        if opcion=='3':
            print(f"La multiplicación es: {multiplicar(num1, num2)}")
    else:
        print("La opcion seleccionada es invalida, se encuentra fuera de rango, las opciones son: (1, 2, 3)")   

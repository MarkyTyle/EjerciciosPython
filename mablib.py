# MabLibs: Un juego sencillo para aprender Python
## autor: Marcos Delgado
## fecha: 2024-10-03
## Ejercicio numero 1 para practicar Python
def jugar_mablib():
    print(f"")
    print(f"")
    print("¡Bienvenido a MabLibs! Completa las palabras para crear una historia divertida.\n")

    nombre = input("Escribe un nombre: ")
    apellido= input("Escriba su apellido:")
    lugar = input("Escribe un lugar: ")
    objeto = input("Escribe un objeto: ")
    verbo = input("Escribe un verbo en infinitivo: ")
    adjetivo = input("Escribe un adjetivo: ")

    print("\nAquí está tu historia:\n")
    print(f"Un día, {nombre} {apellido} fue a {lugar} con su {objeto}.")
    print(f"Allí decidió {verbo} porque estaba muy {adjetivo}.")
    print("¡Fin de la historia!")
    print("\nGracias por jugar a MabLibs.")
if __name__ =="__main__":
    jugar_mablib()
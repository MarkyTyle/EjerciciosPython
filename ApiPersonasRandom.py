import requests

def CargarPersonas(cantidad):
    respuesta= requests.get(f"https://randomuser.me/api/?results={cantidad}")
    if respuesta.ok:
        data = respuesta.json()
        for i, persona in enumerate(data['results'], start=1):
            nombre = f"{persona['name']['first']} {persona['name']['last']}"
            pais = persona['location']['country']
            email = persona['email']
            username = persona['login']['username']
            pasword = persona['login']['password']
            picture = persona['picture']['medium']
            fechaNacimiento = persona['dob']['date']
            edad = persona = persona['dob']['age']
            print(f"{i}. Nombre: {nombre}, Nacimiento: {fechaNacimiento}, Edad: {edad} Pais: {pais},  Email: {email}, Username: {username}, Password: {pasword}, Foto: {picture}")
    else:
        print("\n")
        print(f"Error al obtener datos de la APi.")    

if __name__ =="__main__":
    print("################# P E R S O N A S  R A N D O M API ################")
    print("\n")
    cantidad = input("¿Cuantas personas random desea generar? \n:")
    print(f"")
if not cantidad.isdigit() or int(cantidad) <= 0:
            print("Por favor, ingresa un número válido mayor que 0.")
            exit()
CargarPersonas(cantidad)
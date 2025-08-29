import requests

def obtenerChistesRandom():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    if response.status_code == 200:
        data = response.json()
        print("\n")
        return data.get('value')
    else:
        print("Error al consumir la API")

if __name__ == "__main__":
    joke = obtenerChistesRandom()
    print('El chiste Random es: ', joke)
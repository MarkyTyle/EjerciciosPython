from fastapi import FastAPI
import requests
app = FastAPI(
    title="Fast APi Python V1.2.35",
    description="API Sencilla en Python con FastAPI",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"Bienvenido a mi API"}

@app.get("/chiste")
def obtener_chiste():
    respuesta = requests.get("https://official-joke-api.appspot.com/random_joke")
    if not respuesta.ok:
        print("Ocurrio un error en la soliictud Api")
    else:
        data = respuesta.json()
        return {
        "categoria" : data.get("type"),
        "pregunta" : data.get("setup"),
        "respuesta" : data.get("punchline")
        }


from fastapi import FastAPI
app = FastAPI(
    title="Fast APi Python V1.2.35",
    description="API Sencilla en Python con FastAPI",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"Bienvenido a mi API"}
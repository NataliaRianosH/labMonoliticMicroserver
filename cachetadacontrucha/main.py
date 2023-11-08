from fastapi import FastAPI

app = FastAPI()

@app.get("/cachetadacontrucha")
def read_cachetada():
    return {"mensaje": " bienvenido al servicio3. Aquí solo hay cachetadas con Trucha!"}

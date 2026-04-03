from fastapi import FastAPI, Query
from app import bonjour, calculer_tva

app = FastAPI()


@app.get("/")
def read_root():
    """Endpoint racine"""
    return {"message": bonjour()}


@app.get("/tva")
def get_tva(prix: float = Query(..., description="Prix HT")):
    """Endpoint pour calculer la TVA"""
    ttc = calculer_tva(prix, 0.20)
    tva = ttc - prix
    return {"tva": tva, "ttc": ttc}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

import fastapi
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

#app = FastAPI()


#@app.get("/")
#async def read_main():
#    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Wikipedia API.  Call /search or /wiki or /trans"}
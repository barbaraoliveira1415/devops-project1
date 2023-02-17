import fastapi # pylint: disable=import-error
from fastapi import FastAPI # pylint: disable=import-error
import uvicorn # pylint: disable=import-error
import requests

from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import trans as wikitranslate

app = FastAPI()


@app.get("/")
async def root():
    """Description"""
    return {"msg": "Wikipedia API.  Call /search or /wiki or /trans"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""

    result = wikilogic(name)
    return {"result": result}


@app.get("/trans/{name}")
async def trans(name: str):
    """Retrieve wikipedia page and return translation to french"""

    result = wikitranslate(name)
    return {"result": result}

#@app.get("/wiki_page/{page}")
#async def page(value: str):
 #   """Wikipedia Page"""

  #  result = wiki_page(value)
   # return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

#result = wiki()

from typing import Union
import requests

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/random")
def random():
    resp = requests.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query",
        "list": "random",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "rnnamespace": 0
        }).json()

    resp = requests.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query",
        "titles": resp['query']['random'][0]['title'],
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "rnnamespace": 0
        }).json()
    return { "data": list(resp['query']['pages'].values())[0]['extract'] }


app.mount("/", StaticFiles(directory="static",html = True), name="static")

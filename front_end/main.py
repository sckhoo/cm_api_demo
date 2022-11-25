from typing import Optional
from fastapi import FastAPI, Request, Header, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
#from pydantic import BaseModel
import requests
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

api_url = 'https://api-sckhoo-1mmxfh5b.uc.gateway.dev'
apitoken = <Hidden Token>

@app.post('/index/' ,response_class=HTMLResponse)
async def index(request: Request, query: str = Form(...), country: str = Form(...)):
    if query == 'gdp':
        final_url = api_url + '/gdp_by_country/' + country
        try:
            response = json.loads(requests.get(final_url).text)
            value = response['GDP_USD']
        except TypeError:
            value = "NA"
    elif query == "population":
        final_url = api_url + '/population_by_country/' + country
        try:
            response = json.loads(requests.get(final_url, params={'key':apitoken}).text)
            value = response['2022 Population']
        except TypeError:
            value = "NA"
    elif query == "happiness":
        final_url = api_url + '/happiness_by_country/' + country
        try:
            response = json.loads(requests.get(final_url).text)
            value = response['RANK']
        except TypeError:
            value = "NA"
    print(type(response))
    return templates.TemplateResponse("respond.html", {"request": request, "query": query.upper(), "country": country.title(), "value": value})


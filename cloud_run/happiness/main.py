import os
from csv import DictReader
from pathlib import Path
from fastapi import FastAPI, HTTPException
from csv2list import get_data_csv


filename = 'World Happiness Report 2022.csv'
data_folder = Path(os.getcwd())
file_to_open = data_folder / filename
list_of_dict = get_data_csv(file_to_open)

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = FastAPI()

@app.get('/')
async def home():
    return {"Hello World": "From Cloudrun Happiness API"}

@app.get('/happiness_by_country/{country}')
async def get_by_name(country: str):
    res = None
    try:
        for sub in list_of_dict:
            if sub['Country'] == country.title():
                res = sub
                break
    except:
        raise HTTPException(status_code=404, detail="Country Not Found")
    return res
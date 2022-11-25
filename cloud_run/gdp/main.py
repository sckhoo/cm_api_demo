import os
from csv import DictReader
from pathlib import Path
from fastapi import FastAPI, HTTPException
from csv2list import get_data_csv

year = '2021'
final_list = []
filename = 'world_country_gdp_usd.csv'
data_folder = Path(os.getcwd())
file_to_open = data_folder / filename
list_of_dict = get_data_csv(file_to_open)

for sub in list_of_dict: 
    if (sub['year'] == year) and sub['GDP_USD']:
        final_list.append(sub)

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = FastAPI()

# Create, Read, Update, Delete

@app.get('/')
async def home():
    return {"Hello World": "From CloudRun FastAPI GDP API"}

@app.get('/gdp_by_country/{country}')
async def get_by_name(country: str):
    res = None
    try:
        for sub in final_list:
            if sub['Country Name'] == country.title():
                res = sub
                break
    except:
        raise HTTPException(status_code=404, detail="Country Not Found")
    return res



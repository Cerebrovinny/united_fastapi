from typing import Union

from fastapi import FastAPI
import json
# from services import get_data

from typing import Dict
import json

#TODO move get_data() and get_plan_name() to services.py

def get_data() -> Dict:
    with open('app/scrap_data/data.json') as f:
        return json.load(f)

def get_plan_id(plan_id: str):
    for employee in get_data():
        for reporting_structure in employee['reporting_structure']:
            print(reporting_structure)
            for reporting_plans in reporting_structure['reporting_plans']:
                print(reporting_plans)
                if reporting_plans['plan_id'] == plan_id:
                    return employee

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/employees")
async def all_data():
    return get_data()

@app.get("/employees/{employee_name}")
async def get_employee(employee_name: str):
    #iterate over the list of employees
    for employee in get_data():
        if employee['reporting_entity_name'] == employee_name:
            return employee

@app.get("/employees/{plan_id}")
async def get_plan(plan_id: int):
    return get_plan_name(plan_id)
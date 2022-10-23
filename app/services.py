from typing import Dict
import json

def get_data() -> Dict:
    with open('app/scrap_data/data.json') as f:
        return json.load(f)

def get_plan_name(plan_name: str):
    for employee in get_data():
        for reporting_structure in employee['reporting_structure']:
            for reporting_plans in reporting_structure['reporting_plans']:
                print(reporting_plans)
                if reporting_plans['plan_name'] == plan_name:
                    return employee
from typing import Dict
import json

def get_data() -> Dict:
    with open('app/data/data.json') as f:
        return json.load(f)
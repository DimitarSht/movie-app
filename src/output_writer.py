from typing import List, Dict
import csv
import json
import sys

def output_csv(data: List[Dict]):
    writer = csv.DictWriter(sys.stdout, fieldnames=["title", "rating"])
    writer.writeheader()
    writer.writerows(data)

def output_json(data: List[Dict]):
    json.dump(data, sys.stdout, indent=2)

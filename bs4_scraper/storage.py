# scraper/storage.py

import csv
import json
import pandas as pd

def save_csv(data, path):
    """
    Save list of dicts `data` to a CSV file at `path`.
    Uses the dict keys as column headers.
    """
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)

def save_json(data, path):
    """
    Save `data` (list of dicts) to a JSON file at `path`.
    Pretty-print with indent=2 and preserve Unicode characters.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_excel(data, path):
    """
    Save `data` (list of dicts) to an Excel .xlsx file at `path`.
    """
    df = pd.DataFrame(data)
    df.to_excel(path, index=False)

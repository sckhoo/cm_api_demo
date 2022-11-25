import os
from csv import DictReader
from pathlib import Path

def get_data_csv(file_to_open):
    if not file_to_open.exists():
        print("Oops, file doesn't exist!")
    else:
        with open(file_to_open, 'r') as f:
            dict_reader = DictReader(f)
            list_temp = list(dict_reader)
    return list_temp
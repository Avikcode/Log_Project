from pathlib import Path
import csv

FILE_NAME = "network_traffic.log"

def get_file_csv(path):
    with open(path) as file:
        return list(csv.reader(file))

# print(get_file_csv(FILE_NAME))

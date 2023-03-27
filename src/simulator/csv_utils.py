import csv
from datetime import datetime
import json
from datamodel import *

def combine_csv_files(file_paths, type):
    combined_csv = []
    header = None
    
    for path in file_paths:
        with open(path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            if header is None:
                header = csv_reader.fieldnames
                combined_csv.append(header)
            for row in csv_reader:
                combined_csv.append([row[column] for column in header])
    timestamp = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    output_path = f"{type}_combined_csv_{timestamp}.csv"
    with open(output_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(combined_csv)
    
    return output_path


def save_results_to_file(result: Dict[str, List[Order]]):
    timestamp = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    file_name = f"sim_{timestamp}"
    json_file = f"{file_name}.json"

    with open(json_file, "w") as f:
        f.write(json.dumps(result, indent=2, cls=ProsperityEncoder))
        print(f"Results has been written to {json_file}.")


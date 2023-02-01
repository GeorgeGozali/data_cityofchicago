import requests as r
import json
import csv
import pandas as pd

URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?year=2022"


def write_json(row, columns):
    full_dict = {row[0]: {}}
    for ro, c in zip(row, columns):
        full_dict[row[0]][c] = ro
    with open("crimes_data.json", 'a', encoding='utf-8') as f:
        f.write(json.dumps(full_dict, indent=4))


def write_csv(data):
    columns = []
    for key in data[0].keys():
        if isinstance(data[0].get(key), dict):
            for inner_key in data[0].get(key).keys():
                columns.append(inner_key)

        else:
            columns.append(key)

    with open('crimes_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)

        for data_row in data:
            row = []
            for value in data_row.values():
                if not isinstance(value, dict):
                    row.append(value)
                else:
                    for inner_value in value.values():
                        row.append(inner_value)
            writer.writerow(row)
            write_json(row, columns)


def pd_write_primary_types():
    df = pd.read_csv("crimes_data.csv")
    primary_types = df['primary_type'].unique()
    for pr_type in primary_types:
        df = df[df['primary_type'] == f"{pr_type}"]
        df.to_csv(f"{pr_type.lower()}.csv", encoding='utf-8', index=False)


if __name__ == "__main__":
    response = r.get(URL)
    response_data = response.json()
    write_csv(response_data)
    pd_write_primary_types()

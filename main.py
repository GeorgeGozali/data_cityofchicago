import requests as r
import csv

url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?year=2022"

response = r.get(url)
data = response.json()


def write_csv(data):
    columns = []
    for key in data[0].keys():
        if type(data[0].get(key)) == dict:
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
                if type(value) != dict:
                    row.append(value)
                else:
                    for inner_value in value.values():
                        row.append(inner_value)
            writer.writerow(row)


if __name__ == "__main__":
    write_csv(data)

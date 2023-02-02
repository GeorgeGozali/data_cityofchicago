import json
import csv


def read_data(filename: str) -> dict:
    with open(filename) as f:
        data = json.load(f)
    return data


def format_date(date_string: str) -> str:
    date_list = date_string.split("/")
    date_list[2] = "20" + date_list[2]
    date_list[1] = date_list[1].zfill(2)
    date_list[0] = date_list[0].zfill(2)
    return "-".join(date_list)


def write_data(my_dict: dict) -> None:
    COLUMNS_LIST = ["cases", "deaths", "recovered", "date", "country", "province"]

    file = open("covid_data.csv", "a")
    writer = csv.writer(file)
    writer.writerow(COLUMNS_LIST)

    for list_item in my_dict:
        for value in list_item.values():
            if not isinstance(value, dict):
                pass
            else:
                cases = [in_value for in_value in value.get("cases").values()]
                deaths = [in_value for in_value in value.get("deaths").values()]
                recovered = [
                    (format_date(k), v) for k, v in value.get("recovered").items()
                ]
                # with open("covid_data.csv", "a") as file:
                #     writer = csv.writer(file)
                #     writer.writerow(COLUMNS_LIST)
                for c, d, r in zip(cases, deaths, recovered):
                    writer.writerow(
                        [
                            c,
                            d,
                            r[0],
                            r[1],
                            list_item.get("country"),
                            list_item.get("province"),
                        ]
                    )
    file.close()


if __name__ == "__main__":
    data = read_data("raw.json")
    write_data(data)

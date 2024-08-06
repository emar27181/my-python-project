import csv
from config.constants_dev import LOAD_RANK


def _percent_normalize(value_str):
    if '%' in value_str:
        value_str = value_str.replace('%', '')
    value = float(value_str)
    return value / 100.0


def read_file_to_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    data_list = []
    for i in range(0, len(lines), 14):
        person_dict = {
            'Name': lines[i + 1],
            'KD': lines[i + 2],
            'WinRate': _percent_normalize(lines[i + 8]),
            'PickRate': _percent_normalize(lines[i + 10]),
        }
        data_list.append(person_dict)

    return data_list


def write_dict_to_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


def main():
    file_name = (f"epi9_act1_allmap_{LOAD_RANK}")
    data = read_file_to_data(f'tmp/valorant/data/input/{file_name}.txt')
    print(data)

    output_file_path = (f'tmp/valorant/data/output/{file_name}.csv')
    write_dict_to_csv(data, output_file_path)


if __name__ == "__main__":
    main()

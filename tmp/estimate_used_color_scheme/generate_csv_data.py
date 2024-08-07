import json
import csv


def generate_csv_used_color_scheme(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    used_color_list = []

    for color_scheme in json_data:
        for color_data in color_scheme:
            # print(f"color_data: {color_data}")
            add_dict = {
                'Color': color_data['color'],
                'Rate': color_data['rate'],
                'IllustName': color_scheme[0]['illustName'],
            }
            # print(f"add_dict: {add_dict}")
            used_color_list.append(add_dict)

    print(f"used_color_list: {used_color_list}")


def main():
    generate_csv_used_color_scheme('tmp/estimate_used_color_scheme/data/output/log_used_color_scheme_gaako_instagram.json')


if __name__ == "__main__":
    main()

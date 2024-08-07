import json
import csv
from utils.color_utils import hex_to_rgb, rgb_to_hsl


# 使用した配色のjsonファイルを辞書型のデータに変換する関数
def used_color_scheme_json_to_dict(file_path, illustrator_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    used_color_list = []

    for color_scheme in json_data:
        for color_data in color_scheme:

            color_hex = color_data['color']
            color_rgb = hex_to_rgb(color_hex)
            print(f"color_rgb = {color_rgb}")
            color_hsl = rgb_to_hsl(color_rgb)
            print(f"color_hsl = { color_hsl }")
            print("")
            # print(f"color_data: {color_data}")

            add_dict = {
                'Color': color_data['color'],
                'Hue': color_hsl[0],
                'Saturation': color_hsl[1],
                'Lightness': color_hsl[2],
                'Rate': color_data['rate'],
                'IllustName': color_scheme[0]['illustName'],
                'illustrator_name': illustrator_name,
            }
            # print(f"add_dict: {add_dict}")
            used_color_list.append(add_dict)

    print(f"used_color_list: {used_color_list}")
    return used_color_list


def write_dict_to_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


def main():
    illustrator_name = "gaako_instagram"
    data = used_color_scheme_json_to_dict(f'tmp/estimate_used_color_scheme/data/output/log_used_color_scheme_{illustrator_name}.json', illustrator_name)

    output_file_path = "tmp/estimate_used_color_scheme/data/output/log_used_all_colors.csv"
    write_dict_to_csv(data, output_file_path)
    print(f"{output_file_path} is saved.")


if __name__ == "__main__":
    main()

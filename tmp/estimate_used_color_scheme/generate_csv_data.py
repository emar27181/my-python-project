import json
import csv
from utils.color_utils import hex_to_rgb, rgb_to_hsl


def generate_csv_used_color_scheme(file_path, illustrator_name):
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


def main():
    illustrator_name = "gaako_instagram"
    generate_csv_used_color_scheme(f'tmp/estimate_used_color_scheme/data/output/log_used_color_scheme_{illustrator_name}.json', illustrator_name)


if __name__ == "__main__":
    main()

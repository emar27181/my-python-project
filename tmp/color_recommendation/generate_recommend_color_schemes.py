import json
from utils.color_utils import print_colored_text, hex_to_rgb


# ある塗りかけの配色を基に配色を推薦する関
def generate_recommend_color_schemes(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    # print(json_data)

    for used_colors_info in json_data:
        # print(used_colors_info)
        for color_info in used_colors_info:
            color_rgb = hex_to_rgb(color_info['color'])
            # print(color_rgb)
            print_colored_text("■■■■", color_rgb)
            print(f"color: {color_info['color']}, rate: {color_info['rate']}")
        print("")


def main():
    generate_recommend_color_schemes('tmp/color_recommendation/data/input/log_used_color_scheme_NCG.json')


if __name__ == "__main__":
    main()

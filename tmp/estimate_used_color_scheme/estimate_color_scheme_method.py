import json
from estimate_used_color_scheme import rgb_to_hsl
from utils.color_utils import hex_to_rgb

# ある配色で使われた配色技法を推定する関数


def estimate_color_scheme_method(json_color_scheme):
    # print(color_scheme)
    hue_array = []

    for json_color in json_color_scheme:
        # print(json_color)
        color = json_color['color']
        color_rgb = hex_to_rgb(color)
        color_hsl = rgb_to_hsl(color_rgb)
        hue = color_hsl[0]
        saturation = color_hsl[1]
        if (saturation > 10):
            hue_array.append(hue)
        print(f"hue_array = {hue_array}")

    print("")


def main():

    with open("tmp/estimate_used_color_scheme/data/output/log_used_color_scheme.json", "r") as file:
        json_data = json.load(file)

    for color_scheme in json_data:
        estimate_color_scheme_method(color_scheme)

    # print(json_data)


if __name__ == "__main__":
    main()

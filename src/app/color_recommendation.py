import json
json_file_path = 'data/output/output_color_combination.json'


def color_recommendation():
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    my_color = Color(data[0]["hue"], data[0]
                     ["saturation"], data[0]["lightness"])

    generate_color_combination(my_color)


class Color:
    def __init__(self, hue, saturation, lightness):
        self.hue = hue % 360
        self.saturation = saturation % 100
        self.lightness = lightness % 100

    def __str__(self):
        return f"Color(hue={self.hue}, saturation={self.saturation}, lightness={self.lightness})"


def updateJson(new_color):
    new_data = {
        "hue": new_color.hue,
        "saturation": new_color.saturation,
        "lightness": new_color.lightness
    }

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        data.append(new_data)

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def generate_color_combination(color):
    # 色の組み合わせを返す関数
    print("color(" + str(color.hue) + ", " +
          str(color.saturation) + ", " + str(color.lightness) + ")")

    # 同一色相配色
    new_color = same_hue_color_scheme(color)

    # 隣接色相配色
    # 類似色相配色
    # 中差色相配色
    # 対照色相配色
    # 補色色相配色
    updateJson(new_color)


def same_hue_color_scheme(color):
    new_color = Color(color.hue, color.saturation - 30, color.lightness - 30)
    print("new_color(" + str(new_color.hue) + ", " +
          str(new_color.saturation) + ", " + str(new_color.lightness) + ")")
    return (new_color)


if __name__ == "__main__":
    color_recommendation()

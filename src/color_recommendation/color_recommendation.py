def main():
    #my_color = Color(360, 50, 50)
    my_color = Color(480, 150, 150)
    generate_color_combination(my_color)


class Color:
    def __init__(self, hue, saturation, lightness):
        self.hue = hue % 360
        self.saturation = saturation % 100
        self.lightness = lightness % 100

    def __str__(self):
        return f"Color(hue={self.hue}, saturation={self.saturation}, lightness={self.lightness})"

# 色の組み合わせを返す関数
def generate_color_combination(color):
    print("color(" + str(color.hue) + ", " +
          str(color.saturation) + ", " + str(color.lightness) + ")")

    # 同一色相配色
    same_hue_color_scheme(color)

    # 隣接色相配色
    # 類似色相配色
    # 中差色相配色
    # 対照色相配色
    # 補色色相配色


def same_hue_color_scheme(color):
    new_color = Color(color.hue, color.saturation - 30, color.lightness - 30)
    print("new_color(" + str(new_color.hue) + ", " +
          str(new_color.saturation) + ", " + str(new_color.lightness) + ")")


if __name__ == "__main__":
    main()

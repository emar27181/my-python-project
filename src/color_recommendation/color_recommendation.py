

def main():
    my_color = Color(255, 255, 255)
    generate_color_combination(my_color)

class Color:
    def __init__(self, hue, saturation, lightness):
        self.hue = hue
        self.saturation = saturation
        self.lightness = lightness

    def __str__(self):
        return f"Color(hue={self.hue}, saturation={self.saturation}, lightness={self.lightness})"

def generate_color_combination(color):
    print(color.hue, color.saturation, color.lightness)


if __name__ == "__main__":
    main()

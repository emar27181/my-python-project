from estimate_used_color_scheme import estimate_used_color_scheme


# 読込んだイラストの使用配色をjson形式で保存する関数
def generate_json_used_color_scheme(image_path):
    estimate_used_color_scheme(image_path)


def main():
    generate_json_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG297-2-1920x1920.jpg')
    generate_json_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG260-2000x1200.jpg')
    generate_json_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG290-1920x1200.jpg')


if __name__ == "__main__":
    main()

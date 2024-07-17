import json


# ある塗りかけの配色を基に配色を推薦する関
def generate_recommend_color_schemes(file_path):
    print("init")

    with open(file_path, 'r') as file:
        data = json.load(file)

    print(data)


def main():
    generate_recommend_color_schemes('tmp/color_recommendation/data/input/log_used_color_scheme_NCG.json')


if __name__ == "__main__":
    main()

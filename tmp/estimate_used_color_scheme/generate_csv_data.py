import json


def generate_csv_used_color_scheme(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    print(f"json_data: {json_data}")


def main():
    generate_csv_used_color_scheme('tmp/estimate_used_color_scheme/data/output/log_used_color_scheme_gaako_instagram.json')


if __name__ == "__main__":
    main()

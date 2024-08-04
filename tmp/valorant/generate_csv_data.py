
def read_file_to_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data


def main():
    data = read_file_to_data('tmp/valorant/data/input/epi9_act1_allmap_bronze3.txt')
    print(data)


if __name__ == "__main__":
    main()

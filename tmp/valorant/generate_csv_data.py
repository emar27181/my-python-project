
def read_file_to_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    data_list = []
    for i in range(0, len(lines), 14):
        person_dict = {
            'Name': lines[i + 1],
            'KD': lines[i + 2],
            'WinRate': lines[i + 8],
            'PickRate': lines[i + 10],
        }
        data_list.append(person_dict)

    return data_list


def main():
    # data = read_file_to_data('tmp/valorant/data/input/epi9_act1_allmap_bronze3.txt')
    data = read_file_to_data('tmp/valorant/data/input/epi9_act1_allmap_platinum3.txt')
    # data = read_file_to_data('tmp/valorant/data/input/epi9_act1_allmap_immortal3.txt')
    print(data)


if __name__ == "__main__":
    main()

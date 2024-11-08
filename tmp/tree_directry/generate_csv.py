

def read_tree_file_to_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    lines = [line.replace('-', '') for line in lines]
    lines = [line.replace(',', '') for line in lines]

    print(lines)


def generate_csv():
    read_tree_file_to_data('tmp/tree_directry/data/input/tree_emar27181_github_io.txt')


def main():
    generate_csv()


if __name__ == "__main__":
    main()

import csv
from config.constants_dev import LOAD_RANK


def _percent_normalize(value_str):
    if '%' in value_str:
        value_str = value_str.replace('%', '')
    try:
        value = float(value_str)
    except ValueError:
        value = -1
    return value / 100.0


def read_agent_file_to_data(file_path, load_rank):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    data_list = []
    for i in range(0, len(lines), 14):
        person_dict = {
            'Name': lines[i + 1],
            'KD': lines[i + 2],
            'WinRate': _percent_normalize(lines[i + 8]),
            'PickRate': _percent_normalize(lines[i + 10]),
            'Rank': load_rank,
        }
        data_list.append(person_dict)

    return data_list


def read_rifle_file_to_data(file_path, load_rank):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    data_list = []
    for i in range(0, len(lines), 9):
        person_dict = {
            'Name': lines[i + 1],
            'KillPerRound': lines[i + 2],
            'HeadShotRate': _percent_normalize(lines[i + 4]),
            'BodyShotRate': _percent_normalize(lines[i + 5]),
            'LegShotRate': _percent_normalize(lines[i + 6]),
            'AverageDamage': lines[i + 7],
            'Rank': load_rank,
        }
        data_list.append(person_dict)

    return data_list


def get_agent_role(agent_name):
    if agent_name in ['Jett', 'Raze', 'Neon', 'Reyna', 'Iso', 'Phoenix', 'Yoru']:
        return "duelist"
    elif agent_name in ['Omen', 'Viper', 'Brimstone', 'Astra', 'Harbor', 'Clove']:
        return "controller"
    elif agent_name in ['Sova', 'Fade', 'Skye', 'Breach', 'Gekko', 'KAY/O']:
        return "initiater"
    elif agent_name in ['Killjoy', 'Cypher', 'Sage', 'Chamber', 'Deadlock']:
        return "sentinel"
    else:
        return "unknown"


def read_agent_avility_file_to_data(file_path, load_rank):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    data_list = []
    for i in range(0, len(lines), 7):
        role = get_agent_role(lines[i + 1])

        person_dict = {
            'Name': lines[i + 1],
            'Ability1': lines[i + 2],
            'Ability2': lines[i + 3],
            'Ability3': lines[i + 4],
            'Ultimate': lines[i + 5],
            'Matches': lines[i + 6],
            'Rank': load_rank,
            'Role': role,
        }
        data_list.append(person_dict)

    return data_list


# 引数で受け取ったエージェントのスキルに関するデータのCSVファイルを生成する関数
def generate_agent_avility_csv_data(load_rank_list):
    data = []
    for load_rank in load_rank_list:
        file_name = (f"agent_avility_epi9_act1_allmap_{load_rank}")
        add_data = read_agent_avility_file_to_data(f'tmp/valorant/data/input/{file_name}.txt', load_rank)
        data = data + add_data

    output_file_path = (f'tmp/valorant/data/output/agent_avility_epi9_act1_allmap.csv')
    write_dict_to_csv(data, output_file_path)
    print(f"{output_file_path} is saveed.")


# 引数で受け取ったライフルに関するデータのCSVファイルを生成する関数
def generate_rifle_csv_data(load_rank_list):
    data = []
    for load_rank in load_rank_list:
        file_name = (f"rifle_epi9_act1_allmap_{load_rank}")
        add_data = read_rifle_file_to_data(f'tmp/valorant/data/input/{file_name}.txt', load_rank)
        data = data + add_data

    output_file_path = (f'tmp/valorant/data/output/rifle_epi9_act1_allmap.csv')
    write_dict_to_csv(data, output_file_path)
    print(f"{output_file_path} is saveed.")


def write_dict_to_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


# 引数で受け取ったランクのエージェントに関するデータのCSVファイルを生成する関数
def generate_agent_csv_data(load_rank_list):
    data = []
    for load_rank in load_rank_list:
        file_name = (f"epi9_act1_allmap_{load_rank}")
        add_data = read_agent_file_to_data(f'tmp/valorant/data/input/{file_name}.txt', load_rank)
        data = data + add_data

    output_file_path = (f'tmp/valorant/data/output/agent_epi9_act1_allmap.csv')
    write_dict_to_csv(data, output_file_path)
    print(f"{output_file_path} is saved.")


def main():
    generate_agent_csv_data(["bronze3", "platinum3", "immortal3"])
    generate_rifle_csv_data(["iron3", "bronze3", "silver3", "gold3", "platinum3", "diamond3", "ascendant3", "immortal3", "radiant"])
    generate_agent_avility_csv_data(["iron3", "bronze3", "silver3", "gold3", "platinum3", "diamond3", "ascendant3", "immortal3", "radiant"])


if __name__ == "__main__":
    main()

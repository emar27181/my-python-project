import matplotlib.pyplot as plt
import os
import numpy as np
import json
import config.constants

# 配列の宣言を関数内に移動して、リセット可能にする


def insert_values(recalls):
    recall_at_k_values = []
    precision_at_k_values = []
    k_values = []

    for item in recalls:
        recall = item.get('recall')
        k = item.get('k')

        if k == 0:
            continue

        correct_number = recall * config.constants.EVALUATED_ILLUST_COUNT
        recall_at_k_values.append(recall)
        precision_at_k_values.append(correct_number / k)
        k_values.append(k)

    return recall_at_k_values, precision_at_k_values, k_values

# 引数で受け取った値のグラフを作成する関数


def plot_graph(graph_name, k_values, y_values, same, timing, color, label):
    plt.plot(k_values, y_values, marker='o', color=color, label=label)
    plt.title(f'{graph_name}@k (SAME={config.constants.SIM_MIN}~{config.constants.SIM_MAX}, EVAL={timing},n={config.constants.EVALUATED_ILLUST_COUNT})')
    plt.ylim(0, 1)
    plt.xlabel('k(recommend color schemes pattern)')
    plt.ylabel(graph_name)
    plt.xticks(np.arange(0, max(k_values) + 1, 5))
    plt.grid(True)
    plt.legend()


def return_data(same, timing, lightness):
    file_name = f'recall@k_SAME={same}_EVAL={timing}_LIGHT={lightness}'
    file_path = f'tmp/input/{file_name}.json'

    # ファイルが正しく読み込めた場合
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:

        # jsonデータの読み込み
        with open(file_path, 'r') as file:
            print(f'./{file_path}が読み込まれました．')
            data = json.load(file)
        return data
    # ファイルが存在しなかった場合
    else:
        print(f'./{file_path}は存在しませんでした．')
        return []


# 引数で受け取った閾値のデータを読み込んでグラフを生成する関数
def generate_graph(graph_type, label, color, same, timing, lightness, TIME_LIST):

    data = return_data(same, timing, lightness)

    if (data == []):
        return

    # ファイルデータの取得
    recalls = return_data(same, timing, lightness)

    # 配列のデータの更新
    recall_at_k_values, precision_at_k_values, k_values = insert_values(recalls)
    # color = colors[idx % len(colors)]
    # label = f'SAME={same}'

    if (graph_type == 'recall'):
        plot_graph('recall', k_values, recall_at_k_values, same, TIME_LIST, color, label)
    elif (graph_type == 'precision'):
        plot_graph('precision', k_values, precision_at_k_values, same, TIME_LIST, color, label)
    else:
        print('Invalid graph type')


def load_file_and_generate_graph(graph_type):

    TIME_LIST = [[1]]
    colors = ['blue', 'green', 'red', 'purple']
    i = 0

    plt.figure(figsize=(10, 6))  # グラフの初期化

    for lightness in config.constants.LIGHTNESS_LIST:
        label = f'lightness={lightness}'
        i += 1
        for timing in TIME_LIST:
            color = colors[i % len(colors)]
            # label = f'timing={timing}'
            # i += 1

            for idx, same in enumerate(range(config.constants.SIM_MIN, config.constants.SIM_MAX + 1, 5)):
                generate_graph(graph_type, label, color, same, timing, lightness, TIME_LIST)

    # 対応するグラフの保存
    file_name = f'{graph_type}@k_SAME={config.constants.SIM_MIN}~{config.constants.SIM_MAX}_TIME={TIME_LIST}_LIGHT={config.constants.LIGHTNESS_LIST}'
    plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/{file_name}.png')
    print(f"./tmp/output/{file_name}.png が保存されました．\n")


def main():

    # recall@kのグラフの作成
    load_file_and_generate_graph('recall')
    # precision@kのグラフの作成
    load_file_and_generate_graph('precision')


if __name__ == "__main__":
    main()

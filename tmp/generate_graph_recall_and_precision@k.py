import matplotlib.pyplot as plt
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


def return_data(same, timing):
    file_name = f'recall@k_SAME={same}_EVAL={timing}'
    file_path = f'tmp/input/{file_name}.json'

    # jsonデータの読み込み
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# 引数で受け取った閾値のデータを読み込んでグラフを生成する関数
def generate_graph(graph_type, label, color, same, timing, TIME_LIST):
    # ファイルデータの取得
    recalls = return_data(same, timing)

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

    TIME_LIST = [[0], [1], [0, 1]]
    colors = ['blue', 'green', 'red', 'purple']
    i = 0

    plt.figure(figsize=(10, 6))  # グラフの初期化

    for timing in TIME_LIST:
        color = colors[i % len(colors)]
        label = f'timing={timing}'
        i += 1

        for idx, same in enumerate(range(config.constants.SIM_MIN, config.constants.SIM_MAX + 1, 5)):
            generate_graph(graph_type, label, color, same, timing, TIME_LIST)

    # 対応するグラフの保存
    file_name = f'{graph_type}@k_SAME={config.constants.SIM_MIN}~{config.constants.SIM_MAX}_TIME={TIME_LIST}'
    plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/{file_name}.png')
    print(f"./tmp/output/{file_name}.png is saved")


def main():

    # recall@kのグラフの作成
    load_file_and_generate_graph('recall')
    # precision@kのグラフの作成
    load_file_and_generate_graph('precision')


if __name__ == "__main__":
    main()

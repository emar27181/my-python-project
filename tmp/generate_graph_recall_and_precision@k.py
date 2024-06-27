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


def generate_graph(graph_name, k_values, y_values, SAME, TIME, color, label):
    plt.plot(k_values, y_values, marker='o', color=color, label=label)
    plt.title(f'{graph_name}@k (SAME={config.constants.SIM_MIN}~{config.constants.SIM_MAX}, EVAL={TIME},n={config.constants.EVALUATED_ILLUST_COUNT})')
    plt.ylim(0, 1)
    plt.xlabel('k(recommend color schemes pattern)')
    plt.ylabel(graph_name)
    plt.xticks(np.arange(0, max(k_values) + 1, 5))
    plt.grid(True)
    plt.legend()


def return_data(SAME, TIME):
    file_name = f'recall@k_SAME={SAME}_EVAL={TIME}'
    file_path = f'tmp/input/{file_name}.json'

    # jsonデータの読み込み
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def load_file_and_generate_graph(graph_type):

    TIME = [0, 1]
    colors = ['blue', 'green', 'red', 'purple']

    plt.figure(figsize=(10, 6))  # グラフの初期化
    for idx, SAME in enumerate(range(config.constants.SIM_MIN, config.constants.SIM_MAX + 1, 5)):
        # ファイルデータの取得
        recalls = return_data(SAME, TIME)

        # 配列のデータの更新
        recall_at_k_values, precision_at_k_values, k_values = insert_values(recalls)
        color = colors[idx % len(colors)]
        label = f'SAME={SAME}'

        if (graph_type == 'recall'):
            generate_graph('recall', k_values, recall_at_k_values, SAME, TIME, color, label)
        elif (graph_type == 'precision'):
            generate_graph('precision', k_values, recall_at_k_values, SAME, TIME, color, label)

    # 対応するグラフの保存
    file_name = f'{graph_type}@k_SAME={config.constants.SIM_MIN}~{config.constants.SIM_MAX}_EVAL={TIME}'
    plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/{file_name}.png')
    print(f"./tmp/output/{file_name}.png is saved")


def main():

    load_file_and_generate_graph('recall')
    load_file_and_generate_graph('precision')

    # recall@kグラフの生成
    """
    plt.figure(figsize=(10, 6))  # グラフの初期化
    for idx, SAME in enumerate(range(config.constants.SIM_MIN, config.constants.SIM_MAX + 1, 5)):
        # ファイルデータの取得
        recalls = return_data(SAME, TIME)

        # 配列のデータの更新
        recall_at_k_values, precision_at_k_values, k_values = insert_values(recalls)
        color = colors[idx % len(colors)]
        label = f'SAME={SAME}'
        generate_graph('recall', k_values, recall_at_k_values, SAME, TIME, color, label)

    # グラフの保存
    file_name = f'recall@k_SAME={config.constants.SIM_MIN}~{config.constants.SIM_MAX}_EVAL={TIME}'
    plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/{file_name}.png')
    print(f"./tmp/output/{file_name}.png is saved")

    # precision@kグラフの作成
    plt.figure(figsize=(10, 6))
    for idx, SAME in enumerate(range(config.constants.SIM_MIN, config.constants.SIM_MAX + 1, 5)):
        # ファイルデータの取得
        recalls = return_data(SAME, TIME)

        # 配列のデータの更新
        recall_at_k_values, precision_at_k_values, k_values = insert_values(recalls)
        color = colors[idx % len(colors)]
        label = f'SAME={SAME}'
        generate_graph('precision', k_values, precision_at_k_values, SAME, TIME, color, label)

    # グラフをファイルに保存
    file_name = f'precision@k_SAME={config.constants.SIM_MIN}~{config.constants.SIM_MAX}_EVAL={TIME}'
    plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/{file_name}.png')
    print(f"./tmp/output/{file_name}.png is saved")
    """


if __name__ == "__main__":
    main()

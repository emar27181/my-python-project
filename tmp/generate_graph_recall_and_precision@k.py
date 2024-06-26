import matplotlib.pyplot as plt
import numpy as np
import json
import config.constants

# 配列の宣言
recall_at_k_values = []
precision_at_k_values = []
k_values = []


# 引数で受け取った値を配列に挿入する関数
def insert_values(recalls):
    for item in recalls:
        recall = item.get('recall')
        k = item.get('k')

        if (k == 0):
            continue

        corecct_number = recall * (config.constants.EVALUATED_ILLUST_COUNT)
        recall_at_k_values.append(recall)
        precision_at_k_values.append(corecct_number / k)
        k_values.append(k)


# 引数で受け取った値のグラフを作成する関数
def generate_graph(graph_name, y_values, SAME, TIME):
    plt.plot(k_values, y_values, marker='o')
    plt.title(f'{graph_name}@k (SAME={SAME}, EVAL={TIME},n={config.constants.EVALUATED_ILLUST_COUNT})')
    plt.ylim(0, 1)
    plt.xlabel('K')
    plt.ylabel(f'{graph_name}')
    plt.xticks(np.arange(0, max(k_values) + 1, 5))
    plt.grid(True)


def return_data(SAME, TIME):
    file_name = (f'recall@k_SAME={SAME}_EVAL={TIME}')
    file_path = (f'tmp/input/{file_name}.json')

    # jsonデータの読み込み
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def main():

    SAME = 15
    TIME = [0, 1]

    # ファイル名を変数を使って動的に生成する
    """
    file_name = (f'recall@k_SAME={config.constants.SIM_VALUE_IS_SAME_COLOR}_EVAL={config.constants.IS_EVALUATED_TIMING_DRAW_COLOR}')
    file_path = (f'tmp/input/{file_name}.json')

    # jsonデータの読み込み
    with open(file_path, 'r') as file:
        data = json.load(file)
    recalls = data
    """

    plt.figure(figsize=(10, 6))
    recalls = return_data(SAME, TIME)

    insert_values(recalls)

    # recall@kグラフの生成
    generate_graph('recall', recall_at_k_values, SAME, TIME)

    # グラフの保存
    file_name = (f'recall@k_SAME={SAME}_EVAL={TIME}')
    plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/{file_name}.png')
    print(f"./tmp/output/{file_name}.png is saved")

    plt.figure(figsize=(10, 6))

    # precision@kグラフの作成
    generate_graph('precision', precision_at_k_values, SAME, TIME)

    # グラフをファイルに保存
    precision_file_name = (f'precision@k_SAME={SAME}_EVAL={TIME}')
    # precision_file_name = (f'precision@k_SAME={config.constants.SIM_VALUE_IS_SAME_COLOR}_EVAL={config.constants.IS_EVALUATED_TIMING_DRAW_COLOR}')
    plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/{precision_file_name}.png')
    print(f"./tmp/output/{precision_file_name}.png is saved")


if __name__ == "__main__":
    main()

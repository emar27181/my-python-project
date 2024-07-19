import matplotlib.pyplot as plt
import os
import numpy as np
import json
import config.constants
from config.constants import LOAD_ILLUST_DIR_NAME

# 配列の宣言を関数内に移動して、リセット可能にする


def insert_values(recalls):
    # print(recalls)

    recall_at_k_values = []
    precision_at_k_values = []
    color_count_at_k_values = []
    k_values = []

    for item in recalls:
        recall = item.get('recall')
        color_count = item.get('colorCountAve')
        k = item.get('k')

        if k == 0:
            continue

        correct_number = recall * config.constants.EVALUATED_ILLUST_COUNT
        recall_at_k_values.append(recall)
        color_count_at_k_values.append(color_count)
        precision_at_k_values.append(correct_number / k)
        k_values.append(k)

    return recall_at_k_values, precision_at_k_values, color_count_at_k_values, k_values

# 引数で受け取った値のグラフを作成する関数


def plot_graph(graph_name, k_values, y_values, same, SAME_LIST, TIME_LIST, color, label, y_limit):
    plt.plot(k_values, y_values, marker='o', color=color, label=label)
    plt.title(f'{graph_name}@k (illustrator: {LOAD_ILLUST_DIR_NAME}, SAME={SAME_LIST[0]}~{SAME_LIST[1]}, TIME={TIME_LIST},n={config.constants.EVALUATED_ILLUST_COUNT})')
    # plt.title(f'illustrator: {LOAD_ILLUST_DIR_NAME} {graph_name}@k, TIME={timing},n={config.constants.EVALUATED_ILLUST_COUNT})')
    plt.ylim(0, y_limit)
    plt.xlabel('k(recommend color schemes pattern)')
    plt.ylabel(graph_name)
    plt.xticks(np.arange(0, max(k_values) + 1, 5))
    plt.grid(True)
    plt.legend()


def return_data(same, timing, lightness):
    file_name = f'recall@k_SAME={same}_TIME={timing}_LIGHT={lightness}'
    file_path = f'tmp/plot_evaluate_graph/data/input/{LOAD_ILLUST_DIR_NAME}/{file_name}.json'

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
def generate_graph(graph_type, label, color, same, timing, lightness, SAME_LIST, TIME_LIST):

    data = return_data(same, timing, lightness)

    if (data == []):
        return

    # ファイルデータの取得
    recalls = return_data(same, timing, lightness)

    # 配列のデータの更新
    recall_at_k_values, precision_at_k_values, color_count_at_k_values, k_values = insert_values(recalls)

    if (graph_type == 'recall'):
        plot_graph('recall', k_values, recall_at_k_values, same, SAME_LIST, TIME_LIST, color, label, 1)
    elif (graph_type == 'precision'):
        plot_graph('precision', k_values, precision_at_k_values, same, SAME_LIST, TIME_LIST, color, label, 1)
    elif (graph_type == 'color_count'):
        plot_graph('color_count', k_values, color_count_at_k_values, same, SAME_LIST, TIME_LIST, color, label, 5)
    else:
        print('Invalid graph type')


def load_file_and_generate_graph(graph_type, EVAL_PARAM, SAME_LIST, TIME_LIST, LIGHTNESS_LIST):

    colors = ['blue', 'green', 'red', 'purple']
    i = 0

    plt.figure(figsize=(10, 6))  # グラフの初期化
    print(f"============ {graph_type}@k のグラフ作成 ================")

    # 明度のバリエーションによる精度の違いのプロット
    for lightness in LIGHTNESS_LIST:

        label = 'INIT'
        color = "blue"

        if (EVAL_PARAM == 'CUSTOM'):
            label = 'CUSTOM'

        # ラベルを明度の違いに設定
        if (EVAL_PARAM == 'LIGHT'):
            color = colors[i % len(colors)]
            label = f'lightness={lightness}'
            i += 1

        # タイミングの違いによる精度の違いのプロット
        for timing in TIME_LIST:
            # ラベルをタイミングの違いに設定
            if (EVAL_PARAM == 'TIME'):
                color = colors[i % len(colors)]
                label = f'timing={timing}'
                i += 1

            # 同一色判定の閾値の違いによる精度の違いのプロット
            for idx, same in enumerate(range(SAME_LIST[0], SAME_LIST[1] + 1, 5)):
                # ラベルを同一色判定の閾値に設定
                if (EVAL_PARAM == 'SAME'):
                    color = colors[i % len(colors)]
                    label = f'SAME={same}'
                    i += 1

                generate_graph(graph_type, label, color, same, timing, lightness, SAME_LIST, TIME_LIST)

    # 対応するグラフの保存
    file_name = f'{graph_type}@k_illustrator={LOAD_ILLUST_DIR_NAME}_SAME={SAME_LIST[0]}~{SAME_LIST[1]}_TIME={TIME_LIST}_LIGHT={LIGHTNESS_LIST}'
    plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/plot_evaluate_graph/data/output/{file_name}.png')
    print(f"./tmp/plot_evaluate_graph/data/output/{file_name}.png が保存されました．\n")


def main():

    # recall@kのグラフの作成
    load_file_and_generate_graph('recall', 'SAME', [5, 15], [[0, 1, 2]], [[20]])
    load_file_and_generate_graph('recall', 'TIME', [10, 10], [[0], [1], [2], [0, 1, 2]], [[20]])
    load_file_and_generate_graph('recall', 'LIGHT', [10, 10], [[0, 1, 2]], [[], [10], [20]])

    # precision@kのグラフの作成
    load_file_and_generate_graph('precision', 'SAME', [5, 15], [[0, 1, 2]], [[20]])
    load_file_and_generate_graph('precision', 'TIME', [10, 10], [[0], [1], [2], [0, 1, 2]], [[20]])
    load_file_and_generate_graph('precision', 'LIGHT', [10, 10], [[0, 1, 2]], [[], [10], [20]])

    # color_count@kのグラフの作成
    load_file_and_generate_graph('color_count', 'SAME', [5, 15], [[0, 1, 2]], [[20]])
    load_file_and_generate_graph('color_count', 'TIME', [10, 10], [[0], [1], [2], [0, 1, 2]], [[20]])
    load_file_and_generate_graph('color_count', 'LIGHT', [10, 10], [[0, 1, 2]], [[], [10], [20]])


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np
import json
import config.constants

# ファイル名を変数を使って動的に生成する
file_name = (f'recall@k_SAME={config.constants.SIM_VALUE_IS_SAME_COLOR}_EVAL={config.constants.IS_EVALUATED_TIMING_DRAW_COLOR}')
file_path = (f'tmp/input/{file_name}.json')

# jsonデータの読み込み
with open(file_path, 'r') as file:
    data = json.load(file)
recalls = data

# 配列の宣言
recall_at_k_values = []
precision_at_k_values = []
k_values = []

# 配列に値の代入
for item in recalls:
    recall = item.get('recall')
    k = item.get('k')

    if (k == 0):
        continue

    corecct_number = recall * (config.constants.EVALUATED_ILLUST_COUNT)
    recall_at_k_values.append(recall)
    precision_at_k_values.append(corecct_number / k)
    k_values.append(k)


def recall_at_k(true_labels, pred_scores, k):
    sorted_indices = np.argsort(pred_scores)[::-1]
    sorted_labels = np.array(true_labels)[sorted_indices]
    relevant_at_k = sorted_labels[:k].sum()
    return relevant_at_k / k


# k_values = range(1, len(pred_scores) + 1)
# p_at_k_values = [recall_at_k(true_labels, pred_scores, k) for k in k_values]
# print(precision_at_k_values)
# print(recall_at_k_values)

plt.figure(figsize=(10, 6))
plt.plot(k_values, recall_at_k_values, marker='o')
plt.title(f'Recall@k (SAME={config.constants.SIM_VALUE_IS_SAME_COLOR}, EVAL={config.constants.IS_EVALUATED_TIMING_DRAW_COLOR},n={config.constants.EVALUATED_ILLUST_COUNT})')
plt.xlabel('K')
plt.ylabel('Recall')
plt.xticks(k_values)
plt.grid(True)

# グラフをファイルに保存
plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/{file_name}.png')
print(f"./tmp/output/{file_name}.png is saved")

plt.figure(figsize=(10, 6))
plt.plot(k_values, precision_at_k_values, marker='o')
plt.title(f'Precision@k (SAME={config.constants.SIM_VALUE_IS_SAME_COLOR}, EVAL={config.constants.IS_EVALUATED_TIMING_DRAW_COLOR}, n={config.constants.EVALUATED_ILLUST_COUNT})')
plt.xlabel('K')
plt.ylabel('Precision')
plt.xticks(k_values)
plt.grid(True)

# グラフをファイルに保存
file_name = (f'precision@k_SAME={config.constants.SIM_VALUE_IS_SAME_COLOR}_EVAL={config.constants.IS_EVALUATED_TIMING_DRAW_COLOR}')
plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/{file_name}.png')
print(f"./tmp/output/{file_name}.png is saved")

import matplotlib.pyplot as plt
import numpy as np
import json

with open('tmp/input/precision@k.json', 'r') as file:
    data = json.load(file)

precisions = data

print(precisions)

# サンプルデータ
# pred_scores = [0.9, 0.85, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4]
# true_labels = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0]

# p@kのデータポイント
k_values = [4, 6, 35, 81, 133, 223, 225]
p_at_k_values = [0.25, 0.17, 0.11, 0.06, 0.04, 0.02, 0.03]


def precision_at_k(true_labels, pred_scores, k):
    sorted_indices = np.argsort(pred_scores)[::-1]
    sorted_labels = np.array(true_labels)[sorted_indices]
    relevant_at_k = sorted_labels[:k].sum()
    return relevant_at_k / k


# k_values = range(1, len(pred_scores) + 1)
# p_at_k_values = [precision_at_k(true_labels, pred_scores, k) for k in k_values]

plt.figure(figsize=(10, 6))
plt.plot(k_values, p_at_k_values, marker='o')
plt.title('Precision at K')
plt.xlabel('K')
plt.ylabel('Precision')
plt.xticks(k_values)
plt.grid(True)

# グラフをファイルに保存
plt.savefig('/mnt/c/WSL-directory/my-NLP-project/tmp/output/precision_at_k_recommend_color_schemes.png')

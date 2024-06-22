import matplotlib.pyplot as plt
import numpy as np
import json

# jsonデータの読み込み
with open('tmp/input/precision@k(SAME=20).json', 'r') as file:
    data = json.load(file)
precisions = data

# 配列の宣言
p_at_k_values = []
k_values = []

# 配列に値の代入
for item in precisions:
    precision = item.get('precision')
    k = item.get('k')

    p_at_k_values.append(precision)
    k_values.append(k)


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
print("graph is saved")

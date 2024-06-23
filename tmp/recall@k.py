import matplotlib.pyplot as plt

# データの準備
k_values = [4, 6, 18, 52, 61, 104, 239, 398, 404]
recall_values = [0.1, 0.1, 0.1, 0.3, 0.3, 0.4, 0.5, 0.6, 0.7]

# グラフの作成
plt.plot(k_values, recall_values, marker='o')
plt.xlabel('k')
plt.ylabel('recall?')
plt.title('Recall@k??? ')
plt.grid(True)

# グラフをファイルに保存
plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/recall.png')
print("recall.png is saved")

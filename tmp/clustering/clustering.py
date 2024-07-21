import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster


def plot_clustering():
    # 元のデータセット
    original_data = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [3, 2],

        [5, 6],
        [5, 5],
        [6, 5],
        [4, 6],
        [6, 6],

        [8, 8],
        [8, 8],
        [8, 9],
        [8, 7],
        [7, 8],
    ])

    # 任意の10点を追加
    # additional_data = np.random.rand(10, 2) * 10  # 10x2のランダムデータ
    # data = np.vstack((original_data, additional_data))
    data = np.vstack((original_data))

    # 単連結法でクラスタリング
    Z = linkage(data, method='single', metric='euclidean')
    clusters = fcluster(Z, t=1.5, criterion='distance')  # クラスタ数を指定する場合、criterion='maxclust'

    # クラスタリング結果のプロットと保存
    plt.figure(figsize=(10, 10))
    plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='viridis')
    plt.title("Single Linkage Clustering on XY Plane")
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel("X")
    plt.ylabel("Y")

    file_name = "/mnt/c/WSL-directory/my-NLP-project/tmp/clustering/data/output/single_linkage_dendrogram.png"
    plt.savefig(f"{file_name}")

    print(f"{file_name} が保存されました．")

    plt.close()


def main():
    plot_clustering()


if __name__ == "__main__":
    main()

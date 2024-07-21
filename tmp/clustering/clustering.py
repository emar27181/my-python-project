import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster


def plot_clustering(clustring_kind):
    # 元のデータセット
    original_data = np.array([
        [0, 4],  # A
        [3, 1],  # B
        [4, 1],  # C
        [6, 3],  # D
        [4, 4],  # E

        [1, 2],
        [2, 3],
        [3, 4],
        [3, 2],
        [3, 5],

        [5, 6],
        [5, 5],
        [6, 5],
        [4, 6],
        [6, 6],

    ])

    data = np.vstack((original_data))

    # 単連結法でクラスタリング
    if (clustring_kind == "single"):
        Z = linkage(data, method='single', metric='euclidean')
    # 完全連結法でクラスタリング
    elif (clustring_kind == "complete"):
        Z = linkage(data, method='complete', metric='euclidean')

    clusters = fcluster(Z, t=1.5, criterion='distance')  # 距離を基準にクラスタリング
    # clusters = fcluster(Z, t=3, criterion='maxclust')  # クラスタ数を基準にクラスタリング

    # クラスタリング結果のプロットと保存
    plt.figure(figsize=(10, 10))
    markers = ['o', 's', '^', 'D', 'v', 'p', 'h', 'x', '+', '*']
    colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'black', 'orange', 'purple', 'pink']

    for cluster in np.unique(clusters):
        cluster_data = data[clusters == cluster]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1],
                    # c=[cluster] * len(cluster_data), cmap='viridis',
                    color=colors[cluster % len(colors)],
                    marker=markers[cluster % len(markers)],
                    label=f'Cluster {cluster}',

                    )

    # plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='viridis')
    plt.title(f"{clustring_kind} Linkage Clustering on XY Plane")
    plt.grid(True)
    plt.xlim(-1, 8)
    plt.ylim(-1, 8)
    plt.xlabel("X")
    plt.ylabel("Y")

    file_name = (f"/mnt/c/WSL-directory/my-NLP-project/tmp/clustering/data/output/{clustring_kind}_linkage_xy.png")
    plt.savefig(f"{file_name}")

    print(f"{file_name} が保存されました．")

    plt.close()


def main():
    plot_clustering("single")
    plot_clustering("complete")


if __name__ == "__main__":
    main()

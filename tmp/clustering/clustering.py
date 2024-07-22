import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.cluster import KMeans


def plot_clustering(clustring_method):
    # 元のデータセット
    original_data = np.array([
        [0, 4],  # A
        [3, 1],  # B
        [4, 1],  # C
        [6, 3],  # D
        [4, 4],  # E

        [1, 3],
        [0, 3],
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

    # K-means法でクラスタリング
    if (clustring_method == "kmeans"):
        kmeans = KMeans(n_clusters=3, n_init=10, random_state=0).fit(data)
        clusters = kmeans.labels_
    else:
        # 単連結法でクラスタリング
        if (clustring_method == "single"):
            Z = linkage(data, method='single', metric='euclidean')
        # 完全連結法でクラスタリング
        elif (clustring_method == "complete"):
            Z = linkage(data, method='complete', metric='euclidean')

        clusters = fcluster(Z, t=1.5, criterion='distance')  # 距離を基準にクラスタリング
        # clusters = fcluster(Z, t=3, criterion='maxclust')  # クラスタ数を基準にクラスタリング

    # クラスタリング結果のプロット
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
    plt.title(f"{clustring_method} Linkage Clustering on XY Plane")
    plt.grid(True)
    plt.xlim(-1, 8)
    plt.ylim(-1, 8)
    plt.xlabel("X")
    plt.ylabel("Y")

    file_name = (f"/mnt/c/WSL-directory/my-NLP-project/tmp/clustering/data/output/{clustring_method}_linkage_xy.png")
    plt.savefig(f"{file_name}")

    print(f"{file_name} が保存されました．")

    plt.close()


def main():
    plot_clustering("single")
    plot_clustering("complete")
    plot_clustering("kmeans")


if __name__ == "__main__":
    main()

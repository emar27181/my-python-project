import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist, squareform
# my-nlp-venv/lib64/python3.10/site-packages/scipy/cluster/hierarchy.py
from sklearn.cluster import KMeans


# 単連結法によるクラスタリング
def single_linkage(X):
    n = len(X)
    Z = np.zeros((n - 1, 4))  # 結果を格納する配列
    D = squareform(pdist(X))  # 距離行列
    np.fill_diagonal(D, np.inf)  # 対角要素は無限大にする

    clusters = {i: [i] for i in range(n)}  # 各データポイントをクラスタに格納
    cluster_indices = {i: i for i in range(n)}  # 各データポイントのインデックス

    for k in range(n - 1):
        i, j = np.unravel_index(np.argmin(D), D.shape)  # 最小距離を持つクラスタの探索
        min_dist = D[i, j]  # 最小距離

        # クラスタの結合
        new_cluster = clusters[i] + clusters[j]
        Z[k] = [cluster_indices[i], cluster_indices[j], min_dist, len(new_cluster)]

        # 距離行列の更新
        for m in range(n):
            if m != i and m != j:
                D[i, m] = D[m, i] = min(D[i, m], D[j, m])

        D[j, :] = D[:, j] = np.inf  # j行とj列を無限大に設定

        # クラスタの管理
        clusters[i] = new_cluster
        clusters[j] = []  # jクラスタを空にすることで再利用を防ぐ
        cluster_indices[i] = k + n  # 新しいクラスタのインデックスを設定

    return Z


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

            # Z = linkage(data, method='single', metric='euclidean')
            Z = single_linkage(data)
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

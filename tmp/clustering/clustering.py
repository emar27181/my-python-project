import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist, squareform
# my-nlp-venv/lib64/python3.10/site-packages/scipy/cluster/hierarchy.py
from sklearn.cluster import KMeans


# 完全連結法によるクラスタリング
def complete_linkage(base_matrix):
    n = len(base_matrix)
    clusterd_matrix = np.zeros((n - 1, 4))
    distance_matrix = squareform(pdist(base_matrix))
    np.fill_diagonal(distance_matrix, np.inf)  # 対角要素は無限大にする

    clusters = {i: [i] for i in range(n)}  # 各データポイントをクラスタに格納
    cluster_indices = {i: i for i in range(n)}  # 各データポイントのインデックス

    for k in range(n - 1):
        i, j = np.unravel_index(np.argmin(distance_matrix), distance_matrix.shape)  # 最小距離を持つクラスタの探索
        min_dist = distance_matrix[i, j]  # 最小距離

        # クラスタの結合
        new_cluster = clusters[i] + clusters[j]
        clusterd_matrix[k] = [cluster_indices[i], cluster_indices[j], min_dist, len(new_cluster)]

        # 距離行列の更新
        for m in range(n):
            if m != i and m != j:
                distance_matrix[i, m] = distance_matrix[m, i] = max(distance_matrix[i, m], distance_matrix[j, m])

        distance_matrix[j, :] = distance_matrix[:, j] = np.inf  # j行とj列を無限大に設定

        # クラスタの管理
        clusters[i] = new_cluster
        clusters[j] = []  # jクラスタを空にすることで再利用を防ぐ
        cluster_indices[i] = k + n  # 新しいクラスタのインデックスを設定

    return clusterd_matrix


# 単連結法によるクラスタリング
def single_linkage(base_matrix):
    n = len(base_matrix)
    clusterd_matrix = np.zeros((n - 1, 4))
    distance_matrix = squareform(pdist(base_matrix))
    np.fill_diagonal(distance_matrix, np.inf)  # 対角要素は無限大にする

    clusters = {i: [i] for i in range(n)}  # 各データポイントをクラスタに格納
    cluster_indices = {i: i for i in range(n)}  # 各データポイントのインデックス

    for k in range(n - 1):
        i, j = np.unravel_index(np.argmin(distance_matrix), distance_matrix.shape)  # 最小距離を持つクラスタの探索
        min_dist = distance_matrix[i, j]  # 最小距離

        # クラスタの結合
        new_cluster = clusters[i] + clusters[j]
        clusterd_matrix[k] = [cluster_indices[i], cluster_indices[j], min_dist, len(new_cluster)]

        # 距離行列の更新
        for m in range(n):
            if m != i and m != j:
                distance_matrix[i, m] = distance_matrix[m, i] = min(distance_matrix[i, m], distance_matrix[j, m])

        distance_matrix[j, :] = distance_matrix[:, j] = np.inf  # j行とj列を無限大に設定

        # クラスタの管理
        clusters[i] = new_cluster
        clusters[j] = []  # jクラスタを空にすることで再利用を防ぐ
        cluster_indices[i] = k + n  # 新しいクラスタのインデックスを設定

    return clusterd_matrix


def plot_clustering(clustring_method, input_matrix):
    # K-means法でクラスタリング
    if (clustring_method == "kmeans"):
        kmeans = KMeans(n_clusters=3, n_init=10, random_state=0).fit(input_matrix)
        clusters = kmeans.labels_
    else:
        # 単連結法でクラスタリング
        if (clustring_method == "single"):

            # Z = linkage(data, method='single', metric='euclidean')
            Z = single_linkage(input_matrix)
        # 完全連結法でクラスタリング
        elif (clustring_method == "complete"):
            # Z = linkage(data, method='complete', metric='euclidean')
            Z = complete_linkage(input_matrix)

        clusters = fcluster(Z, t=1.5, criterion='distance')  # 距離を基準にクラスタリング
        # clusters = fcluster(Z, t=3, criterion='maxclust')  # クラスタ数を基準にクラスタリング

    # クラスタリング結果のプロット
    plt.figure(figsize=(10, 10))
    markers = ['o', 's', '^', 'D', 'v', 'p', 'h', 'x', '+', '*']
    colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'black', 'orange', 'purple', 'pink']

    for cluster in np.unique(clusters):
        cluster_data = input_matrix[clusters == cluster]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1],
                    color=colors[cluster % len(colors)],
                    marker=markers[cluster % len(markers)],
                    label=f'Cluster {cluster}',
                    # color="red",
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

    # 元のデータセット
    input_data = np.array([
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

    print(input_data)
    print("")

    plot_clustering("single", input_data)
    plot_clustering("complete", input_data)
    plot_clustering("kmeans", input_data)


if __name__ == "__main__":
    main()

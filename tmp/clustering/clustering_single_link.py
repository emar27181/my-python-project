import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

# 初期データ点
np.random.seed(0)
initial_points = np.random.rand(10, 2)

# 任意の10点を追加
additional_points = np.random.rand(10, 2)

# 全データ点
data = np.vstack((initial_points, additional_points))

# 距離行列の計算
dist_matrix = sch.distance.pdist(data, metric='euclidean')

# 単連結法でクラスタリング
Z_single = sch.linkage(dist_matrix, method='single')

# デンドログラムのプロット
plt.figure(figsize=(10, 7))
sch.dendrogram(Z_single)
plt.title('Single Linkage Clustering')
plt.savefig('single_linkage_clustering.png')
plt.close()

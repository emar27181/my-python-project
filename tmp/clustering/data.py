import numpy as np
import matplotlib.pyplot as plt

# 初期データ点
np.random.seed(0)
initial_points = np.random.rand(10, 2)

# 任意の10点を追加
additional_points = np.random.rand(10, 2)

# 全データ点
data = np.vstack((initial_points, additional_points))

plt.scatter(data[:, 0], data[:, 1])
plt.title('Data Points')
plt.show()

plt.savefig(f'/mnt/c/WSL-directory/my-NLP-project/tmp/output/output_clustering.png')
print("output_clustering.png is saved")

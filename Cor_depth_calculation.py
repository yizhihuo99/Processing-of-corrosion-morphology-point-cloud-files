import pandas as pd
import numpy as np

# 读取点云CSV文件(Read point cloud CSV file)
df = pd.read_csv("./steel/1.csv", header=None)

# 读取该腐蚀表面X、Y、Z的最大最小值(Read the maximum and minimum values of X, Y, and Z on the corroded surface)
X_max, X_min = df[0].max(), df[0].min()
Y_max, Y_min = df[1].max(), df[1].min()
Z_max = df[2].max()
print(f"Z坐标的最大值: {Z_max} 微米")

# 计算腐蚀区域面积A(Calculate the corrosion area A)
A = (X_max - X_min) * (Y_max - Y_min)

# 计算未腐蚀前的理论体积V0(Calculate the theoretical volume V0 before corrosion)
V0 = A * Z_max
print(A,V0)
# 计算网格步长 dx, dy（用唯一X、Y坐标数估计）
dx = (X_max - X_min) / len(df[0].unique())
dy = (Y_max - Y_min) / len(df[1].unique())

# 计算腐蚀后剩余体积 V1(Calculate the remaining volume V1 after corrosion)
V1 = np.sum(df[2]) * dx * dy

# 计算腐蚀损失体积 V2(Calculate the volume of corrosion loss V2)
V2 = V0 - V1

# 计算等效均匀腐蚀深度 d（单位为微米）Calculate the equivalent uniform corrosion depth d (in micrometers)
d = V2 / A

# 将腐蚀深度 d 转换为毫米(Convert corrosion depth d to millimeters)
d_mm = d / 1000

print(f"等效均匀腐蚀深度 d: {d:.6f} 微米")
print(f"等效均匀腐蚀深度 d: {d_mm:.6f} 毫米")
print(f"Z_max: {Z_max} 微米,  dx: {dx} 微米, dy: {dy} 微米")

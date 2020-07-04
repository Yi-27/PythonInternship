#coding:utf-8

"""
求解距离矩阵，首先生成100个二维坐标点,然后计算任意两点之间的距离

分析：
	这里的距离指的是欧式距离，就是两个坐标之间的距离

	100个二维坐标点就意味着有100个x坐标和100个y坐标

	任意两个坐标点的距离，就是一个(x, y)到100个(x, y)的距离（包括本身）

	并将得到的距离，作为(1, 100)的数组

	最终全部坐标得到 (100, 100)的二维数组

"""

import numpy as np

x = np.random.randint(0, 100, size=100) # 随机100个数的一维数组
y = np.random.randint(100, 200, size=100)

arr = [] # 返回的结果的列表，先是一维列表，后面再转换成矩阵并变化形状

for i in range(100):
	for j in range(100):
		# 公式：根号下(x1-x2)^2+(y1-y2)^2
		distance = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
		arr.append(distance)

# 直接将list转换成矩阵
arr = np.matrix(arr)
arr = arr.reshape(100, 100) # 转换成100*100的矩阵
print(arr)
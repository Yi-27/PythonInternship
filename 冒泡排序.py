#coding:utf-8


x = [1, 2, 6, 0.3, 2, 0.5, -1, 2, 4]

# 冒泡排序
for i in range(len(x)):
	for j in range(i):
		if x[j] > x[i]:
			x[i], x[j] = x[j], x[i] # 不需要中间变量

print(x) # [-1, 0.3, 0.5, 1, 2, 2, 2, 4, 6]

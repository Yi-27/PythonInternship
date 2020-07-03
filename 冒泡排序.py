#coding:utf-8

import random
import time 
# x = [1, 2, 6, 0.3, 2, 0.5, -1, 2, 4]
# print(x)

x = list(range(10000))
random.shuffle(x) # 打乱list
y = x.copy() # 拷贝list
n = len(x)

start1 = time.clock()
# 冒泡排序1
for i in range(n):
	for j in range(i):
		if x[j] > x[i]:
			x[i], x[j] = x[j], x[i] # 不需要中间变量

end1 = time.clock()
print(f"{end1 - start1}秒") # 9.1822401秒
# print(x) # [-1, 0.3, 0.5, 1, 2, 2, 2, 4, 6]


start2 = time.clock()
# 经典·冒泡排序  慢慢慢
for i in range(n - 1): # 只要比较n-1个数
	for j in range(n - i - 1): # 
		if y[j] > y[j + 1]:
			y[j], y[j + 1] = y[j + 1], y[j]
# print(x)
end2 = time.clock()
print(f"{end2 - start2}秒") # 12.349049999999998秒
#coding:utf-8

# 这里就是一些测试

sum0 = 0
for i in range(1, 11):
	if i%2 == 0:
		continue
	if i%10 == 5:
		break
	print(i)
	sum0 += i
print(sum0)

for i in range(2,5):
	print(i, end=',')

l1 = ['a', 'b', 'c', 'd']
l2 = ['A', 'B', 'C', 'D']

print([i + j for i,j in zip(l1, l2)])

a = 2,3,4,5
print(a)
print(type(a))

b = list("abcde")
print(b)

l3 = [3,4,5,6,7,8]
l3.insert(2,3)
print(l3)
print(l3[4:])
print(list(range(1,15,3)))

print(list(range(1,11)))

print(type(range(1,11)))

x = 2
x *= 2**2**3//100
print(2**2)
print(2**3)
print(2**8)
print(2**2**3)
print(2**2**3//100)
print(x)

print(int("2"))

i = True + 2

exa = 'example'
print(exa.replace('a', 'b'))

def InputInt(a):
	a = 15
b = 2
InputInt(b)
print(b)

import math
def f(n):
	assert n>0, 'n '
	return math.sqrt(n)
print(f(4))

result = list(map(lambda x: x*x, [1,2,3,4,5,6,7,8,9]))
print(result)

print(tuple(map(lambda x: x, [1,3,6])))

# 模块的查找顺序是：内存中已经加载的模块->内置模块->sys.path路径中包含的模块

from math import pi
print(pi)

import math
print(math.sin(20))

x = [1, 2, 6, 0.3, 2, 0.5, -1, 2, 4]
print(len(x))
for i in range(len(x)):
	print(i)

for j in range(0):
	print(j)

import random
x = list(range(10))
random.shuffle(x)
print(x)

y = [1, 2, 3]
z = y
z[0] = 4
print(y)
print(y.__len__())


def tes():
	pass

print(type(tes))
import numpy as np

print(np.arange(10, 20))

import pandas as pd

data = pd.read_csv("./data/meal_order_info.csv", encoding='gbk')
data['lock_time'] = pd.to_datetime(data['lock_time']) # 更新该列数据
print(data['use_start_time'].dtype)
print(pd.PeriodIndex(data['use_start_time'].values, freq='S')) # 指定时间间隔为 S秒  一组Period构成的Index

import datetime

now = datetime.datetime.now()
print(now)

import time
print(time.time())
# 1594546996 428
# 1594548638 634
# 1594548760 667
# 1594549307 2850437
timeStamp = 1594549307
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)


d = {"1": "123", "2": 345, "3": "abc"}
print(d.pop("2"))
print(d)

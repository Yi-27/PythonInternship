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
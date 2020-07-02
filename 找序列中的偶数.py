#coding:utf-8

x = [1, 2, 3, 4, 5, 6]
def even_number(list_num):
	for i in list_num:
		if i % 2 == 0:
			print(i, end=" ")
	print([i for i in list_num if i % 2 == 0])

even_number(x) # 2 4 6 [2, 4, 6]
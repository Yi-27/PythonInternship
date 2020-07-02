#coding:utf-8

year = int(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0:
	print(year, " 年是普通闰年")
elif year % 400 == 0:
	print(year, " 年是世纪闰年")
else:
	print(year, " 年不是闰年")

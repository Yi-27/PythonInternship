#coding:utf-8

class Rectangle(object):

	def __init__(self, length, width):
		self.length = length
		self.width = width

	# 计算矩形周长
	def get_circumference(self):
		return 2 * (self.length + self.width)

	# 计算矩形面积
	def get_area(self):
		return self.length * self.width

if __name__ == '__main__':
	# 实例化一个矩形对象
	rect = Rectangle(3, 4)
	print("矩形周长：", rect.get_circumference()) # 矩形周长： 14
	print("矩形面积：", rect.get_area()) # 矩形面积： 12
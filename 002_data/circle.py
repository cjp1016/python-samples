"""
输入半径计算圆的周长和面积

周长：C=2πr，
面积：S=πr2

Author: cjp
Version: 0.1
"""
import math

radius = float(input("请输入半径: "))
c = 2*math.pi*radius
s = math.pi*radius*radius

print('周长是：%.2f' %c)
print('面积是：%.2f' %s)

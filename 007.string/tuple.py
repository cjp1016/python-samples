# -*- coding: utf-8 -*-

"""
tuple
Python中的元组与列表类似也是一种容器数据类型，
可以用一个变量（对象）来存储多个数据，
不同之处在于元组的元素不能修改

Author: cjp
Version: 1.0
"""
t = ('陈',30,True,"武汉")
print(t)

# t(1) = 40 #  Type Error

# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
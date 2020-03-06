# -*- coding: utf-8 -*-
"""
定义列表可以将列表的元素放在[]中，多个元素用,进行分隔，
可以使用for循环对列表元素进行遍历，
也可以使用[]或[:]运算符取出列表中的一个或多个元素
"""
import sys

list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) # ['hello', 'hello', 'hello']
# 计算列表长度(元素个数)
print(len(list1)) # 5
# 下标(索引)运算
print(list1[0]) # 1
print(list1[4]) # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1]) # 100
print(list1[-3]) # 5
list1[2] = 300
print(list1) # [1, 3, 300, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)



print('\n下面的代码演示了如何向列表中添加元素以及如何从列表中移除元素。\n')

list2 = [1, 3, 5, 7, 100]
# 添加元素
list2.append(200)
list2.insert(1, 400)
# 合并两个列表
# list2.extend([1000, 2000])
list2 += [1000, 2000]
print(list2) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list2)) # 9
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list2:
	list2.remove(3)
if 1234 in list2:
    list2.remove(1234)
print(list2) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list2.pop(0)
list2.pop(len(list2) - 1)
print(list2) # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list2.clear()
print(list2) # []


print('\n-------------- list 切片-------------------\n')

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


print('\n-------------- list 排序-------------------\n')

list4 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list5 = sorted(list4)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list6 = sorted(list4, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list7 = sorted(list4, key=len)
print(list4)
print(list5)
print(list6)
print(list7)
# 给列表对象发出排序消息直接在列表对象上进行排序
list4.sort(reverse=True)
print(list4)


print('\n-------------- list 生成式和生成器-------------------\n')


f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    pass
    # print(val)
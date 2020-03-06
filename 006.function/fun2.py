"""
在Python中，函数的参数可以有默认值，也支持使用可变参数，
所以Python并不需要像其他语言一样支持函数的重载，
因为我们在定义一个函数的时候可以让它有多种不同的使用方式.

Version: 0.1
Author: cjp
"""

from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


print("==================================")
"""
其实上面的add函数还有更好的实现方案，因为我们可能会对0个或多个参数进行加法运算，
而具体有多少个参数是由调用者来决定，我们作为函数的设计者对这一点是一无所知的，
因此在不确定参数个数的时候，我们可以使用可变参数，代码如下所示。

由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，
也就意味着两个函数同名函数实际上只有一个是存在的
"""

# 在参数名前面的*表示args是一个可变参数
def add2(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add2())
print(add2(1))
print(add2(1, 2))
print(add2(1, 2, 3))
print(add2(1, 3, 5, 7, 9))


print("==================================")

def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？
foo()

"""
项目是由多人协作进行团队开发的时候，团队中可能有多个程序员都定义了名为foo的函数，
那么怎么解决这种命名冲突呢？答案其实很简单，Python中每个文件就代表了一个模块（module），
我们在不同的模块中可以有同名的函数，
在使用函数的时候我们通过import关键字导入指定的模块就可以区分到底要使用的是哪个模块中的foo函数，
代码如下所示。
module1.py

def foo():
    print('hello, world!')
    
module2.py

def foo():
    print('goodbye, world!')    
"""
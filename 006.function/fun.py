"""
输入M和N计算C(M,N)

排列组合公式:https://www.cnblogs.com/1024th/p/10623541.html
Amn=n(n−1)(n−2)⋯(n−m+1)=n!(n−m)!,

Cmn=Amn/Amm=n(n−1)(n−2)⋯(n−m+1)/m!=n!/m!*(n−m)!,n,m∈N∗,并且m≤n

如 7,3 = 35

我们做了3次求阶乘，

range()函数和for-in循环

函数原型：range（start， end， scan):

参数含义：start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
         end:技术到end结束，但不包括end 。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
         scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

Version: 0.1
Author: cjp
"""

m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print("fm:",fm) # 7
print("fn:",fn) # 3
print("fmn:",fmn)
print(fm // fn // fmn) # 35


"""
Python的math模块中其实已经有一个factorial函数了，
事实上要计算阶乘可以直接使用这个现成的函数而不用自己定义。
下面例子中的一些函数在Python中也都是现成的，
我们这里是为了讲解函数的定义和使用才把它们又实现了一遍，
实际开发中不建议做这种低级的重复性的工作。
"""
def factorial(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

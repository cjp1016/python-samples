"""
输入一个正整数判断是不是素数。
素数指的是只能被1和自身整除的大于1的整数。

思路1)：因此判断一个整数m是否是素数，只需把 m 被 2 ~ m-1 之间的每一个整数去除，如果都不能被整除，那么 m 就是一个素数。
思路2)：如果 m 不能被 2 ~ m求平方根 间任一整数整除，m 必定是素数。
Version:0.1
Author:cjp
"""
a = int(input("请输入正整数："))
b = False
for i in range(2,a-1):
    if(a%i == 0):
        b = True
        break

if not b and a != 1:
    print("%d 是素数" % a)
else:
    print("%d 不是素数" % a)


# 思路2
from math import sqrt

n = int(input('请输入一个正整数: '))
m = int(sqrt(n))
is_prime = True
for x in range(2, m + 1):
    if n % x == 0:
        is_prime = False
        break
if is_prime and n != 1:
    print('%d是素数' % n)
else:
    print('%d不是素数' % n)
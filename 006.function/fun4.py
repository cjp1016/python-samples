# -*- coding: utf-8 -*-
"""
求列表最大值和最小值
# Author: cjp
# Version: 1.0.0
"""

def findMinAndMax(L):
    if L:
        min = L[0]
        max = L[0]
        for x in L:
            if max < x:
                max = x
            if min > x:
                min = x 
        return (min, max)
    else:
        return (None, None)



# 测试
if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('测试成功!')
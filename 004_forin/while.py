"""
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。
while循环通过一个能够产生或转换出bool值的表达式来控制循环，
表达式的值为True循环继续，表达式的值为False循环结束

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version:0.1
Author: cjp
"""
import random

m = random.randint(1,100)
b = True
counter = 0
while b: 
    counter += 1
    n = int(input('请输入:'))
    if n > m:
        print('猜大了，继续')
    elif n < m:
        print('猜小了，继续')
    else:
        b = False
        print('猜对了')
        # break

print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
"""
用户身份验证

Version: 0.1
Author: cjp
"""

username = input('请输入用户名: ')
password = input('请输入口令: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')

"""
Python中没有用花括号来构造代码块而是使用了缩进的方式来设置代码的层次结构，
如果if条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了，
换句话说连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，相当于是一个执行的整体。
"""

# 当然如果要构造出更多的分支，可以使用if…elif…else…结构，例如下面的分段函数求值。


"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: cjp
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))


"""
同理elif和else中也可以再构造新的分支，我们称之为嵌套的分支结构
"""
"""
分段函数求值

		        3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		        5x + 3	(x < -1)

Version: 0.1
Author: cjp
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else: 
    if x >= -1:
        y = x+2
    else:
        y = 5 * x + 3

print('f(%.2f) = %.2f' % (x, y))


"""
大家可以自己感受一下这两种写法到底是哪一种更好。
在之前我们提到的Python之禅中有这么一句话“Flat is better than nested.”，
之所以提倡代码“扁平化”是因为嵌套结构的嵌套层次多了之后会严重的影响代码的可读性
，所以能使用扁平化的结构时就不要使用嵌套。
"""
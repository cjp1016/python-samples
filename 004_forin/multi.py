"""
输出99乘法口诀表（九九表）
\t	横向制表符
\r	回车
\f	换页

Version: 0.1
Author: cjp
"""
for i in range(1,10):
    for f in range(1,i+1):
        print('%d * %d = %d' % (i,f,i*f) ,end ='\t')
    print() # 输出空行

# -*- coding: utf-8 -*-

"""
字符串使用
单引号和双引号表示字符串
三个双引号或单引号开头的字符串可以拆行
字符串用反斜杠\表示转义
Author: cjp
Version: 1.0
"""
s1 = 'hello,s1'
s2 = "hello,s2"
# 三个换行
s3 = """
hello,
s3
"""
print(s1,s2,s3,end='-----------------\n')

"""
\后面可以接八进制、十六进制，也可以接unicode字符编码表示

"""
s5 = '\141\142\143\x61\x62\x63'
s6 = '\u9a86\u660a'
print(s5, s6,end='\n-----------------\n')


"""
Python为字符串类型提供了非常丰富的运算符，我们可以使用+运算符来实现字符串的拼接，
可以使用*运算符来重复一个字符串的内容，
可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算），
"""

s7 = 'hello ' * 3   # 重复前面字符串3次
print(s7) # hello hello hello 

s8 = 'world'
s7 += s8
print(s7) # hello hello hello world

print('ll' in s7) # True
print('good' not in s7) # True


str2 = 'abc123456'
print(str2[:-1]) # 获取第0个字符到倒数字符
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
# string从第2个开始，每两个取一个：
print(str2[2::2]) # c246
# string从第0个开始，每两个取一个：
print(str2[::2]) # ac246
print(str2[::-2]) # 642ca  字符串翻转
# string，每-1个取一个,意思是反着取每一个
print(str2[::-1]) # 654321cba  字符串翻转
print(''.join(reversed(str2))) # 使用reversed()反转
print(str2[-3:-1]) # 45
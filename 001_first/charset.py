#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. 最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，
这个编码表被称为ASCII编码,比如大写字母A的编码是65.

2.Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了
ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。
3. 本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码
搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

"""
print(ord("A"))  # 65

print(ord("中")) # 20013

print(chr(66))  # B

print(chr(20013))

print(len('ABC'))
print(len('中文'))


print(len(b'ABC')) # 换成bytes，len()函数就计算字节数
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

# 1个中文字符经过UTF-8编码后通常会占用3个字节
# 而1个英文字符只占用1个字节。
print(len('中文'.encode('utf-8')))


# Python 3的字符串使用Unicode，直接支持多语言。
# 当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。
# Python当然也支持其他编码方式，比如把Unicode编码成GB2312：

print( '中文'.encode('gb2312'))
print( '中文'.encode('utf-8'))




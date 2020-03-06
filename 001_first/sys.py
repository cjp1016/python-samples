# -*- coding: utf-8 -*-
"""
第一个python程序
vscode 
{
    "python.pythonPath": "C:\\Program Files\\Python36\\python.exe",
    "python.linting.pylintArgs": ["--generate-members"]
}
VSCode——使用CodeRunner开发python输出中文出现乱码的解决方法
https://blog.csdn.net/yukinoai/article/details/81624936
Version: 0.1
Author: cjp
"""
import sys
# import io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码


# 输出python版本
# sys.version_info(major=3, minor=6, micro=7, releaselevel='final', serial=0)
print(sys.version_info)

# 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)]
print(sys.version)

# 输出其他
print("hello,python")

print('你好','世界')

print('hello','world',sep=',' ,end='!')

print('goodbye,workd',end='!\n')
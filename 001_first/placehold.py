"""
占位符	替换内容
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
Version : 0.1
Author : cjp
"""

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Age: %s. Gender: %s' % (25, True))

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
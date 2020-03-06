"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

两边之和大于第三边

1.已知三角形底a，高h，则 
2.已知三角形三边a,b,c，则
（海伦公式）p= (a+b+c)/2
S=sqrt[p(p-a)(p-b)(p-c)]   sqrt()的用法: 计算一个非负实数的平方根 
=sqrt[(1/16)(a+b+c)(a+b-c)(a+c-b)(b+c-a)]
=1/4sqrt[(a+b+c)(a+b-c)(a+c-b)(b+c-a)]


**	指数
Version: 0.1
Author: cjp
"""
a = float(input("边长a= "))
b = float(input("边长b= "))
c = float(input("边长c= "))

if a+b>c and a+c>b and b+c>a :
    print('周长 = %f' % (a+b+c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积 = %f ' %area)
else:
    print("不能构成三角形")
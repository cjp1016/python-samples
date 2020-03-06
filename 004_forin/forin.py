"""
用for循环实现1~100求和

需要说明的是上面代码中的range(101)可以用来构造一个从0到100的取值范围
Version: 0.1
Author: cjp
"""
sum = 0
for i in range(101):
    sum += i

print('1到100求和是',sum)

"""
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。
知道了这一点，我们可以用下面的代码来实现1~100之间的偶数求和。
"""
even_sum = 0
for i in range(0,101,2):   # 注意不是(0,100,2) 会少算最后的100
    even_sum += i

print('1到100间偶数求和是',even_sum)

# 也可以通过在循环中使用分支结构的方式来实现相同的功能，代码如下所示。

even_sum2 = 0
for i in range(0,101):   # 注意不是(0,100,2) 会少算最后的100
    if(i % 2 ==0):
        even_sum2 +=i

print('1到100间偶数求和是',even_sum2)
"""
百分制程序转换为等级制成绩
如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E。
"""
score = float(input("请输入成绩分数："))

if score >= 90:
    # print("成绩是A")
    grade = 'A'
elif score < 90 and score >= 80:
    # print("成绩是B")
    grade = 'B'
elif score < 80 and score >= 70:
    # print("成绩是C")
    grade = 'C'
elif score < 70 and score >= 60:
    # print("成绩是D")
    grade = 'D'
else:
    # print("成绩是E")
    grade = 'E'

print('成绩分数是：%.1f,对应等级是%s' %(score,grade))
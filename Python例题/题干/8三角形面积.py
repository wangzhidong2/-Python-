#
# 注意：
# （1）请勿增加或删除行；
# （2）请勿更改程序的结构；
# （3）请勿修改代码行缩进。
#


import math
a=【?】(input("请输入第一条边长："))                               #【?】处更换为正确答案
b=float(input("请输入第二条边长："))
c=float(input("请输入第三条边长："))
if(a+b>c)and(a+c>b)and(b+c>a)                                      #此行有一处错误
    p=(a+b+c)/3                                                    #此行有一处错误
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(a,b,c,"能构成三角形！","三角形的面积为：","%.2f"%p)      #此行有一处错误
else:
    print(a,b,c,"不能构成三角形！")

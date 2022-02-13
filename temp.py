# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''name="Scott handsome"
print(name[0:-1])
s=len(name)
print(s)
print(str(name),str(s))
print(str.lower(name))
print(str.upper(name))
name="Scott handsome"
#print(name.count("t",0,10))
print(name.replace("t","n"))
print(name.replace("t","n",1))
print(name.replace("t","n",2))
print(name.replace("t","n",3))
t='China'
for a in t:
    print(a,end=',')
print(10/3)
print(10//3)
print(10//6)
a=4
while a>0:
    a = a+1
    print(a)
for a in "scott":
    if a =="s":
            continue
    print(a,end=",")'
from random import*
print(randrange(1,100,5))
t='China'
print(t[::])
t='China'
print(max(t))
print(min(t))
a = 'cat','dog','fish','tiger','scott'
print(a)
print(a[1][2])
i = [243,422,333,"sd",332]
i[0]=2
del i[2]
i.append(33222)
b = [2,3,4]
i[0:1] = b
i.insert(3,10)
print(i)
b.clear()
print(b )'''
"""
Created on Sun Mar 21 23:57:40 2021

@author: balabala
"""
'''
【问题描述】一元二次方程：ax2+bx+c=0 （a ╪ 0）
【输入形式】输入a、b和c的值（有理数）
【输出形式】输出x的两个值，或者No（即没有有理数的解）
【样例输入】1 2.5 3
【样例输出】No
【样例输入】1 -2 1
【样例输出】1.00 1.00

【样例输出说明】输出的两个解保留两位小数，大的在前。

import math
a=input("a的值: ")
b=input("b的值: ")
c=input("c的值: ")
e=b*b-4*a*c
d=math.sqrt(e)
if d>0:
    x=(-b+d)/2*a
    y=(-b-d)/2*a
    print("{:.2f},{:.2f}".format(max(x,y),min(x,y)))
else:
    print("NO")
import math
a,b,c=map(float,input().split())
d=b**2-4*a*c
if a==0:
    print("a can not be 0")
if d<0:
    print("NO")
if d>=0:
    x1 = (-b-math.sqrt(d))/2*a
    x2 = (-b+math.sqrt(d))/2*a
    print("%1f,%1f"%(max(x1,x2),min(x1,x2)))
input_str = input("请输入一行字符：")
str_list = [0, 0, 0]
for i in input_str:
    if i.isalpha():
        str_list[0] += 1
    if i.isspace():
        str_list[1] += 1
    if i.isdigit():
        str_list[2] += 1

str_tuple = tuple(str_list)
print("英文字母个数为：%d\n"
      "空格个数为%d\n"
      "数字个数为%d" %str_tuple) '''
'''【问题描述】编写程序实现在字符串s中删除子字符串c的功能。
            
            说明：不考虑去掉子字符串c后形成的新的子字符串c。
            例如：字符串s为abcabcd，子串c为bc，则调用该函数后，结果字符串s为aad。
【输入形式】输入的第一行表示字符串s，第二行表示子串c。
【输出形式】输出的一行表示处理后的结果。
【样例输入】
abcabcd
bc
【样例输出】
aad'''

    

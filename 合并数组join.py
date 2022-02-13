# -*- coding: utf-8 -*-
"""
合并数组 
.join 列
.merge
"""
import pandas as pd
import numpy as np
#.join
data1 = pd.DataFrame(np.ones((2,4)),index=["A","B"],columns=list("abcd"))
print(data1)
data2 = pd.DataFrame(np.zeros((3,3)),index=["A","B","C"],columns=list("xyz"))
#print(data2)
data3 = data1.join(data2)
#print(data3)
data4 = data2.join(data1)
#print(data4)


#.merge
'''
一、条件
1.有相同名字的列
2.那一行的值相同
二、方式
1.一行匹配合并一行
'''
data5 = pd.DataFrame(np.arange(9).reshape((3,3)),columns=list("fax"))
print(data5)
data6 = data1.merge(data5,on='a')
#print(data6)
#how inner交集 outer并集nan补齐 
data7 = data1.merge(data5,on='a',how='outer')
print(data7)




















































# -*- coding: utf-8 -*-
"""
数据处理
"""
import pandas as pd
import numpy as np
t1 = pd.DataFrame(np.arange(20).reshape(4,5),index=list("abcd"),columns=list("ABCDE"))
#处理为0的数据
t1[t1==0]=np.nan
#print(t1)
#判断数据是否nan值
#print(t1.isnull())
#找出不含有nan的列 输出不含有nan的行
i1 = t1[pd.notnull(t1["A"])]
#print(i1)
#删除含有nan的行或列
#print(t1.dropna(axis=0))#删除行
#print(t1.dropna(axis=1))#删除列
#how="any"是删除含有nan的 how="all"是删除全是nan的行或列
#print(t1.dropna(axis=1,how="any"))
#inplace
t2 = t1.dropna(axis=1,how="any",inplace=True)
print(t2)





































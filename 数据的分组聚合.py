# -*- coding: utf-8 -*-
"""
数据的分组聚合
groupby
"""
import pandas as pd
#读取数据
data = pd.read_csv("E:\starbucks_store_worldwide.csv")
#观察数据
#print(data)
#print(data.info())


#pd.groupby按照by的列名分组 分出来为 列名+所跟着的数据的dataframe 其数据类型为DataFrameGroupBy
#DataFrameGroupBy
'''
1.可以遍历
2.调用聚合方法
'''
#按照国家分组
grouped = data.groupby(by="Country")
#print(grouped)

#选出特定的国家数据
#print(data[data["Country"]=="US"])

#遍历
#for i,j in grouped:
    
    #print(i)
    #print("-"*100)
    #print(j)
    #print("="*100)

'''
VN
----------------------------------------------------------------------------------------------------
           Brand  Store Number  ... Longitude Latitude
25572  Starbucks  48482-263452  ...    105.83    21.01
25573  Starbucks  24015-232287  ...    105.86    21.03
25574  Starbucks  24016-230012  ...    105.78    21.04... 
'''

#聚合
#统计Brand个数
d1 = grouped["Brand"].count()
#print(d1)
'''
AD        1
AE      144
AR      108
AT       18
AU       22
 ...
TT        3
TW      394
US    13608
VN       25
ZA        3
'''


#比较美国和中国的数据
d2 = d1["US"]
d3 = d1["CN"]
print(d3)
print(d2)


#对中国每个省份的Brand的数量
china_data = data[data["Country"]=="CN"]

CN_grouped = china_data.groupby(by="State/Province").count()["Brand"]
print(CN_grouped)




















































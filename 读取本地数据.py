# -*- coding: utf-8 -*-
"""
读取数据
axis
二维:行-0
     列-1
三维:
    块-0
    行-1
    列-2
"""
import numpy as np
'''
np.loadtxt(fname,dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False)
fname:文件名
dtype:数据类型,默认科学计数法的float类型
delimiter:分隔字符串,默认空格,应改成逗号(csv文件)
skiprows:跳过前x行,一般跳过第一行表头
usecols:读取指定的列
unpack:默认False读取原矩阵，修改成True读取转置矩阵
'''
#转置矩阵方法一
t1 = np.arange(10).reshape(2,5)
t2 = np.transpose(t1)
print(t1)
'''
[[0 1 2 3 4]
 [5 6 7 8 9]]
'''
print(t2)
'''
[[0 5]
 [1 6]
 [2 7]
 [3 8]
 [4 9]]
'''
#转置矩阵方法二
t3 = t2.swapaxes(1,0)#行列交换
print(t3)
'''
[[0 1 2 3 4]
 [5 6 7 8 9]]
'''
#读取数据
filename_us='E:/youtube_video_data/US_video_data_numbers.csv'
filename_GB='E:/youtube_video_data/GB_video_data_numbers.csv'
data_us = np.loadtxt(filename_us,delimiter=',',dtype="int")
#print(data_us)
    
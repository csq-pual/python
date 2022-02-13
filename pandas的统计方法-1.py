# -*- coding: utf-8 -*-
"""
pandas的统计方法
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#读取数据
movie_data = pd.read_csv("E:\IMDB-Movie-Data.csv")


#观察数据信息
#print(movie_data.info())
#print(movie_data)
#print(movie_data.head())

'''
#取出导演列
director = movie_data["Director"]
print(director.head())
#求出导演的人数
director_num = len(director.tolist())
print(len(set(movie_data["Director"].tolist())))#利用set解决重复导演 644
#.unique()自动生成一个含有数据的列表
print(len(director.unique()))
print(director_num)#1000

#取出评分列
rating = movie_data["Rating"]
print(rating.head())
#获取平均评分
average = rating.mean()
print(average)


#取出演员人数
print(movie_data["Actors"].head())#查看前几行看如何分割
actor_num = movie_data["Actors"].str.split(", ").tolist()
#利用列表展开 两个循环将数组誊抄在另一个数组中
actor_num_list = [i for j in actor_num for i in j]
print(len(set(actor_num_list)))


#利用flatten变成一维数组 列表里面是列表不能使用latten 只用于展平数组里是字符串或者数字 
actor_num_list = list(np.array(actor_num).flatten())
print(type(actor_num_list))
print(len(set(actor_num_list)))
'''



#电影分类情况
pre_genre = movie_data["Genre"].str.split(",").tolist()
#print(pre_genre)#此时列表里面是列表[["",""],["",""]...]

#展开列表变成一行
genre_list = list(set([i for j in pre_genre for i in j]))
#print(genre_list)#此时列表里全是字符串["",""...]

#构造全为零的数组用于统计
zero_genre_list = pd.DataFrame(np.zeros((movie_data.shape[0],len(genre_list))),columns=genre_list)
#print(zero_genre_list)

#给每出现一次电影分类赋值
for i in range(movie_data.shape[0]):
    #使第i行所含有对应分类的列的0改为1
    zero_genre_list.loc[i,pre_genre[i]] = 1
#print(zero_genre_list.head(5))

#统计各个分类的总和
sum_count = zero_genre_list.sum(axis=0)
print(sum_count)
#排序
genre_count_sorted = sum_count.sort_values()


#画图
plt.figure(figsize=(20,8),dpi=80)
_x = genre_count_sorted.index
_y = genre_count_sorted.values
plt.bar(range(len(_x)),_y)
#设置x轴的str
plt.xticks(range(len(_x)),_x)
plt.show()




















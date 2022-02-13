# -*- coding: utf-8 -*-
"""
pandas的统计方法
"""
import pandas as pd
from matplotlib import pyplot as plt
#读取数据
movie_data = pd.read_csv("E:\IMDB-Movie-Data.csv")


#观察数据信息
#print(movie_data.info())
#print(movie_data)
#print(movie_data.head())


#取出导演列
director = movie_data["Director"]
print(director.head())
#求出导演的人数
director_num = len(director.tolist())
print(len(set(movie_data["Director"].tolist())))#利用set解决重复导演 644
#.unique()自动生成一个含不重复数据的列表
print(len(director.unique()))#644
print(director_num)#1000

#取出评分列
rating = movie_data["Rating"]
print(rating.head())
#获取平均评分
average = rating.mean()
print(average)


#取出演员列
actor = movie_data["Actors"].str.split(", ").tolist()





























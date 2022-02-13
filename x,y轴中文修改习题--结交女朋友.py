# -*- coding: utf-8 -*-
"""
me从11到30岁每年交的女朋友
a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
tz从11到30岁每年交的女朋友

"""
from matplotlib import pyplot as plt
#设置中文
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
#设置图片大小
fig = plt.figure(figsize=(20,10),dpi=100)
#设置x,y轴数据
x = range(11,31)
y_me = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_tz = [1,0,0,1,2,6,0,0,0,2,4,1,2,8,3,1,2,1,1,1]
#设置x轴中文描述
x_labels = ["{}岁".format(i) for i in range(11,31)]
plt.xticks(list(x),x_labels,rotation=60)
#设置图片网格
plt.grid(alpha=0.8)#设置透明度（越大越明显）
#设置x,y轴的标签
plt.xlabel("年龄")
plt.ylabel("女朋友个数")
#作图
plt.plot(x,y_me)
plt.plot(x,y_tz)
plt.show()
from collections import defaultdict
from random import uniform
from math import sqrt

def readdata():              #读取文档数据
    datas=[]
    with open('C:\Users\balabala\Desktop\blood.txt','r') as txt:
        for line in txt:
            date=list(map(float,line.split(' ')))
            datas.append(date)
        txt.close() 
    return datas

def putresults(assignments,k):    #输出结果
    print('\n\n分类结果:\n\n')
    resultlist=[[] for i in range(k)]
    num=0
    for i in assignments:
        resultlist[i].append(num)
        num=num+1
        
    for i in range(k):
        print("CLASS %d:"%(i+1))
        print(resultlist[i])
        print('\n')

def generatecenters(datas,k):  #得到初始化中心
    initailcenters=[]
    dimensions=len(datas[0])
    minmaxdata=defaultdict(int)
    
    for data in datas:
        for i in range(dimensions):
            value=data[i]
            min_key='min_%d'%i
            max_key='max_%d'%i
            if min_key not in minmaxdata or value<minmaxdata[min_key]:
                minmaxdata[min_key]=value
            if max_key not in minmaxdata or value>minmaxdata[max_key]:
                minmaxdata[max_key]=value
                
    for j in range(k):
        center=[]
        for i in range(dimensions):
            min_val=minmaxdata['min_%d'%i]
            max_val=minmaxdata['max_%d'%i]
            temp=float("%.8f"%(uniform(min_val,max_val)))
            center.append(temp)
        initailcenters.append(center)
        
    return initailcenters

def eucdist(a,b):             #欧几里得距离
    sums=0
    for i in range(len(a)):
        s=pow((a[i]-b[i]),2)
        sums+=s
    return sqrt(sums)

def updatecenters(datas,assignments,k):   #更新中心
    new_means = defaultdict(list)
    centers = []
    for assignment ,point in zip(assignments,datas):
        new_means[assignment].append(point)
    for i in range(k):
        points=new_means[i]
        ncenter=[]
        for i in range(len(points[0])):
            sum=0
            for p in points:
                sum+=p[i]
            ncenter.append(float("%.8f"%(sum/float(len(points)))))
        centers.append(ncenter)
    return centers

def sortdatas(datas,centers):     #根据中心给数据分类
    sortresults=[]
    for data in datas:
        shortest=float('inf')
        shortestp = 0
        for i in range(len(centers)):
            dist=eucdist(data,centers[i])
            if dist<shortest:
                shortest=dist
                shortestp=i
        sortresults.append(shortestp)
    return sortresults  

def kmeans(datas,k):
    initailcenters=generatecenters(datas,k)
    assignments=sortdatas(datas,initailcenters)
    oldassignments=None
    
    while assignments !=oldassignments:             
        newcenters=updatecenters(datas,assignments,k)
        oldassignments=assignments
        assignments=sortdatas(datas,newcenters)
    
    putresults(assignments,k)

def main():
    datas=readdata()
    kmeans(datas,3)

main()
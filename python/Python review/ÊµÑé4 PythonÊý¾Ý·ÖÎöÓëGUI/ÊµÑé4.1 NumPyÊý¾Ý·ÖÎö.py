#实验4.1 NumPy数据分析

import numpy
from numpy import *
import random

#（1）创建一维数组
print("一维数组：",end='')
list1=[]
for i in range(10):
    n=int(random.random()*90+10)#范围:n in [10,99]
    list1.insert(i,n)  
arr1=numpy.array(list1)#通过一维列表创建一维数组
print(arr1)#显示一维数组

#计算最大值，最小值和平均值
print("数据分析：",end='')
max1=arr1[0]; min1=arr1[0]; avg1=arr1[0]
for i in range(1,10):
    if max1<arr1[i]:max1=arr1[i]
    if min1>arr1[i]:min1=arr1[i]
    avg1+=arr1[i]
avg1=avg1/10
print("最大值=",max1,"最小值=",min1,"平均值=",avg1)

print("----------------------------------------")

#（2）创建二维数组
print("二维数组：",end='\n')
list2=[]
for i in range(5):
    temp=[]
    for j in range(5):
        n=int(random.random()*90+10)# 范围:n in [10,99]
        temp.insert(j,n)        
    list2.insert(i,temp)
arr2=numpy.array(list2)#通过二维列表创建二维数组
print(arr2)#显示二维数组

#计算最大值，最小值和平均值
print("数据分析：",end='')
max2=arr2[0][0]; min2=arr2[0][0]; avg2=0.0
for i in range(5):
    for j in range(5):
        if max2<arr2[i][j]:max2=arr2[i][j]
        if min2>arr2[i][j]:min2=arr2[i][j]
    avg2+=arr2[i][j]
avg2=avg2/25
print("最大值=",max2,"最小值=",min2,"平均值=",avg2)



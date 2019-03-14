#!/usr/bin/python
#coding=utf-8
x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
myList =[x,y,z]
for j in range(len(myList)+1):
    #两两之间进行比较大小，挑选出最大数
    for i in range(len(myList)-(j+1)):
        if myList[i] > myList[i+1]:
            tmp = myList[i+1]#定义一个变量来存储某一数据
            myList[i+1] = myList[i]
            myList[i] = tmp
print(myList)

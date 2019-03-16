#!/usr/bin/python
#coding=utf-8
a=int(raw_input('输入第一个数:'))
n=int(raw_input('输入第二个数:'))
b=0
c=a
for i in range(1,n+1):
    b=b+c
    c=c*10+a
    print(c)
print('和为: %d ' % b)

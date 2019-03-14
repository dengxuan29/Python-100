#/usr/bin/env python
#coding=utf-8
num = (1,2,3,4)
for i in num:
    for j in num:
        for k in num:
            if(i != j) and (i !=k) and (j != k): 
                print(i,j,k) 

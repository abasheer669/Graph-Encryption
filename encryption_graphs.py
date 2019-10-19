# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:13:43 2019

@author: basheer669
"""

print("Hello")
class node:
    def __init__(self):
        self.a=[]
        self.b=int(5)
c=node()
print(c.b)
a="A"
a1="WAEL"
a+=a1
b=[]
d=int(0)
for i in range(len(a)):
    e=[]
    for j in range(len(a)):
        e.append((d))
    if i==len(a)-1:
        e[1]=ord(a[1])-ord(a[i])    #sub first with last coz cycle
        b.append(e)
        break
    e[i+1]=ord(a[i+1])-ord(a[i])
#    print(e)
    b.append(e)
import numpy as np
f=np.array(b)
b1=int(27)
for i in range(1,len(f)-2):
    for j in range(i-1+3,len(f)):
        if i==1 and j==len(f)-1:
            continue
        f[i][j]=b1
        b1+=1
f=f+np.transpose(f)
print(f)

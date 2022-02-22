# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:21:11 2021

@author: USER
"""

import random

x=random.randint(1, 50)
print(x)
win=False

for i in range(5):
    y=int(input('請猜一個數字(1~50):'))    
    if y==x:
        print('猜對了!')
        win=True
        break
    
    if y>x:
        print('猜低一點~')
    else:
        print('猜高一點~')

if win:
    print('恭喜過關!')
else:
    print('正確答案為:%d'%x)



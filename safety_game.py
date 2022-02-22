# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:43:43 2021

@author: dave7
"""
from random import randint
answer=randint(0,100)

number=int(input('請猜數字0~100: '))
start=0
end=100

while number != answer:   
    
    if  number < answer :
        start=number
        print(start,'到',end) 
    elif number > answer:
        end=number
        print(start,'到',end)              
    number = int(input('請猜數字: '))
    if number <= start:
        print('請選擇範圍內數字')
        number = start    
    elif number >= end:
        print('請選擇範圍內數字')        
        number = end
print('BOOOM!!!')    

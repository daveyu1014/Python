# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:24:21 2022

@author: dave7
"""

import random

number=list(range(1,50))

bingo_number=random.sample(number,7)

print('依落球順序開獎號碼:')
print(bingo_number[0:6],end='')
print('特別號為:'+str(bingo_number[-1]))

sort_number=sorted(bingo_number[0:6])
print('依大小順序開獎號碼:')
print(sort_number,end='')
print('特別號為:'+str(bingo_number[-1]))



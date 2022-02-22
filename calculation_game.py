# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 23:04:48 2022

@author: dave7
"""
import random

print('Welcome to calculation game!....')
playing = input('Do you want to play? (y/n) ').lower()
score,count= 0, 0
while True:
    
    if playing == 'y':        
        a=random.randint(1, 20)
        b=random.randint(1, 20)
               
        cal=['+','-','*','//']
        op=random.choice(cal)
        
        if op == '+':
            answer = a + b
        elif op == '-':
            answer = a - b
        elif op == '*':
            answer = a * b
        elif op == '//':
            if a % b != 0:
                continue    
            else:
                answer = a / b
        
        print('0 to quit the game ',end="")
        question= eval(input(f'{a} {op} {b} = '))
        count+=1
        if question == answer:
            print('Correct Answer!')
            score+=1
        elif question == 0:
            print('')
            print('End of Game! ')
            print(f'總答 {count-1}題, 答對 {score}題, 正確率為{round((score/count)*100)}%')
            break
        else:
            print('Wrong Answer')
            print(f'The answer is: {answer}')
    elif playing =='n':
        break
    else:
        print('incorrect input!')
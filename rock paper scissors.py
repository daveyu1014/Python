# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 11:30:52 2022

@author: dave7
"""
import tkinter as tk
import random

def scissors_click():
    global draw_counts,computer_wins,user_wins,options
    computer_pick=random.choice(options)
    label2.config(text='Player: scissors',font=('Arial',18))
    label3.config(text=f'Computer: {computer_pick}',font=('Arial',18))
    
    if computer_pick == 'scissors':
        label1.config(text='Draw !',fg='indigo')
        draw_counts+=1
    elif computer_pick == 'rock':
        label1.config(text='You lose !',fg='maroon')
        computer_wins+=1
    elif computer_pick == 'paper':
        label1.config(text='You won !',fg='palegoldenrod')
        user_wins+=1   
    label4.config(text=f' You won: {user_wins} Computer won: {computer_wins} Draw: {draw_counts}')
    
def stone_click():
    global draw_counts,computer_wins,user_wins,options
    computer_pick=random.choice(options)
    label2.config(text='Player: stone',font=('Arial',18))
    label3.config(text=f'Computer: {computer_pick}',font=('Arial',18))
    if computer_pick == 'rock':
        label1.config(text='Draw !',fg='indigo')
        draw_counts+=1
    elif computer_pick == 'paper':
        label1.config(text='You lose !',fg='maroon')
        computer_wins+=1
    elif computer_pick == 'scissors':
        label1.config(text='You won !',fg='palegoldenrod')
        user_wins+=1        
    label4.config(text=f' You won: {user_wins} Computer won: {computer_wins} Draw: {draw_counts}')
    
def paper_click():
    global draw_counts,computer_wins,user_wins,options 
    computer_pick=random.choice(options)
    label2.config(text='Player: paper',font=('Arial',18))
    label3.config(text=f'Computer: {computer_pick}',font=('Arial',18))
    if computer_pick == 'paper':
        label1.config(text='Draw !',fg='indigo')
        draw_counts+=1
        draw_counts+=1
    elif computer_pick == 'scissors':
        label1.config(text='You lose !',fg='maroon')
        computer_wins+=1
    elif computer_pick == 'rock':
        label1.config(text='You won !',fg='palegoldenrod')
        user_wins+=1        
    label4.config(text=f' You won:{user_wins} Computer won:{computer_wins} Draw:{draw_counts}')

win=tk.Tk()
win.title('Rock Paper Scissors Game!')

f1=tk.Frame(win,bg='cadetblue',width=500,height=500)
f2=tk.Frame(win,bg='lightsteelblue')
f3=tk.Frame(win,bg='darkslategray',width=500,height=500)
f1.pack(side='top',fill = 'x')
f2.pack(fill='x')
f3.pack(side='bottom', fill ='x')

font=('Arial',18)
label1=tk.Label(f1,text='Please choose your pick',font=font,width=20,heigh=2,bg='cadetblue',fg='darkblue')
label2=tk.Label(f2,text='player',font=font,width=20,heigh=5,bg='lightsteelblue', fg='darkblue')
label3=tk.Label(f2,text='computer',font=font,width=20,heigh=5,bg='lightsteelblue', fg='darkblue')
label4=tk.Label(f3,text='Results : ',font=font,width=20,heigh=3,bg='darkslategray',fg='mistyrose')
label1.pack()
label2.pack(side='left')
label3.pack(side='right')
label4.pack(fill='x')

paper_btn=tk.PhotoImage(file="paper.gif")
scissors_btn=tk.PhotoImage(file="scissors.gif")
stone_btn=tk.PhotoImage(file="stone.gif")

paper_label=tk.Label(f2,image=paper_btn)
scissors_label=tk.Label(f2,image=scissors_btn)
stone_label=tk.Label(f2,image=stone_btn)


button1=tk.Button(f2, image=paper_btn,command=paper_click)
button1.pack(pady=20)
button2=tk.Button(f2, image=scissors_btn,command=scissors_click)
button2.pack(pady=20)
button3=tk.Button(f2, image=stone_btn,command=stone_click)
button3.pack(pady=20)

user_wins = 0
computer_wins = 0
draw_counts=0
options = ['rock','paper','scissors'] 

win.mainloop()

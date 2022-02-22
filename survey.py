# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:54:15 2022

@author: dave7
"""

import tkinter as tk
import datetime
import csv

comment=('非常不滿意','不滿意','普通','滿意','非常滿意')
time=datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
today =str(datetime.date.today())

win=tk.Tk()
win.geometry('600x950')
win.resizable(width=False, height=False)
win.title('用餐滿意度調查')
f1=tk.Frame(win,bg='mediumseagreen',width=600,height=150)
f2=tk.Frame(win,bg='mistyrose',width=600,height=400)
f3=tk.Frame(win,bg='mistyrose',width=600,height=100)
f4=tk.Frame(win,bg='mistyrose',width=600,height=300)

f1.pack(side='top',fill='x')
f2.pack(fill='both')
f3.pack(fill='both')
f4.pack(fill='both')

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()
var6 = tk.StringVar()
var7 = tk.StringVar()
var8 = tk.StringVar()
var9 = tk.StringVar()
var10 = tk.StringVar()
var11 = tk.StringVar()
var12 = tk.StringVar()
var13 = tk.StringVar()


def select():
    data=[]
    text = entry1.get()
    name = entry2.get()
    phone = entry3.get()
    mail = entry4.get()
    data.append(today)
    data.append(name)
    data.append(phone)
    data.append(mail)
    data.append(var1.get())
    data.append(var2.get())
    data.append(var3.get())
    data.append(var4.get())
    data.append(var5.get())
    data.append(var6.get())
    data.append(var7.get())
    data.append(var8.get())
    data.append(var9.get())
    data.append(var10.get())
    data.append(var11.get())
    data.append(var12.get())
    data.append(var13.get()) 
    data.append(text)
    print(data)
    
    with open(f"{today}-comment.csv",mode='a+',newline='',encoding='utf-8-sig') as csvfile:
        writer=csv.writer(csvfile)
        #head=['日期','姓名','電話','e-mail','整體','環境','服務','餐點','價位','沙拉','湯品','主餐','甜點','飲品','來店次數','得知本店','用餐目的','建議']
        #writer.writerow(head)
        writer.writerow(data)


#frame1
label0 = tk.Label(f1, text="David de Cafe", font=('Brush Script MT', 38),bg='mediumseagreen', fg="olive", anchor="center")
label0.pack(fill="x")


label1 = tk.Label(f1, text="為了提升餐廳的品質，此份調查目的，\n 僅供公司「內部使用」，敬請顧客放心。", font=('標楷體', 16), bg='mediumseagreen', fg="khaki", anchor="w")
label1.pack(fill='x', ipady=5)
label1_1 = tk.Label(f1, text=f'{time}', font=('標楷體', 14), bg='mediumseagreen', fg="darkslateblue", anchor="e")
label1_1.pack(fill='x', ipady=5)

#frame2
label2 = tk.Label(f2, text="您對於用餐的滿意度：", font=('標楷體', 18), fg="firebrick", anchor="center", bg='mistyrose')
label2.grid(row=0, ipady=5)


label3 = tk.Label(f2, text="整體", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label3.grid(row=2, column= 0)
com13 = tk.ttk.Combobox(f2, values=comment, textvariable=var1)
com13.grid(padx=90, pady=2,row=2,column=1,columnspan=4)

label4 = tk.Label(f2, text="環境", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label4.grid(row=3, column= 0)
com12 = tk.ttk.Combobox(f2, values=comment, textvariable=var2)

com12.grid(padx=90, pady=5,row=3,column=1,columnspan=4)

label5 = tk.Label(f2, text="服務", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label5.grid(row=4, column= 0)
com11 = tk.ttk.Combobox(f2, values=comment, textvariable=var3)
com11.grid(padx=90, pady=4,row=4,column=1,columnspan=4)

label6 = tk.Label(f2, text="餐點", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label6.grid(row=5, column= 0)
com10 = tk.ttk.Combobox(f2, values=comment, textvariable=var4)
com10.grid(padx=90, pady=5,row=5,column=1,columnspan=4)

label7 = tk.Label(f2, text="價位", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label7.grid(row=6, column= 0)
com9 = tk.ttk.Combobox(f2, values=comment, textvariable=var5)
com9.grid(padx=90, pady=5,row=6,column=1,columnspan=4)

#餐點
label8 = tk.Label(f2, text="您對於餐點的滿意度：", font=('標楷體', 18), fg="firebrick", anchor="center", bg='mistyrose')
label8.grid(row=7, ipady=5)

label9 = tk.Label(f2, text="沙拉", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label9.grid(row=9, column= 0)
com8 = tk.ttk.Combobox(f2, values=comment, textvariable=var6)
com8.grid(padx=90, pady=5,row=9,column=1,columnspan=4)

label10 = tk.Label(f2, text="湯品", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label10.grid(row=10, column= 0)
com7 = tk.ttk.Combobox(f2, values=comment, textvariable=var7)
com7.grid(padx=90, pady=5,row=10,column=1,columnspan=4)

label11 = tk.Label(f2, text="主餐", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label11.grid(row=11, column= 0)
com6 = tk.ttk.Combobox(f2, values=comment, textvariable=var8)
com6.grid(padx=90, pady=5,row=11,column=1,columnspan=4)

label12 = tk.Label(f2, text="甜點", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label12.grid(row=12, column= 0)
com5 = tk.ttk.Combobox(f2, values=comment, textvariable=var9)
com5.grid(padx=90, pady=5,row=12,column=1,columnspan=4)

label13 = tk.Label(f2, text="飲品", font=('標楷體', 16), fg="firebrick",bg='mistyrose')
label13.grid(row=13, column= 0)
com4 = tk.ttk.Combobox(f2, values=comment, textvariable=var10)
com4.grid(padx=90, pady=5,row=13,column=1,columnspan=4)


#frame3
label14= tk.Label(f3, text='這次您第幾次到本店用餐?', height=2, font=('標楷體', 14), bg='mistyrose', fg='firebrick')
label14.grid(row=0,column=0)
com1 = tk.ttk.Combobox(f3, textvariable=var11)
com1['values'] = ('第1次','2-3次','第4-6次','6-8次','8次以上')
com1.grid(padx=100, pady=5,row=0,column=3,columnspan=4)

label15= tk.Label(f3, text='您是從哪裡得知本店呢?', height=2, font=('標楷體', 14), bg='mistyrose', fg='firebrick')
label15.grid(row=1,column=0)
com2 = tk.ttk.Combobox(f3, textvariable=var12)
com2['values'] = ('親友介紹','網路社交媒體','新聞媒體','經過看到','其他管道')
com2.grid(padx=100, pady=5,row=1,column=3,columnspan=4)

label16= tk.Label(f3, text='您今天用餐的目的?', height=2, font=('標楷體', 14), bg='mistyrose', fg='firebrick')
label16.grid(row=2,column=0)
com3 = tk.ttk.Combobox(f3, textvariable=var13)
com3['values'] = ['單純用餐','生日聚餐','約會聚餐','家庭聚餐','公司聚餐','其他聚餐']
com3.grid(padx=100, pady=5,row=2,column=3,columnspan=4)



#frame4
label18 = tk.Label(f4, text="對於本店的建議:    ", font=('標楷體', 14), bg='mistyrose', fg='firebrick')
label18.grid(row=0)
entry1=tk.Entry(f4,text='\n \n' ,font=('標楷體',12),width=40)
entry1.grid(row=0,column=1,ipady=30)

label18 = tk.Label(f4, text="姓名:", font=('標楷體', 14), bg='mistyrose', fg='firebrick')
label18.grid(row=1,pady=2)
entry2=tk.Entry(f4,font=('標楷體',14),width=20)
entry2.grid(row=1,column=1)

label19 = tk.Label(f4, text="電話:", font=('標楷體', 14), bg='mistyrose', fg='firebrick')
label19.grid(row=2,pady=2)
entry3=tk.Entry(f4,font=('標楷體',14),width=20)
entry3.grid(row=2,column=1)

label20 = tk.Label(f4, text="E-mail:", font=('標楷體', 14), bg='mistyrose', fg='firebrick')
label20.grid(row=3,pady=2)
entry4=tk.Entry(f4,font=('標楷體',14),width=20)
entry4.grid(row=3,column=1)

label21 = tk.Label(f4, text="感謝您耐心地填寫，期待您的再次光臨!", font=('標楷體', 16), bg='mistyrose', fg='darkslateblue')
label21.grid(row=5,column=0, pady=10, columnspan=4)

b1=tk.Button(f4,text='送出',font=('標楷體',20), command = select)
b1.grid(row=6,column=2, pady=5, columnspan=4)


win.mainloop()
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter
from tkinter import *

cal = Tk()
cal.title("Calculator")
operator = ""
text_input = StringVar()

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
    
def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")
    
def btnEqualsInput():
    global operator
    ans = str(eval(operator))
    text_input.set(ans)

txtDisplay = Entry(cal, font=('arial',20, 'bold'), textvariable=text_input, bd=30, insertwidth =4, bg = "powder blue", 
                   justify = "right").grid(columnspan = 4)

btn0 = Button (cal, padx = 16, bd =8, fg= "black", font=('arial',20, 'bold'), text = "0", command = lambda:btnClick(0)).grid(row=4, column=1)
btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1)).grid(row= 3,column=0) 
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2)).grid(row= 3,column=1) 
btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3)).grid(row= 3,column=2) 
btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4)).grid(row= 2,column=0) 
btn5 = Button (cal, padx = 16, bd =8, fg= "black", font=('arial',20, 'bold'), text = "5", command = lambda:btnClick(5)).grid(row=2, column=1)
btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6)).grid(row= 2,column=2) 
btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:btnClick(7)).grid(row= 1,column=0) 
btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:btnClick(8)).grid(row= 1,column=1) 
btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9)).grid(row= 1,column=2) 

addition=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick("+")).grid (row=1,column=3)
subtraction=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick("- ")).grid(row=2,column=3) 
multiplication=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick("*") ).grid(row=3,column=3) 
Division=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/")).grid( row=4,column=3) 

Equal= Button (cal, padx = 16, bd =8, fg= "black", font=('arial',20, 'bold'), text = "=", command = btnEqualsInput).grid(row=4, column=2)

Division=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/")).grid( row=4,column=3) 

Clear = Button (cal, padx = 16, bd =8, fg= "black", font=('arial',20, 'bold'), text = "C", command = btnClearDisplay).grid(row=4, column=0)



cal.mainloop()
#Namaz Clock
import tkinter as tk
from tkinter import *
import time

background_color = input("Enter background color")
color = input("Enter text color")

root = tk.Tk()
root.geometry("400x400")
root.configure(background="lightgreen")
root.title("Namaz Clock")

def tick(time1 = ""):
    time2 = time.strftime('%I:%M:%S')
    clock_frame.config(text = time2)
    clock_frame.after(20, tick)

def Fajar_namaz():
    Fajar.config(text = "05:40 a.m Fajar")
    
def Zuhar_namaz():
    Zuhar.config(text = "01:30 p.m Zuhar")
    
def Asar_namaz():
    Asar.config(text = "04:20 p.m Asar")
    
def Maghrib_namaz():
    Maghrib.config(text = "06:55 p.m Maghrib")
    
def Isha_namaz():
    Isha.config(text = "08:15 p.m Isha")
    
def Jumma_namaz():
    Jumma.config(text = "02:00 p.m Jumma")

clock_frame= tk.Label(root, font=('arial',100, 'bold'), bg =background_color, fg = color)
clock_frame.pack(fill = "both", expand = 1)

Fajar= tk.Label(root, font=('arial',20, 'bold'), bg =background_color, anchor = 'n', fg = color)
Fajar.pack(fill = X)

Zuhar= tk.Label(root, font=('arial',20, 'bold'), bg =background_color, anchor = 'n', fg = color)
Zuhar.pack(fill = X)

Asar= tk.Label(root, font=('arial',20, 'bold'), bg =background_color, anchor = 'n', fg = color)
Asar.pack(fill = X)

Maghrib= tk.Label(root, font=('arial',20, 'bold'), bg =background_color, anchor = 'n', fg = color)
Maghrib.pack(fill = X)

Isha= tk.Label(root, font=('arial',20, 'bold'), bg =background_color, anchor = 'n', fg = color)
Isha.pack(fill = X)

Jumma= tk.Label(root, font=('arial',20, 'bold'), bg =background_color, anchor = 'n', fg = color)
Jumma.pack(fill = X)

tick()
Fajar_namaz()
Zuhar_namaz()
Asar_namaz()
Maghrib_namaz()
Isha_namaz()
Jumma_namaz()

root.mainloop()


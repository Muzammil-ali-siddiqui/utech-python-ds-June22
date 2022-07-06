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


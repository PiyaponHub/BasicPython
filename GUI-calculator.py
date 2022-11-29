#GUI-calculator

from tkinter import *
from tkinter import ttk, messagebox 

GUI = Tk()
GUI.title('Program calculates fish cost')
GUI.geometry('700x600')

bg = PhotoImage(file='ice-cream-car.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI, text='Please fill the number of fish(kg)', font=(None,20))
L.pack()

v_qty = StringVar() # Variable which keeps the message
E1 = ttk.Entry(GUI, textvariable=v_qty, font=(None,16))
E1.pack()

def calculate():
    try:
        quan = float(v_qty.get())
        calc = quan * 39 # 39 Baht/kg.
        messagebox.showinfo('Total price', 'Price of fish = {} Baht'.format(calc))
        E1.focus()
        v_qty.set("")  
    except:
        messagebox.showwarning('Invalid values', 'Please fill only number')
        v_qty.set('1')
B = ttk.Button(GUI, text='Calculate',command=calculate)
B.pack(ipadx=30, ipady=20)

GUI.mainloop()
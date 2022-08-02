'''
Final Project
Author: Sean Gifford
Date: 7/20/2022
'''

#Initization
from tkinter import *
import random

#Creating Window 1 (Home Window)
window_1 = Tk ()
window_1.geometry("600x1000")
window_1.title("Seans Pizzeria Online Portal - Home")

#Creating Background Images for Window 1 (Home Window) & Window 3 (Order Submitted Window)
bg = PhotoImage(file = "pizza.png")
bg_2 = PhotoImage(file = "pizza2.png")

window_1_background = Label(window_1, image = bg)
window_1_background.place(x = 0, y = 0)

#Declaring Entry Variables for Window 2
e1 = IntVar() #Delcaring Entry 1 as integer
e2 = IntVar() #Delcaring Entry 2 as integer
e3 = IntVar() #Delcaring Entry 3 as integer
e4 = IntVar() #Delcaring Entry 4 as integer
e5 = IntVar() #Delcaring Entry 5 as integer
e6 = IntVar() #Delcaring Entry 6 as integer
e7 = IntVar() #Delcaring Entry 7 as integer
e8 = IntVar() #Delcaring Entry 8 as integer
e9 = IntVar() #Delcaring Entry 9 as integer

#Creating Window 2 (Menu Window), with a Window Title & Sizing the Window
def open_window_2():
    window_2 = Tk ()
    window_2.title("Seans Pizzeria Online Portal - Menu")
    window_2.geometry("475x475")

#Getting Menu Input & Calculating Total for Window 2 (Menu Window)
    def calculate():
        total = 0
        cheese_pizza = e1.get()
        veggie_pizza = e2.get()
        pepperoni_pizza = e3.get()
        house_salad = e4.get()
        bread_sticks = e5.get()
        boneless_wings = e6.get()
        juice = e7.get()
        soda = e8.get()
        alcohol = e9.get()
        
        total=((int(cheese_pizza)*10) + (int(veggie_pizza)*11) + (int(pepperoni_pizza)*12) + (int(house_salad)*5) +
           (int(bread_sticks)*5) + (int(boneless_wings)*5) + (int(juice)*2) + (int(soda)*2) + (int(alcohol)*4))
        label_0 = Label(window_2, text = f"${total}", font="times 16 italic").place(x=350, y =400)

#Creating a Clear Menu for Window 2 (Menu Window) by deleting any current input, and replacing with 0, a starting value
    def clear_form ():
        total = 0
        e1.delete(0, END)
        e1.insert(0,0)
        e2.delete(0, END)
        e2.insert(0,0)
        e3.delete(0, END)
        e3.insert(0,0)
        e4.delete(0, END)
        e4.insert(0,0)
        e5.delete(0, END)
        e5.insert(0,0)
        e6.delete(0, END)
        e6.insert(0,0)
        e7.delete(0, END)
        e7.insert(0,0)
        e8.delete(0, END)
        e8.insert(0,0)
        e9.delete(0, END)
        e9.insert(0,0)
        label_0 = Label(window_2, text = "            ", font="times 18").place(x=330, y =390) #Overwriting total to replace total anytime clear command is called
    
#Creating Menu Labels for Window 2 (Menu Window), to hold menu data
    label_1 = Label(window_2, text ="Seans Pizzeria Menu", font="helvetica 22 bold")
    label_1.place(x=100, y =30)
    label_2 = Label(window_2, text ="Menu Item                            Price/Amt", font="times 16 italic")
    label_2.place(x=80, y =80)
    label_3 = Label(window_2, text ="Cheese Pizza.........................$10", font="helvetica 14")
    label_3.place(x=70, y =120)
    label_4 = Label(window_2, text ="Veggie Pizza..........................$11", font="helvetica 14")
    label_4.place(x=70, y =150)
    label_5 = Label(window_2, text ="Pepperoni Pizza....................$12", font="helvetica 14")
    label_5.place(x=70, y =180)
    label_6 = Label(window_2, text ="House Salad............................$5", font="helvetica 14")
    label_6.place(x=70, y =210)
    label_7 = Label(window_2, text ="Bread Sticks............................$5", font="helvetica 14")
    label_7.place(x=70, y =240)
    label_8 = Label(window_2, text ="Boneless Wings......................$5", font="helvetica 14")
    label_8.place(x=70, y =270)
    label_9 = Label(window_2, text ="Juice........................................$2", font="helvetica 14")
    label_9.place(x=70, y =300)
    label_10 = Label(window_2, text ="Soda........................................$2", font="helvetica 14")
    label_10.place(x=70, y =330)
    label_11 = Label(window_2, text ="Alcohol....................................$4", font="helvetica 14")
    label_11.place(x=70, y =360)
    label_12 = Label(window_2, text ="Total: ", font="times 16 italic")
    label_12.place(x=275, y =400)


#Creating Menu Entry Fields for Window 2 (Menu Window), to allow for menu input from user
    e1 = Entry(window_2, width=3)
    e1.place(x=363, y=126)
    e1.insert(0, "0")
    e2 = Entry(window_2, width=3)
    e2.place(x=363, y=156)
    e2.insert(0, "0")
    e3 = Entry(window_2, width=3)
    e3.place(x=363, y=186)
    e3.insert(0, "0")
    e4 = Entry(window_2, width=3)
    e4.place(x=363, y=216)
    e4.insert(0, "0")
    e5 = Entry(window_2, width=3)
    e5.place(x=363, y=246)
    e5.insert(0, "0")
    e6 = Entry(window_2, width=3)
    e6.place(x=363, y=276)
    e6.insert(0, "0")
    e7 = Entry(window_2, width=3)
    e7.place(x=363, y=306)
    e7.insert(0, "0")
    e8 = Entry(window_2, width=3)
    e8.place(x=363, y=336)
    e8.insert(0, "0")
    e9 = Entry(window_2, width=3)
    e9.place(x=363, y=366)
    e9.insert(0, "0")

#Creating Buttons for Window 2 (Total to calculate total, Clear to clear menu inputs, Submit to submit menu form)
    button_1 = Button(window_2, text='Total', width=10, command=calculate).place(x=200, y=450)
    button_2 = Button(window_2, text='Clear', width=10, command=clear_form).place(x=100, y=450)
    button_3 = Button(window_2, text='Submit', width=10, command=open_window_3).place(x=300, y=450)
    button_4 = Button(window_2, text='Exit', width=10, command=window_2.quit).place(x=400, y=450)
    
#Creating Window 3 (Order Submitted Window)
def open_window_3():
    import tkinter as tk
    window_3 = tk.Toplevel()
    window_3.title("Seans Pizzeria Online Ordering Form - Order Submitted")
    window_3.geometry("1200x950")
    window_3_background = Label(window_3, image = bg_2)
    window_3_background.place(x = 0, y = 0)

#Creating Labels for Window 3 (Order Submitted Window)
    label_13 = Label(window_3, text ="Your Order is", font="helvetica 50 bold")
    label_13.place(x = 700, y = 300)
    label_14 = Label(window_3, text ="in the Oven!", font="helvetica 50 bold")
    label_14.place(x = 725, y = 400)

#Creating Button for Window 1 (Home Window)
button_4 = Button(window_1,text="Place an Online Order", command = open_window_2).place (x=470, y=20)

mainloop()
exit(0)

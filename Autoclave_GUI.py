# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:37:21 2021

@author: ltuey
"""

import time
from tkinter import *
from tkinter import messagebox
import datetime



def P1_down():
    p_1 = int(Phase1.get()) 
    if p_1 > 4:
        p_1 -= 1
    Phase1.set(p_1)

def P1_up():
    p_1 = int(Phase1.get()) 
    if p_1 < 24:
        p_1 += 1
    Phase1.set(p_1)

def P2_down():
    p_2 = int(Phase2.get()) 
    if p_2 > 20:
        p_2 -= 1
    Phase2.set(p_2)

def P2_up():
    p_2 = int(Phase2.get()) 
    if p_2 < 40:
        p_2 += 1
    Phase2.set(p_2)
    
def P3_down():
    p_3 = int(Phase3.get()) 
    if p_3 > 4:
        p_3 -= 1
    Phase3.set(p_3)

def P3_up():
    p_3 = int(Phase3.get()) 
    if p_3 < 4:
        p_3 += 1
    Phase3.set(p_3)
    
def update_clock():
    global current_time 
    current_time = datetime.datetime.now()
    now = time.strftime("%a %b %d %Y %H:%M:%S")
    timenow.configure(text=now)
    p_1 = int(Phase1.get()) 
    p_2 = int(Phase2.get())
    p_3 = int(Phase3.get())
    root.after(200, update_clock)
    cycle_time = p_1 + p_2 + p_3
    cycle_delta = datetime.timedelta(hours = cycle_time)
    time_finish = current_time + cycle_delta
    print_time_finish = time_finish.strftime("%a %b %d %Y %H:%M")
    finishlabel.configure(text=print_time_finish)



# creating Tk window
root = Tk()



# setting geometry of tk window
# root.geometry("300x250")
root.configure(bg = '#333333')
#root.geometry("400x300")
root.attributes('-fullscreen', True)
#root.grid_rowconfigure(row=0, minsize=15)
# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Autoclave Dev")

# Declaration of variables
Phase1=StringVar()
Phase2=StringVar()
Phase3=StringVar()

# setting the default phase times
Phase1.set("8")
Phase2.set("24")
Phase3.set("4")

# Use of Entry class to take input from the user
Phase1Entry= Entry(root, width=3, font=("Arial",30,""),
                textvariable=Phase1, justify = 'center')
Phase1Entry.grid(column = 2, row = 1)

Phase2Entry= Entry(root, width=3, font=("Arial",30,""),
                textvariable=Phase2, justify = 'center')
Phase2Entry.grid(column = 2, row = 2)

Phase3Entry= Entry(root, width=3, font=("Arial",30,""),
                textvariable=Phase3, justify = 'center')
Phase3Entry.grid(column = 2, row = 3)

timenow=Label(font =("Arial Bold",35,""), bg = '#333333', fg = 'White')
timenow.grid(column = 0, row = 0, columnspan = 4, pady = 4)

phase1label=Label(text = "Pressure", font =("Arial Bold",35), bg = '#333333', fg = '#63d1db')
phase1label.grid(column = 0, row = 1, pady = 2 )

phase2label=Label(text = "Pressure + Heat", font =("Arial Bold",35), bg = '#333333', fg = '#63d1db')
phase2label.grid(column = 0, row = 2, pady = 2, ipadx =5)

phase3label=Label(text = "Pressure", font =("Arial Bold",35), bg = '#333333', fg = '#63d1db')
phase3label.grid(column = 0, row = 3, pady = 2)


finishtitle=Label(text = "Finish Time", font =("Arial Bold",32), bg = '#333333', fg = '#cf3021')
finishtitle.grid(column = 0, row = 5, columnspan = 4)
finishlabel=Label(font =("Arial Bold",32,""), bg = '#333333', fg = '#cf3021')
finishlabel.grid(column = 0, row = 6, columnspan = 4)

update_clock()



def exit_win():
    global Autoclave_Running_Window
    Autoclave_Running_Window.destroy()

def reset():
    # setting the default phase times
    Phase1.set("8")
    Phase2.set("24")
    Phase3.set("4")

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
            p_1 = int(Phase1.get()) 
            p_2 = int(Phase2.get())
            p_3 = int(Phase3.get())
            cycle_time = p_1 + p_2 + p_3
            cycle_delta = datetime.timedelta(hours = cycle_time)
            time_finish = current_time + cycle_delta
            print_time_finish = time_finish.strftime("%a %b %d %Y %H:%M")
            global finished 
            finished = -1
            
            global Autoclave_Running_Window
            Autoclave_Running_Window = Toplevel(root)
            Autoclave_Running_Window.title("Autoclave in Use")
            Label(Autoclave_Running_Window, text = "Autoclave Running").pack()
            exit_button = Button(Autoclave_Running_Window, text = 'Exit', command = exit_win)
            exit_button.pack()
            
            
    except:
        print("Please input the right value")
    while finished == 0:
        
        finished =1
        
P1_down_btn = Button(root, text = '<', bd = '3',font =("Arial Bold",18),
                       command= P1_down)
P1_down_btn.grid(column = 1, row = 1, pady = 2 , sticky = 'E')

P1_up_btn = Button(root, text = '>', bd = '3',font =("Arial Bold",18),
                       command= P1_up)
P1_up_btn.grid(column = 3, row = 1, sticky ='W' , pady = 2 )

P2_down_btn = Button(root, text = '<', bd = '3',font =("Arial Bold",18),
                       command= P2_down)
P2_down_btn.grid(column = 1, row = 2, pady = 2 , sticky = 'E' )

P2_up_btn = Button(root, text = '>', bd = '3',font =("Arial Bold",18),
                       command= P2_up)
P2_up_btn.grid(column = 3, row = 2, sticky ='W' , pady = 2  )

P3_down_btn = Button(root, text = '<', bd = '3',font =("Arial Bold",18),
                       state = "disabled", command= P3_down)
P3_down_btn.grid(column = 1, row = 3, pady = 2 , sticky = 'E' )

P3_up_btn = Button(root, text = '>', bd = '3',font =("Arial Bold",18),
                       state = "disabled", command= P3_up)
P3_up_btn.grid(column = 3, row = 3, sticky ='W' , pady = 2 )

start_btn = Button(root, text='Start', font =("Arial Bold",28), bd='5', bg = 'green', padx = 80, pady = 10,
            command= submit)
start_btn.grid(column = 0, row = 4, padx =1 , pady = 4 )

reset_btn = Button(root, text='Reset Times', font =("Arial Bold",28), bd='5', bg = 'black' , fg = 'white', pady = 10,
            command = reset)
reset_btn.grid(column = 1, row = 4, columnspan = 3, padx =1 , pady = 5 )


# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs

root.mainloop()

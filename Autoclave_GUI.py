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
    current_time = datetime.datetime.now()
    now = time.strftime("%a %b %d %Y %H:%M:%S")
    timenow.configure(text=now)
    root.after(200, update_clock)
    p_1 = int(Phase1.get()) 
    p_2 = int(Phase2.get())
    p_3 = int(Phase3.get())
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
root.geometry("400x300")
#root.attributes('-fullscreen', True)

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
Phase1Entry= Entry(root, width=3, font=("Arial",14,""),
				textvariable=Phase1, justify = 'center')
Phase1Entry.place(x=35,y=50)

Phase2Entry= Entry(root, width=3, font=("Arial",14,""),
				textvariable=Phase2, justify = 'center')
Phase2Entry.place(x=35,y=92)

Phase3Entry= Entry(root, width=3, font=("Arial",14,""),
				textvariable=Phase3, justify = 'center')
Phase3Entry.place(x=35,y=134)

timenow=Label(font =("Arial Bold",21,""), bg = '#333333', fg = '#63d1db')
timenow.place(x=10, y=5)

phase1label=Label(text = "Pressure", font =("Arial Bold",14), bg = '#333333', fg = '#63d1db')
phase1label.place(x=100, y=50)

phase2label=Label(text = "Pressure + Heat", font =("Arial Bold",14), bg = '#333333', fg = '#63d1db')
phase2label.place(x=100, y=92)

phase3label=Label(text = "Pressure", font =("Arial Bold",14), bg = '#333333', fg = '#63d1db')
phase3label.place(x=100, y=134)


finishtitle=Label(text = "Finish Time", font =("Arial Bold",21), bg = '#333333', fg = '#cf3021')
finishtitle.place(x=10, y=225)
finishlabel=Label(font =("Arial Bold",21,""), bg = '#333333', fg = '#cf3021')
finishlabel.place(x=10, y=255)
update_clock()

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
            finished = 0
            
	except:
		print("Please input the right value")
	while finished == 0:
		
		finished =1
        
P1_down_btn = Button(root, text = '<', bd = '3',
                       command= P1_down)
P1_down_btn.place(x = 10,y = 50)

P1_up_btn = Button(root, text = '>', bd = '3',
                       command= P1_up)
P1_up_btn.place(x = 77,y = 50)

P2_down_btn = Button(root, text = '<', bd = '3',
                       command= P2_down)
P2_down_btn.place(x = 10,y = 92)

P2_up_btn = Button(root, text = '>', bd = '3',
                       command= P2_up)
P2_up_btn.place(x = 77,y = 92)

P3_down_btn = Button(root, text = '<', bd = '3',
                       command= P3_down)
P3_down_btn.place(x = 10,y = 134)

P3_up_btn = Button(root, text = '>', bd = '3',
                       command= P3_up)
P3_up_btn.place(x = 77,y = 134)

# P2_down_btn = Button(root, text = '<', 
#                        command = hours_down)
# hoursdown_btn.place = (x = 25 , y = 30)

start_btn = Button(root, text='Start', bd='5',
			command= submit)
start_btn.place(x = 100,y = 180)

reset_btn = Button(root, text='Reset Times', bd='5',
			command = reset)
reset_btn.place(x = 160,y = 180)    


# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs

root.mainloop()

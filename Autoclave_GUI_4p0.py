# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:09:16 2022

@author: ltuey
"""
import time
from tkinter import *
from tkinter import messagebox
import datetime

# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

# GPIO.setup(10,GPIO.OUT, initial = 1)
# GPIO.setup(9,GPIO.OUT, initial = 1)

root = Tk()
root.geometry("500x500")
root.title("Autoclave GUI")
root.configure(bg = '#333333')
root.attributes('-fullscreen', True)

global start_btn

# Phase1=StringVar()
# Phase2=StringVar()
# Phase3=StringVar()

# #Phase 1 Nominal: 8 Hours / Min: 4 Hours / Max:24 Hours
# global Phase1
# Phase1 ="8"
# #Phase 2 Nominal: 24 Hours / Min: 24 Hours / Max: 40 Hours
# global Phase2
# Phase2="24"
# #Phase 3 Nominal 4 / Min 4 / Max 4
# global Phase3
# Phase3="4"

global p_1
global p_2
global p_3
p_1=8
p_2=24
p_3=4

# def runAutoclave():
#     try:

Autoclave=Label(root, text= "Autoclave #1",font =("Arial Bold",40,""), bg = '#333333', fg = '#a4e1e6')
Autoclave.grid(column = 0, row = 0, columnspan = 4)
# Autoclave.pack()
timenow=Label(root, font =("Arial Bold",35,""), bg = '#333333', fg = 'White')
timenow.grid(column = 0, row = 1, columnspan = 4)
# timenow.pack()

Phase1Entry=Label(text = str(p_1), font =("Arial Bold",30), bg = '#333333', fg = '#FFFFFF')
Phase1Entry.grid(column = 2, row = 2)

# Phase2Entry= Label(root, width=3, font=("Arial",30,""),textvariable=Phase2, justify = 'center')
Phase2Entry=Label(text = str(p_2), font =("Arial Bold",33), bg = '#333333', fg = '#FFFFFF')
Phase2Entry.grid(column = 2, row = 3)

# Phase3Entry= Label(root, width=3, font=("Arial",30,""), textvariable=Phase3, justify = 'center')
Phase3Entry=Label(text = str(p_3), font =("Arial Bold",33), bg = '#333333', fg = '#FFFFFF')
Phase3Entry.grid(column = 2, row = 4)

phase1label=Label(text = "Pressure", font =("Arial Bold",35), bg = '#333333', fg = '#63d1db')
phase1label.grid(column = 0, row = 2, pady = 2 )

phase2label=Label(text = "Pressure + Heat", font =("Arial Bold",35), bg = '#333333', fg = '#63d1db')
phase2label.grid(column = 0, row = 3, pady = 2)

phase3label=Label(text = "Pressure", font =("Arial Bold",35), bg = '#333333', fg = '#63d1db')
phase3label.grid(column = 0, row = 4, pady = 2)

# global finishtitle
# finishtitle=Label(text = "Finish Time", font =("Arial Bold",25), bg = '#333333', fg = '#cf3021')
# # finishtitle.pack()
# finishtitle.grid(column = 0, row = 7, columnspan = 1)
global finishlabel
finishlabel=Label(font =("Arial Bold",25,""), bg = '#333333', fg = '#cf3021')
# finishlabel.pack()
finishlabel.grid(column = 0, row = 7, columnspan = 4)

def P1_down():
    global p_1
    if p_1 > 4:
        p_1 -= 1

def P1_up():
    # p_1 = int(Phase1.get()) 
    global p_1
    if p_1 < 24:
        p_1 += 1

def P2_down():
    global p_2
    if p_2 > 20:
        p_2 -= 1

def P2_up():
    global p_2
    if p_2 < 40:
        p_2 += 1
    
def P3_down():
    global p_3
    if p_3 > 4:
        p_3 -= 1

def P3_up():
    global p_3
    if p_3 < 4:
        p_3 += 1
    
def Max_Times():
    global p_1, p_2
    p_1 = 24
    p_2 = 40

def Min_Times():
    global p_1, p_2
    p_1 = 4
    p_2 = 20
    
def update_clock():
    global current_time 
    current_time = datetime.datetime.now()
    now = time.strftime("%a %b %d %Y %H:%M:%S")
    timenow.configure(text=now)
    Phase1Entry.configure(text=str(p_1))
    Phase2Entry.configure(text=str(p_2))
    Phase3Entry.configure(text=str(p_3))
    root.after(200, update_clock)
    cycle_time = p_1 + p_2 + p_3
    cycle_delta = datetime.timedelta(seconds = cycle_time)
    time_finish = current_time + cycle_delta
    print_time_finish = time_finish.strftime("%a %b %d %Y %H:%M:%S")
    print_time_finish = "Finish: " + print_time_finish
    finishlabel.configure(text=print_time_finish)
    
def reset():
    # setting the default phase times
    # Phase1.set("8")
    # Phase2.set("24")
    # Phase3.set("4")
    global p_1, p_2
    p_1 = 8
    p_2 = 24

def verify_msg():
    res=messagebox.askquestion('Run Autoclave', 'Do you want to Run Autoclave with these settings?')
    if res == 'yes' :
        submit()
    else :
        mb.showinfo('Return', 'Returning to main application')
    
def submit():
    
    print('Autoclave Sequence started')
    
    current_time = datetime.datetime.now()
    now = current_time.strftime("%a %b %d %Y %H:%M:%S")
    timenow.configure(text=now)
    time_start = now
    
    p1_delta = datetime.timedelta(seconds = p_1)
    p1_finish = current_time + p1_delta
    print_text = p1_finish.strftime("%a %b %d %Y %H:%M:%S")
    p2_start = print_text
    print('P1 finish:' + print_text)
    p2_delta = datetime.timedelta(seconds = p_2)
    p2_finish = p1_finish + p2_delta
    print_text = p2_finish.strftime("%a %b %d %Y %H:%M:%S")
    p3_start = print_text
    print('P2 finish:' + print_text)
    p3_delta = datetime.timedelta(seconds = p_3)
    p3_finish = p2_finish + p3_delta
    print_text = p3_finish.strftime("%a %b %d %Y %H:%M:%S")  
    print('P3 finish:' + print_text)
    
    time_finish = p3_finish
    print_time_finish = time_finish.strftime("%a %b %d %Y %H:%M:%S")
    print_time_finish = 'Finish Time: ' + print_time_finish
    
    
    # start_btn["state"] = DISABLED
    # current_phase.configure(text="Phase 1 Pressure On in progress")
    # phasetimeleft.configure(text="time xxxxxxx")
    
    #Open New window for messages during Autoclave Cycle
    running_window = Toplevel()
    running_window.title('Autoclave Running')
    running_window.configure(bg = '#333333')
    AC_Run=Label(running_window, text= "Autoclave #1",font =("Arial Bold",40,""), bg = '#333333', fg = '#a4e1e6')
    AC_Run.pack()
    run_timenow=Label(running_window, font =("Arial Bold",35,""), bg = '#333333', fg = 'White')
    run_timenow.pack()
    current_phase=Label(running_window, font =("Arial Bold",35,""), bg = '#333333', fg = 'White')
    current_phase.pack()
    phasetimeleft=Label(running_window, font =("Arial Bold",35,""), bg = '#333333', fg = 'White')
    phasetimeleft.pack()
    AC_finishlabel=Label(running_window, font =("Arial Bold",32,""), bg = '#333333', fg = '#cf3021')
    AC_finishlabel.configure(text=print_time_finish)
    AC_finishlabel.pack()
    current_phase.configure(text="Phase 1 Pressure On in progress")
    close_btn = Button(running_window, font =("Arial Bold",28), bd='5', padx = 80, pady = 10,
                text = 'Back', command = running_window.destroy)
    close_btn.pack()
    close_btn["state"] = DISABLED
    
    finished = 1
    
    while (finished == 1):
        current_time = datetime.datetime.now()
        now = current_time.strftime("%a %b %d %Y %H:%M:%S")
        timenow.configure(text=now)
        run_timenow.configure(text=now)
        
        #Loop for Phase 1
        #Update Screen until after phase 1 finish time
        while (current_time < p1_finish):
            timenow.update()
            current_time = datetime.datetime.now()
            now = current_time.strftime("%a %b %d %Y %H:%M:%S")
            timenow.configure(text=now)
            run_timenow.configure(text=now)
            time_remaining = p1_finish - current_time
            p_mins, p_secs = divmod(time_remaining.seconds,60)
            p_hours, p_mins= divmod(p_mins,60)
            print_string = str(p_hours)+ ":" + str(p_mins) + ":" + str(p_secs)
            print_string = 'Phase time left: ' + print_string
            phasetimeleft.configure(text= print_string)
            time.sleep(0.5)
            
        #Setup and Loop phase 2
        current_phase.configure(text="Phase 2 Heat ON in progress")
        
        #Update Screen until after phase 2 finish time
        while (current_time < p2_finish):
            timenow.update()
            current_time = datetime.datetime.now()
            now = current_time.strftime("%a %b %d %Y %H:%M:%S")
            timenow.configure(text=now)
            run_timenow.configure(text=now)
            time_remaining = p2_finish - current_time
            p_mins, p_secs = divmod(time_remaining.seconds,60)
            p_hours, p_mins= divmod(p_mins,60)
            print_string = str(p_hours)+ ":" + str(p_mins) + ":" + str(p_secs)
            print_string = 'Phase time left: ' + print_string
            phasetimeleft.configure(text= print_string)
            time.sleep(0.5)
        
        #setup display and Loop Phase 3 
        current_phase.configure(text="Phase 3 Heat OFF in progress")
        
        while (current_time < p3_finish):
            timenow.update()
            current_time = datetime.datetime.now()
            now = current_time.strftime("%a %b %d %Y %H:%M:%S")
            timenow.configure(text=now)
            run_timenow.configure(text=now)
            time_remaining = p3_finish - current_time
            p_mins, p_secs = divmod(time_remaining.seconds,60)
            p_hours, p_mins= divmod(p_mins,60)
            print_string = str(p_hours)+ ":" + str(p_mins) + ":" + str(p_secs)
            print_string = 'Phase time left: ' + print_string
            phasetimeleft.configure(text= print_string)
            time.sleep(0.5)
        
        
        #Reset Display for cycle complete 
        if (current_time > p3_finish) :
            #Show Cycle info
            AC_Run.configure(text="Autoclave Complete")
            print_string = "Pressure ON: " + str(p_1) + " hours at " + str(time_start) 
            run_timenow.configure(text=print_string)
            print_string = "Heat ON:" + str(p_2) + " hours at " + str(p2_start) 
            current_phase.configure(text=print_string)
            print_string = "Heat OFF: " + str(p_3) + " hours at " + str(p3_start)
            phasetimeleft.configure(text=print_string)
            close_btn["state"] = ACTIVE
            
            #exit test cycle
            finished = 0

# def press_on(self):
#     GPIO.output(9,0)
# def press_off(self):
#     GPIO.output(9,1)
# def temp_on(self):
#     GPIO.output(10,0)
# def temp_off(self):
#     GPIO.output(10,1) 

P1_down_btn = Button(root, text = '<', bd = '3',font =("Arial Bold",18),
                       command= P1_down)
P1_down_btn.grid(column = 1, row = 2, pady = 2 , sticky = 'E')

P1_up_btn = Button(root, text = '>', bd = '3',font =("Arial Bold",18),
                       command= P1_up)
P1_up_btn.grid(column = 3, row = 2, sticky ='W' , pady = 2 )

P2_down_btn = Button(root, text = '<', bd = '3',font =("Arial Bold",18),
                       command= P2_down)
P2_down_btn.grid(column = 1, row = 3, pady = 2 , sticky = 'E' )

P2_up_btn = Button(root, text = '>', bd = '3',font =("Arial Bold",18),
                       command= P2_up)
P2_up_btn.grid(column = 3, row = 3, sticky ='W' , pady = 2  )

P3_down_btn = Button(root, text = '<', bd = '3',font =("Arial Bold",18),
                       state = "disabled", command= P3_down)
P3_down_btn.grid(column = 1, row = 4, pady = 2 , sticky = 'E' )

P3_up_btn = Button(root, text = '>', bd = '3',font =("Arial Bold",18),
                       state = "disabled", command= P3_up)
P3_up_btn.grid(column = 3, row = 4, sticky ='W' , pady = 2 )

start_btn = Button(root, text='Start', font =("Arial Bold",24), bd='5', bg = 'green',  height=2, width=10,
            pady=2, command= verify_msg)
start_btn.grid(column = 0, row = 6, columnspan=1)

reset_btn = Button(root, text='Reset', font =("Arial Bold",24), bd='5', bg = 'black' , fg = 'white', 
             height=2, width=10, pady=2, command = reset)
reset_btn.grid(column = 1, row = 6, columnspan = 3)

# min_btn = Button(root, text='Min', font =("Arial Bold",24), bd='5', bg = '#34cfbf', padx = 80, pady = 10,
#             command= Min_Times)
min_btn = Button(root, text='Min', font =("Arial Bold",24), bd='5', bg = '#34cfbf', height=2, width=10,
            command= Min_Times)
min_btn.grid(column = 0, row = 5, columnspan=1, pady=10)

max_btn = Button(root, text='Max', font =("Arial Bold",24), bd='5', bg = '#34cfbf' , fg = 'white', height = 2,
            width =10, command = Max_Times)
# max_btn = Button(root, text='Max', font =("Arial Bold",28), bd='5', bg = '#34cfbf' , fg = 'white', pady = 10,
#             command = Max_Times)
max_btn.grid(column = 1, row = 5, columnspan = 3, pady = 10)
    


# start_btn = Button(root, text='Start', font =("Arial Bold",28), bd='5', bg = 'green', padx = 80, pady = 10,
#             command= submit)
# start_btn.pack()

update_clock()

root.mainloop()

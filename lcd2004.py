#!/usr/bin/env python

import time
import liquidcrystal_i2c
import datetimefunctions
import datetime
import RPi.GPIO as GPIO
import keypad

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

dt = datetimefunctions.dt_fun()
lcd = liquidcrystal_i2c.LiquidCrystal_I2C(0x27, 1, numlines=4)
kp = keypad.keypad()

#Phase A: Pressure only 8Hours +16/-4
#Phase B: P&T 24 Hours +16/-4
#Phase C: Temp Off, Press on 4 Hours +/-0
phase_a_default = 5
# phase_a_min = 4
# phase_a_max = 24
phase_b_default = 10
# phase_b_min = 20
# phase_b_max = 40
phase_c_default = 5
# phase_c_min = 4
# phase_c_max = 4
phase_a = phase_a_default
phase_b = phase_b_default
phase_c = phase_c_default
current_phase = 1
current_disp = 1

kp.keypad_gpio_setup()

while 1:
# Control Variables for Block Diagram
#   ===================================
#   Home Screen 
    while current_phase == 1:
          
        current_time = datetime.datetime.now()
        cycle_time = phase_a + phase_b + phase_c
        key = kp.keypad_scan()
        dt.print_home_screen(current_time,cycle_time,current_disp)
        time.sleep(0.75)
        
        if current_disp < 12:
            current_disp += 1
        else:
            current_disp = 1
            
        if key == "A":
            current_phase = 2
#   Confirm Test Start Screen          
    while current_phase == 2:
        
        current_time = datetime.datetime.now()
        cycle_time = phase_a + phase_b + phase_c
        key = kp.keypad_scan()
        dt.confirm_screen(current_time,cycle_time)
        time.sleep(0.25)
        
            
        if key == "A":
            start_time = current_time             
            current_phase = 3
            time_delta = datetime.timedelta(seconds=phase_a)
            phase_a_finish = current_time + time_delta
            time_delta = datetime.timedelta(seconds=phase_b)
            phase_b_finish = phase_a_finish + time_delta
            time_delta = datetime.timedelta(seconds=phase_c)
            phase_c_finish = phase_b_finish + time_delta
            kp.press_on()
            
            
        elif key == "D":
            current_phase = 1
#   Phase A Pressure only in progress       
    while current_phase == 3:
        
        current_time = datetime.datetime.now()
        dt.phase_screen(current_time, "A", phase_c_finish, phase_a_finish)
        time.sleep(1)
        current_time = datetime.datetime.now()
        dt.phase_screen(current_time, "A", phase_c_finish, phase_a_finish)
        time.sleep(1)
        dt.autoclave_in_use()
        time.sleep(2)
        
        if current_time > phase_a_finish:
            current_phase = 4
            kp.temp_on()
            
    while current_phase == 4:
        
        current_time = datetime.datetime.now()
        dt.phase_screen(current_time, "B", phase_c_finish, phase_b_finish)
        time.sleep(1)
        current_time = datetime.datetime.now()
        dt.phase_screen(current_time, "B", phase_c_finish, phase_b_finish)
        time.sleep(1)
        dt.autoclave_in_use()
        time.sleep(2)
        
        if current_time > phase_b_finish:
            current_phase = 5
            kp.temp_off()
   
    while current_phase == 5:
        
        current_time = datetime.datetime.now()
        dt.phase_screen(current_time, "C", phase_c_finish, phase_c_finish)
        time.sleep(1)
        current_time = datetime.datetime.now()
        dt.phase_screen(current_time, "C", phase_c_finish, phase_c_finish)
        time.sleep(1)
        dt.autoclave_in_use()
        time.sleep(2)
        
        if current_time > phase_b_finish:
            current_phase = 6
            kp.press_off()
            disp_opt = 0
   
    while current_phase == 6:
        current_time = datetime.datetime.now()
        dt.final_screen(current_time, start_time, phase_a_finish, phase_b_finish, phase_c_finish, disp_opt)
        key = kp.keypad_scan()
        time.sleep(0.5)
        
        if disp_opt < 8:
            disp_opt += 1
        else:
            disp_opt = 1
            
        if key == "A":
            current_phase = 1

#  except KeyboardInterrupt:
#      GPIO.cleanup()
            

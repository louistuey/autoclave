import datetime

import liquidcrystal_i2c

lcd = liquidcrystal_i2c.LiquidCrystal_I2C(0x27, 1, numlines=4)

# x = datetime.datetime.now()
# print(x)

def print_time(time):
    pt =  time.strftime("%a")+" "
    pt += time.strftime("%b")+"-"+time.strftime("%d") 
    pt += "  " 
    pt += time.strftime("%H")+(":")+time.strftime("%M")
    pt += (":")+time.strftime("%S")
    return pt

def print_time_short(time):
    pt = time.strftime("%b")+"-"+time.strftime("%d") 
    pt += " " 
    pt += time.strftime("%H")+(":")+time.strftime("%M")
    return pt

def print_time_short_phase(time):
    pt = time.strftime("%d")+time.strftime("%b") 
    pt += " " 
    pt += time.strftime("%H")+(":")+time.strftime("%M")
    return pt

def print_time_weekday(time):
    pt = time.strftime("%a") 
    pt += "    " 
    pt += time.strftime("%H")+(":")+time.strftime("%M")
    return pt

def fin_time_calc(x,delta):
    total_time_delta = datetime.timedelta(hours=delta)
    finish_time = x + total_time_delta
    return finish_time

def home_top_lines(current_time,cycle_length):
    pstr = print_time(current_time)
    lcd.printline(0,pstr)
    finish_time = fin_time_calc(current_time,cycle_length)
    pstr = "Finish: " + print_time_short(finish_time)
    lcd.printline(1,pstr)

def home_bottom_line():
    lcd.printline(3," Press [A] to Start ")

class dt_fun:    
    def print_home_screen(self,current_time,cycle_length,screen_opt):
        if screen_opt == 1:
            home_top_lines(current_time,cycle_length)
            lcd.printline(2,"Phase A: Pressure   ")
            home_bottom_line()
        elif screen_opt == 3:
            home_top_lines(current_time,cycle_length)
            lcd.printline(2,"Phase A: 8 Hours    ")
            home_bottom_line()
        elif screen_opt == 5:
            home_top_lines(current_time,cycle_length)
            lcd.printline(2,"Phase B: Press+Temp ")
            home_bottom_line()
        elif screen_opt == 7:
            home_top_lines(current_time,cycle_length)
            lcd.printline(2,"Phase B: 24 Hours   ")
            home_bottom_line()
        elif screen_opt == 9:
            home_top_lines(current_time,cycle_length)
            lcd.printline(2,"Phase C: Pressure   ")
            home_bottom_line()
        elif screen_opt == 11:
            home_top_lines(current_time,cycle_length)
            lcd.printline(2,"Phase C: 4 Hours    ")
            home_bottom_line()
#         elif screen_opt == 2:
#             home_top_lines(current_time,cycle_length)
#             lcd.printline(2,"Phase A: Pressure   ")
#             home_bottom_line()
#         elif screen_opt == 4:
#             home_top_lines(current_time,cycle_length)
#             lcd.printline(2,"Phase A: 8 Hours    ")
#             home_bottom_line()
#         elif screen_opt == 6:
#             home_top_lines(current_time,cycle_length)
#             lcd.printline(2,"Phase B: Press+Temp ")
#             home_bottom_line()
#         elif screen_opt == 8:
#             home_top_lines(current_time,cycle_length)
#             lcd.printline(2,"Phase B: 24 Hours   ")
#             home_bottom_line()
#         elif screen_opt == 10:
#             home_top_lines(current_time,cycle_length)
#             lcd.printline(2,"Phase C: Pressure   ")
#             home_bottom_line()
#         elif screen_opt == 12:
#             home_top_lines(current_time,cycle_length)
#             lcd.printline(2,"Phase C: 4 Hours    ")
#             home_bottom_line()
    
    def confirm_screen(self,current_time,cycle_length):
        pstr = print_time(current_time)
        lcd.printline(0,pstr)
        finish_time = fin_time_calc(current_time,cycle_length)
        pstr = "Finish: " + print_time_short(finish_time)
        lcd.printline(1,pstr)
        pstr = "Cycle Total: " + str(cycle_length) +" hrs" 
        lcd.printline(2,pstr)
        pstr = "[A] Conf | [D] Exit "
        lcd.printline(3,pstr)
    
    def phase_screen(self, current_time, current_phase, cycle_end_time, phase_end_time):
        pstr = print_time(current_time)
        lcd.printline(0,pstr)
        pstr = "Phase " + current_phase + ": In Prog    "
        lcd.printline(1,pstr)
        pstr = "CycleFin:" + print_time_short_phase(cycle_end_time) 
        lcd.printline(2,pstr)
        pstr = "PhaseFin:" + print_time_short_phase(phase_end_time)
        lcd.printline(3,pstr)
        
    def autoclave_in_use(self):
        lcd.printline(0,"/*================*/")
        lcd.printline(1,"/*   Autoclave    */")
        lcd.printline(2,"/*    In  Use     */")
        lcd.printline(3,"/*================*/")
        
    def final_screen(self, current_time, start_time, phase_a_finish, phase_b_finish, phase_c_finish, disp_opt):
        lcd.printline(0,"*Autoclave Complete*")
        pstr = print_time_short(current_time)
        pstr = "Now: "+ pstr + "   "
        lcd.printline(1,pstr)
        
        if disp_opt == 1:
            pstr = "Start:  " + print_time_short_phase(start_time)
            lcd.printline(2,pstr)
        elif disp_opt == 3:
            pstr = "A Fin:  " + print_time_short_phase(phase_a_finish) + "  "
            lcd.printline(2,pstr)
        elif disp_opt == 5:
            pstr = "B Fin:  " + print_time_short_phase(phase_b_finish) + "  "
            lcd.printline(2,pstr)
        elif disp_opt == 7:
            pstr = "C Fin:  " + print_time_short_phase(phase_c_finish) + "  "
            lcd.printline(2,pstr)
            
        lcd.printline(3,"Press [A] to Exit   ")

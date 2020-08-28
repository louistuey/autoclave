import datetime

x = datetime.datetime.now()
print(x)

#Phase A: Pressure only 8Hours +16/-4
#Phase B: P&T 24 Hours +16/-4
#Phase C: Temp Off, Press on 4 Hours +/-0
phase_a_default = 8
phase_a_min = 4
phase_a_max = 24
phase_b_default = 26
phase_b_min = 20
phase_b_max = 40
phase_c_default = 4
phase_c_min = 4
phase_c_max = 4

y = x.hour + phase_a_default + phase_b_default + phase_c_default
print(y)

x = datetime.datetime.now()
total_time = phase_a_default + phase_b_default + phase_c_default
print(total_time)

total_time_delta = datetime.timedelta(hours=total_time)
finish_time = x + total_time_delta
print(finish_time)

def print_time(time):
    x = time.strftime("%b")+"-"+time.strftime("%d") 
    x += " " 
    x += time.strftime("%H")+(":")+time.strftime("%M") 
    return x
def fin_time_calc(x,delta):
    total_time_delta = datetime.timedelta(hours=delta)
    finish_time = x + total_time_delta
    return finish_time
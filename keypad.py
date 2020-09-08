import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

MATRIX = [["1","2","3","A"],
          ["4","5","6","B"],
          ["7","8","9","C"],
          ["*","0","#","D"]]

ROW = [12,16,20,21]
COL = [5,6,13,19]
class keypad:

    def keypad_gpio_setup(self):
        for i in range(4):
            GPIO.setup(ROW[i],GPIO.OUT, initial = 0)
            GPIO.setup(COL[i],GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(24,GPIO.OUT, initial = 0)
        GPIO.setup(25,GPIO.OUT, initial = 0)
    def keypad_scan(self):    
        for m in range (3):
            test = 0
            for j in range(len(ROW)):
                GPIO.output(ROW[j],1)
                
                for k in range(len(COL)):
                    test_output = GPIO.input(COL[k])
                    if test_output == 1:
                        time.sleep(0.2) #debounce
                        key = MATRIX[j][k]
                        test = 1
                GPIO.output(ROW[j],0)
                if test == 1:
                    break
            if test == 1:
                break
        time.sleep(0.1)
        
        if test == 1:
            return key
        else:
            return "_"
        
    def press_on(self):
        GPIO.output(25,1)
    def press_off(self):
        GPIO.output(25,0)
    def temp_on(self):
        GPIO.output(24,1)
    def temp_off(self):
        GPIO.output(24,0)    
                
# except KeyboardInterrupt:
#     GPIO.cleanup()
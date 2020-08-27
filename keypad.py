import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

MATRIX = [[1,2,3,"A"],
          [4,5,6,"B"],
          [7,8,9,"C"],
          ["*",0,"#","D"]]

ROW = [12,16,20,21]
COL = [5,6,13,19]

for i in range(4):
    GPIO.setup(ROW[i],GPIO.OUT, initial = 0)
    GPIO.setup(COL[i],GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
try:
    while(1):
        for j in range(len(ROW)):
            GPIO.output(ROW[j],1)
            
            for k in range(len(COL)):
                test_output = GPIO.input(COL[k])
                if test_output == 1:
                    print(MATRIX[j][k])
                    time.sleep(0.2)
                    
            GPIO.output(ROW[j],0)
            
except KeyboardInterrupt:
    GPIO.cleanup()
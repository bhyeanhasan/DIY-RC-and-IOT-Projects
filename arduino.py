from pyfirmata import Arduino, util,INPUT
import time

# port cinte command ls /dev/tty*
PORT = '/dev/ttyACM0'   

# Initialize Arduino board
board = Arduino(PORT)
time.sleep(0.5)

ANALOG_PIN = 0  
l0plus = 8  
l0minus = 9

# define pin mode
board.analog[ANALOG_PIN].mode = INPUT  
board.digital[l0plus].mode = INPUT  
board.digital[l0minus].mode = INPUT  

# Set up iterator to avoid buffer overflow
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()

while True:
    lp = board.digital[l0plus].read()
    lm = board.digital[l0minus].read()

    if lp==1 or lm ==1:
        print(" ? ")
    else:
        analog_value = board.analog[ANALOG_PIN].read()
        print(analog_value," ",lp," ",lm)
    time.sleep(1)

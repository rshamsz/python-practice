#! /usr/bin/env python3
from IPython.display import clear_output
import time

start_time = time.time()
active =True
while active :
    time.sleep(1)
    elapsedTime = time.time() - start_time
    if  elapsedTime > 5 :
        active =False
        print (f"\nExiting the loop!\n{elapsedTime:.4f} has passed since the start the script\n")
    else :
        print (f"\nThe current time is: {time.time()}\n{elapsedTime:.4f} has passed since the start!")
        
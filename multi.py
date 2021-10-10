from threading import Thread
from time import sleep
import sys

def timer():
    for i in range(45):
        sleep(1)   #waits 45 seconds
    sys.exit() #stops program after timer runs out, you could also have it print something or keep the user from attempting to answer any longer

def question():
    answer = input("foo?")

t1 = Thread(target=timer)
t2 = Thread(target=question)
t1.start() #Calls first function
t2.start() #Calls second function to run at same time
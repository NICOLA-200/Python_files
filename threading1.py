import threading
import time


def eat_breakFast():
     time.sleep(3)
     print("You eat breakfast!")
     

def drink_coffee():   
     time.sleep(4);
     print("you drink coffee")

def study():
     time.sleep(5)  
     print("You sleeps")


x = threading.Thread(target=eat_breakFast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()


x.join()
y.join()
z.join()
# eat_breakFast()
# drink_coffee()


print(threading.active_count())



print(threading.enumerate())

print(time.perf_counter())


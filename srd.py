import threading 
import time

def sana():
    for x in range(0,71):
        time.sleep(0.3)
        print(x)
sana()

def sanoq():
    for x in range(0,61):
        time.sleep(0.3)              
        print(x)
sanoq()

t1 = threading.Thread(target=sana)
t2 = threading.Thread(target=sanoq)

t1.start()
t2.start()
    
        

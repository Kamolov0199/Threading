
import time
a = int(input("1-ogli , 2-qizi: "))

def Jinsi():
    if a == 1:
        for x in range(0,31):
            time.sleep(0.2)              
            print("ogli")  
    elif a == 2:
         for x in range(0,31):
            time.sleep(0.2)              
            print("qizi")
    else:
        print("Bunaqa son yoq")

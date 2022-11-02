import threading
import time
from ism import *
from familiya import *
from ochistva import *
from Jinsi import *

t1 = threading.Thread(target=ism)
t2 = threading.Thread(target=familiya)
t3 = threading.Thread(target=ochistva)
t4 = threading.Thread(target=Jinsi)
t1.start()
t2.start()
t3.start()
t4.start()
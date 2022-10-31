import threading
import time
from ism import *
from familiya import *
from ochistva import *

t1 = threading.Thread(target=ism)
t2 = threading.Thread(target=familiya)
t3 = threading.Thread(target=ochistva)

t1.start()
t2.start()
t3.start()
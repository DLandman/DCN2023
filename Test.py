import time
import numpy as np

t1=time.time()
print(t1)
time.sleep(2)
t2=time.time()
print(t2)
print(np.round(t2-t1))
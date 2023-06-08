import Dataframe
import Sender
import Receiver
import numpy as np
from scipy.stats import bernoulli

# Input
# data = pd.read_fwf('message.txt', header=None)
data = np.loadtxt('message.txt', dtype=int) #[:,np.newaxis]
p1 = 0
p2 = 0
t_timeout = 5
dataEnd = len(data)-1
sender = Sender()
receiver = Receiver()
#loop


# sender.sendData()



# Main Loop
# n = 0
# while (n < dataEnd):
#     if (sender.data == None): #first message
#         sender.sendData(data[n])
#     else:
#         #sender sequence
#         if (sender.timer - time.time() > t_timeout): #check if timeout
#             pass
#         else:
#             #receiver part
#             if (ACKframe.n_r == sender.n_s):
#                 n+=1
#                 pass




P2 = bernoulli(p2)

for n in range(dataEnd):
    sender()

    while (sender.timer - time.time() <= t_timeout):
        if (ACKframe != (0, 0, 0)):
            if (ACKframe.n_r == sender.n_s):
                continue
            else:
                n -= 1
                continue








# Data Frame (1.1.125)

# Sender Function
def sender(ACKframe = (0, 0, 0), timer_status = 0, timer_value = 0, n_r = 0, data_next = 0, data_buffer = None):
    if (timer_status == 0):
        if (data_buffer == None):  # first message
            dataframe = Dataframe(bernoulli(1-p1), n_r, data_next)
        else:
            sender.sendData(data_next, n_r)
            # timer_status = 1


    return dataframe, timer_value, n_s

# Receiver Function
def receiver(dataframe, n_s_prev):
    if(dataframe.status == 0):
        return  #sleep()
    if (dataframe.n_s != n_r):
        #ExtractData()
                #DeliverData()
        n_r = n_r ^ 1  #n_r = n_r + 1 (mod 2 arithmetics)
    return ACkframe, n_r, data







import numpy as np

# Input
# data = pd.read_fwf('message.txt', header=None)
data = np.loadtxt('message.txt', dtype=int)
p1 = 0
p2 = 0
t_timeout = 5
data_end
sender = Sender()
#loop


sender.sendData()



# Main Loop
n = 0
while (n < dataEnd):
    if (sender.data == None): #first message
        sender.sendData( data[n])
    else:
        #sender sequence
        if (sender.timer - time.time() > t_timeout): #check if timeout
            pass
        else:
        #receiver part
        
        if (ACKframe.n_r == sender.n_s):
            n+=1




# Data Frame (1.1.125)

# # Sender Function
# def sender(ACKframe, timer_status, timer_value, n_r, data_next, data_buffer):
# 
# 
# 
# 
#     return dataframe, timer_value, n_r
# 
# # Receiver Function
# def receiver(dataframe, n_s_prev):
#     if(dataframe.status == 0):
#         return  #sleep()
#     if (dataframe.n_s != n_r):
#         #ExtractData()
#                 #DeliverData()
#         n_r = n_r ^ 1  #n_r = n_r + 1 (mod 2 arithmetics)
#     return ACkframe, n_r, data







class Sender:
    def __init__(self):
        self.n_s = 0  #Ns value
        self.data = None
        self.timer = time.time()

    def sendData(self, *args):
        data = args[0] 
        if length(args) > 1:
            ACKframe = args[1]
        #first message
        if (self.data == None):
            pass
        else:
            if(ACKframe.status == 0 ):
                return   Dataframe(0, 0, 0)
            if (self.n_s == ACKframe.n_r): #last data received succesfully
                self.n_s = self.n_s ^ 1

        self.timer = time.time()
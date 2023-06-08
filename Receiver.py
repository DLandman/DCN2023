class Receiver:
    def __init__(self):
        self.n_r = 0  #Nr value

    def sendData(self, Dataframe: Dataframe, data: int):
        if (self.n_s == ACKframe.n_r): #last data received succesfully
            self.n_s = self.n_s ^ 1


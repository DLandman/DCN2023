class Dataframe:
    def __init__(self, *args):  #(status, n_s, data) or (status, n_r)
        if len(args) > 2:
            self.status = args[0]  #0 = corrupt, 1 = error free
            self.n_s = args[1]  #Ns value
            self.n_r = None
            self.data = args[2]  #payload being transmitted
        else:
            self.status = args[0]  #0 = corrupt, 1 = error free
            self.n_s = None  #Nr value
            self.n_r = args[1]
            self.data = None  #payload being transmitted

    def corrupt(self):
        self.status = 0

databit = Dataframe(1,1,27)
print(databit.status)
databit.corrupt()
print(databit.status)

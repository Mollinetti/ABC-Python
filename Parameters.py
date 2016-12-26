

class Params:
    
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().splitlines()
        line = data[0]
        self.dim = line.split()
        self.dim = list(map(int, self.dim))
        self.size = 0
        for i in (range(0,len(self.dim)-1)):
            self.size+= self.dim[i] * self.dim[i+1]
        self.SN = int(data[1])
        self.empnum = self.SN
        self.onlnum = int(self.SN/2)
        self.scoutnum = int(data[2])
        self.limit   = int(data[3]) 
        line = data[4]
        self.lowBound = line.split()
        self.lowBound = list(map(float, self.lowBound))
        line = data[5]
        self.uppBound = line.split()
        self.uppBound = list(map(float, self.uppBound))
        self.MCN  = int(data[6])
        self.isbias = str(data[7])
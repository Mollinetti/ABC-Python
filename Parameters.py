'''
Created on 01/07/2015

@author: Mollinetti
'''

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
        self.MCN  = int(data[len(data)-1])
        line = data[len(data)-4]
        self.lowBound = line.split()
        self.lowBound = list(map(float, self.lowBound))
        line = data[len(data)-3]
        self.uppBound = line.split()
        self.uppBound = list(map(float, self.uppBound))
        self.funcName = data[len(data)-2]


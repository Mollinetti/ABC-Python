'''
Created on 01/07/2015

@author: Mollinetti
'''

class Params:
    
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().splitlines()
        self.dim = int(data[0])
        self.SN = int(data[1])
        self.empnum =SN
        self.onlnum = int(SN/2)
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


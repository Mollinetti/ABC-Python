import pandas,numpy

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
        self.limit   = int(self.SN*sum(self.dim)) 
        line = data[4]
        self.lowBound = line.split()
        self.lowBound = list(map(float, self.lowBound))
        line = data[5]
        self.uppBound = line.split()
        self.uppBound = list(map(float, self.uppBound))
        self.MCN  = int(data[6])
        self.isbias = str(data[7])
        self.filename = str(data[8])
        self.testfilename = str(data[9])
        data = pandas.read_csv(self.filename, header=None)
        dataset = data.values

        testset= pandas.read_csv(self.testfilename, header= None)
        tests= testset.values

        ## Splita variaveis de entrada ##
        self.X= dataset[:,0:8]
        self.X = numpy.array(self.X).astype(float)  
            ## Splita variaveis de Saida ##
        self.Y= dataset[:,8]
        self.Y= numpy.array([self.Y,]).T
        ## Test Set ##
        self.Z= tests[:,0:8]
        self.Z= numpy.array(self.Z).astype(float)
        self.Z2= tests[:,8]
        self.Z2= numpy.array([self.Z2,]).T
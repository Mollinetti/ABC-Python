import pandas,numpy,itertools

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
        self.limit   = int(numpy.around(self.SN*sum(self.dim)/4)) 
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

        if(filename == "pima"):
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
        #elif(filename == "horse"):

        elif(filename == "soybean"):
            self.X= dataset[:,1:36]
            self.Y1= dataset[:,0]
            self.Y= []
            #criando as labels
            n = 19
            n1 = 9
            d= []
            c = 0
            for x in itertools.combinations( range(n), n1 ) :
                if(c >= n):
                    break
                d.append([ 1 if i in x else 0 for i in range(n) ])
                c+= 1

            print("d:",d)
            for i in self.Y1:
                if (i == "diaporthe-stem-canker"):
                    self.Y.append(d[0])
                elif (i == "charcoal-rot"):
                    self.Y.append(d[1])
                elif (i == "rhizoctonia-root-rot"):
                    self.Y.append(d[2])
                elif (i == "phytophthora-rot"):
                    self.Y.append(d[3])
                elif (i == "brown-stem-rot"):
                    self.Y.append(d[4])
                elif (i == "powdery-mildew"):
                    self.Y.append(d[5])
                elif (i == "downy-mildew"):
                    self.Y.append(d[6])
                elif (i == "brown-spot"):
                    self.Y.append(d[7])
                elif (i == "bacterial-blight"):
                    self.Y.append(d[8])
                elif (i == "bacterial-pustule"):
                    self.Y.append(d[9])
                elif (i == "purple-seed-stain"):
                    self.Y.append(d[10])
                elif (i == "anthracnose"):
                    self.Y.append(d[11])
                elif (i == "phyllosticta-leaf-spot"):
                    self.Y.append(d[12])
                elif (i == "alternarialeaf-spot"):
                    self.Y.append(d[13])
                elif (i == "frog-eye-leaf-spot"):   
                    self.Y.append(d[14])
                elif (i == "diaporthe-pod-&-stem-blight"):
                    self.Y.append(d[15])
                elif (i == "cyst-nematode"):
                    self.Y.append(d[16])
                elif (i == "2-4-d-injury"):
                    self.Y.append(d[17])
                elif (i == "herbicide-injury"):
                    self.Y.append(d[18])

            self.Y= numpy.array(self.Y)
            self.Z= tests[:,1:36]
            self.Z= numpy.array(self.Z).astype(float)
            self.ZP= tests[:,0]
            self.Z2= []
            for i in self.ZP:
                if (i == "diaporthe-stem-canker"):
                    self.Z2.append(d[0])
                elif (i == "charcoal-rot"):
                    self.Z2.append(d[1])
                elif (i == "rhizoctonia-root-rot"):
                    self.Z2.append(d[2])
                elif (i == "phytophthora-rot"):
                    self.Z2.append(d[3])
                elif (i == "brown-stem-rot"):
                    self.Z2.append(d[4])
                elif (i == "powdery-mildew"):
                    self.Z2.append(d[5])
                elif (i == "downy-mildew"):
                    self.Z2.append(d[6])
                elif (i == "brown-spot"):
                    self.Z2.append(d[7])
                elif (i == "bacterial-blight"):
                    self.Z2.append(d[8])
                elif (i == "bacterial-pustule"):
                    self.Z2.append(d[9])
                elif (i == "purple-seed-stain"):
                    self.Z2.append(d[10])
                elif (i == "anthracnose"):
                    self.Z2.append(d[11])
                elif (i == "phyllosticta-leaf-spot"):
                    self.Z2.append(d[12])
                elif (i == "alternarialeaf-spot"):
                    self.Z2.append(d[13])
                elif (i == "frog-eye-leaf-spot"):   
                    self.Z2.append(d[14])
                elif (i == "diaporthe-pod-&-stem-blight"):
                    self.Z2.append(d[15])
                elif (i == "cyst-nematode"):
                    self.Z2.append(d[16])
                elif (i == "2-4-d-injury"):
                    self.Z2.append(d[17])
                elif (i == "herbicide-injury"):
                    self.Z2.append(d[18])

            self.Z2= numpy.array(self.Z2)
            #print("Z2=",self.Z2)
            

        elif(filename == "spam"):

            ## Splita variaveis de entrada ##
            self.X= dataset[:,0:57]
            self.X = numpy.array(self.X).astype(float)  
                ## Splita variaveis de Saida ##
            self.Y= dataset[:,57]
            self.Y= numpy.array([self.Y,]).T
            ## Test Set ##
            self.Z= tests[:,0:57]
            self.Z= numpy.array(self.Z).astype(float)
            self.Z2= tests[:,57]
            self.Z2= numpy.array([self.Z2,]).T
            print("ok")

        elif(filename == "horse"):
            data= pandas.read_csv("Datasets/horse.csv", header= None, delim_whitespace= True)

            dataset = data.values

            self.X= dataset[:,0:27]
            self.Y= dataset[:,27]

            aux = aux2 = 0

            for i in self.X:
                aux2 = 0    
                for j in i:
                    if (j == "?"):
                        self.X[aux][aux2] = 0
                    aux2 += 1

                aux += 1

            self.X = self.X.astype(float) # Não precisa converter p numpy matriz #


        elif(filename == "thyroid"):
            self.X= dataset[:,0:29]
            
                ## Splita variaveis de Saida ##
            self.Y= dataset[:,29]
         
            ## Test Set ##
            self.Z= tests[:,0:29]

            self.Z2= tests[:,29]
            
            #criando as labels
            n = 3
            n1 = 2
            d= []
            c = 0
            for x in itertools.combinations( range(n), n1 ) :
                if(c >= n):
                    break
                d.append([ 1 if i in x else 0 for i in range(n) ])
                c+= 1

            count= 0
            print("d:",d)
            for i in self.Y:
                aux, aux2 = i.split(".")
                
                if(aux == "negative"):
                    self.Y[count]= d[0]
                elif(aux == "increased binding protein"):
                    self.Y[count]= d[1]
                else:
                    self.Y[count]= d[2]
                count+= 1

            aux= 0

            for i in self.X:
                aux2 = 0    
                for j in i:
                    if (j == "F"):
                        self.X[aux][aux2]= 0
                    elif (j == "M"):
                        self.X[aux][aux2]= 1
                    elif (j == "f"):
                        self.X[aux][aux2]= 0
                    elif (j == "t"):
                        self.X[aux][aux2]= 1
                    elif (j == "?"):
                        self.X[aux][aux2]= 0
                    elif (j == "SVI"):
                        self.X[aux][aux2]= 0
                    elif (j == "SVHC"):
                        self.X[aux][aux2]= 1
                    elif (j == "STMW"):
                        self.X[aux][aux2]= 2
                    elif (j == "SVHD"):
                        self.X[aux][aux2]= 3
                    elif (j == "other"):
                       self.X[aux][aux2]= 4

                    aux2 += 1

                aux += 1

            self.Y= numpy.array([self.Y,])
            self.X = numpy.array(self.X)
            self.Z= numpy.array(self.Z)
            self.Z2= numpy.array([self.Z2,])
'''
Created on 01/07/2015

@author: Mollinetti
'''

import Parameters, math, copy, random, Bee
from operator import attrgetter

class Cycles ():
    
    
    
    def __init__(self,  param = Parameters):
        self.parameters = param
        
        
    #employed cycle
    def employedCycle(self, sol = Bee):
    	#iterate over all individuals
    	for i in range(0,self.parameters.empnum):
    		temp = copy.deepcopy(sol[i])
    		j = random.randint(0,self.parameters.size-1) 
    		while True:
    			k = random.randint(0, self.parameters.empnum-1)
    			if k not i:
    				break
    		temp.weights[j] = sol[i].weights[j] + random.uniform(-1, 1) * (sol[i].weights[j] - sol[k].weights[j])

    		#tratar o valor de peso se extrapolar o bound (se for permitido eh claro)

    		#temp.objvalue = evaluate(sol[i].weights)
    		if(temp.objvalue < sol[i].objvalue):
    			sol[i].weights[j] = temp.weights[j] 
    			sol[i].objvalue = temp.objvalue
    			sol[i].limit = 0
    		else:
    			sol[i].limit += 1

    #onlooker cycle
    def onlookerCycle(self, sol = Bee):
    	#get a sample of the indexes of all solutions
    	samples = random.sample(range(0,(self.parameters.SN)- 1),self.parameters.onlnum)
    	#iterate over only a predetermined set
    	for i in range(0,len(samples)):
    		temp = copy.deepcopy(sol[samples[i]])
    		j = random.randint(0,self.parameters.size-1) 
    		while True:
    			k = random.randint(0, self.parameters.empnum-1)
    			if k not samples[i]:
    				break
    		temp.weights[j] = sol[samples[i]].weights[j] + random.uniform(-1, 1) * (sol[samples[i]].weights[j] - sol[samples[k]].weights[j])

    		#tratar o valor de peso se extrapolar o bound (se for necessario eh claro)

    		#temp.objvalue = evaluate(sol[i].weights)
    		if(temp.objvalue < sol[samples[i]].objvalue):
    			sol[samples[i]].weights[j] = temp.weights[j] 
    			sol[samples[i]].objvalue = temp.objvalue
    			sol[samples[i]].limit = 0
    		else:
    			sol[samples[i]].limit += 1

    #scout cycle
    def scoutCycle(self, sol = Bee):
    	#lista de index de  abelhas que ultrapassaram o limit
    	limit_bee = []
    	#checar se ha alguma abelha que ultrapassou o limite
    	for i in range(0, len(self.parameters.SN)):
    		if sol[i].limit >= self.parameters.limit
    		limit_bee.append(i)
    	#escolher as fontes para cada scout que houver por uma sample
    	chosen = random.sample(limit_bee, self.parameters.scoutnum)
    	#gerar novos valores pra nova fonte
    	for i in range (0, len(chosen)):
    		temp = copy.deepcopy(sol[chosen[i]])
    		j = random.randint(0,self.parameters.size-1) 
    		sol[chosen[i]].weights[j] = random.uniform(-1, 1) 
    		#temp.objvalue = evaluate(sol[i].weights)
    		if(temp.objvalue < sol[samples[i]].objvalue):
    			sol[chosen[i]].weights[j] = temp.weights[j] 
    			sol[chosen[i]].objvalue = temp.objvalue
    			sol[chosen[i]].limit = 0
    		else:
    			sol[chosen[i]].limit += 1


    
    #function to find the best element of the population
    def findBest(self):
        if self.param.isMin == True:

            if self.param.hasConst == True:
                best = min(self.population, key=attrgetter('violations','fitness'))
                return best
            else:
                best = min(self.population, key=attrgetter('fitness'))
                return best
        else:
            if self.param.hasConst == True:
                best = max(self.population, key=attrgetter('violations','fitness'))
                return best
            else:
                best = max(self.population, key=attrgetter('fitness'))
                return best

    #funtion that writes the results of the algorithm
    def writeResult(self, filename):
        f = open(filename,'w')
        f.write(str("Fitness").rjust(5))

        if self.param.hasConst == True:
            f.write(str("Violations").rjust(5))

        for i in range(0,int(self.param.dim)):
            f.write("Variable" + str(i) +"\t")

        if self.param.hasConst == True:
            for i in range(0,int(self.param.restrictions)):
                f.write("Restriction"+ str(i) + "\t")

        f.write("\n")

        if self.param.hasConst == True:
            for i in range(0, int(len(self.bests))):
                f.write(str(self.bests[i].fitness)[:12])
                f.write(str(self.bests[i].violations).rjust(3)+ "  ")
                for j in range(0, int(self.param.dim)):
                    f.write(str(self.bests[i].genotype[j])[:12] + "  ")
                f.write(str(self.bests[i].violations)+ "\t")
                for j in range(0, int(self.param.restrictions)):
                    f.write(str(self.bests[i].restrictions[j]) + "\t") 
                f.write("\n")

        else:        
            for i in range(0, int(len(self.bests))):
                f.write(str(self.bests[i].fitness)+ "\t")
                for j in range(0, int(self.param.dim)):
                    f.write(str(self.bests[i].genotype[j])+ "\t")
                f.write("\n")    

        #end it by closing the file\
        f.close()



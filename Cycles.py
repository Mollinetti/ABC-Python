'''
Created on 01/07/2015

@author: Mollinetti
'''

import Parameters, math, copy, random, Bee, Eval, numpy
from operator import attrgetter

class Cycles ():
    
    
    
    def __init__(self,  param = Parameters):
        self.parameters = param

        
        
    #employed cycle
    def employedCycle(self, sol = Bee):
        #iterate over all individuals
        for i in range(0,self.parameters.empnum):
        #print ("i:", i)
            temp = copy.deepcopy(sol[i])
            j = random.randint(0,self.parameters.size-1) 
            while True:
            	k = random.randint(0, self.parameters.empnum-1)
            	if k != i:
            		break
            #print ("j:", j)
            #print ("k:", k)
            temp.weights[j] = sol[i].weights[j] + random.uniform(-1, 1) * (sol[i].weights[j] - sol[k].weights[j])
            #tratar o valor de peso se extrapolar o bound (se for permitido eh claro)
            temp.objvalue, temp.output = self.evaluate(temp)
            if(temp.objvalue < sol[i].objvalue):
                sol[i].output = temp.output
                sol[i].weights[j] = temp.weights[j] 
                sol[i].objvalue = temp.objvalue
                sol[i].limit = 0
            else:
            	sol[i].limit += 1

    #onlooker cycle
    def onlookerCycle(self, method = "std",sol = Bee):
        #numero de participante do torneio: sempre setado em 2, mas caso queira aumentar, eh possivel
        tn_size = 2
    	#dependendo da escolha, samples pode ser uma pool de torneio ou um valor de uma sample de populacao
        samples = []
        if (method == "std"):
            samples = random.sample(range(0,(self.parameters.SN)- 1),self.parameters.onlnum)
    	#print("samples:", samples)
        #selecao de torneio
        elif (method == "tournament"):
            for x in range(0,self.parameters.onlnum):        
                #escolher dois numeros aleatorios e realizar torneio
                tn_pool = random.sample(range(0,(self.parameters.SN)- 1),tn_size)
                #tirar o minimo
                if (sol[tn_pool[0]].objvalue <= sol[tn_pool[1]].objvalue):
                    samples.append(tn_pool[0])
                else:
                    samples.append(tn_pool[1])

    	#iterate over only a predetermined set
        for i in range(0,len(samples)):
         temp = copy.deepcopy(sol[samples[i]])
         j = random.randint(0,self.parameters.size-1) 
         while True:
            k = random.randint(0, self.parameters.onlnum-1)
            if k != samples[i]:
                break
         temp.weights[j] = sol[samples[i]].weights[j] + random.uniform(-1, 1) * (sol[samples[i]].weights[j] - sol[samples[k]].weights[j])

        #tratar o valor de peso se extrapolar o bound (se for necessario eh claro)

         temp.objvalue, temp.output = self.evaluate(temp)
         if(temp.objvalue < sol[samples[i]].objvalue):
             sol[samples[i]].weights[j] = temp.weights[j] 
             sol[samples[i]].objvalue = temp.objvalue
             sol[samples[i]].limit = 0
             sol[samples[i]].output = temp.output
         else:
             sol[samples[i]].limit += 1

    #scout cycle
    def scoutCycle(self, sol = Bee):
        #lista de index de  abelhas que ultrapassaram o limit
        limit_bee = [] 
        #checar se ha alguma abelha que ultrapassou o limite
        for i in range(0, int(self.parameters.SN)):
            if (sol[i].limit >= self.parameters.limit):
                limit_bee.append(i)
        #escolher as fontes para cada scout que houver por uma sample
        if (limit_bee):
            #chosen = random.sample(limit_bee, self.parameters.scoutnum)
            #escolher todos os individuos da pool
            chosen = random.sample(limit_bee, len(limit_bee))
        #print("chosen:", chosen, sol[chosen[0]].weights)
        #gerar novos valores pra nova fonte
            for i in range (0, len(chosen)):
                temp = copy.deepcopy(sol[chosen[i]])
                j = random.randint(0,self.parameters.size-1) 
                temp.weights[j] = random.uniform(-1, 1) 
                temp.objvalue, temp.output = self.evaluate(temp)
                if(temp.objvalue < sol[chosen[i]].objvalue):
                    sol[chosen[i]].weights[j] = temp.weights[j] 
                    sol[chosen[i]].objvalue = temp.objvalue
                    sol[chosen[i]].limit = 0
                    sol[chosen[i]].output = temp.output
        #print("chosen after:", chosen, sol[chosen[0]].weights)
                else:
                    sol[chosen[i]].limit += 1

    def evaluate(self,  sol = Bee):
    	#generic function for fitness assessment
        #bounding all parameters
       # for i in range(0, self.parameters.size):
            #if g.genotype[i] < self.param.lowBound[i]:
               # g.genotype[i] = self.param.lowBound[i]

            #elif g.genotype[i] > self.param.uppBound[i]:
                #g.genotype[i] = self.param.uppBound[i]
        result,output = getattr(Eval, "error2")(self.parameters.X, self.parameters.Y,sol.weights,sol.bias,self.parameters.dim)
        return result,output


    #function to find the best element of the population
    def findBest(self, sol = Bee):
        best = min(sol, key=attrgetter('objvalue'))
        return best


    #funtion that writes the results of the algorithm
    def writeResult(self, filename, bests = Bee):
        f = open(filename,'w')
        f.write(str("ObjValue").rjust(5))
        f.write("Accuracy" + "\t")

        f.write("\n")  
        for i in range(0, int(len(bests))):
            total_acertos = 0
            total_predicts= 0
            count = 0
            f.write("%12.10f"%(bests[i].objvalue)+ "\t")
            for j in self.parameters.Z:
                output = Eval.think(j,bests[i].weights,self.parameters.dim,bests[i].bias)
                total_predicts+=1
                if (numpy.around(self.parameters.Z2[count]) == numpy.around(output[-1])):
                    total_acertos += 1
                count+=1

            accuracy = (total_acertos/total_predicts)*100
            f.write("Accuracy: %.2f" % (accuracy))
            f.write("\n")    

        #end it by closing the file\
        f.close()




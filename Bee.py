'''
Created on 01/07/2015

@author: Mollinetti
'''
import Parameters, random
import numpy as np

class Bee:
    
    total = 0

    #os pesos serao inicializados seguindo a distribuicao normal [-1,1], mas vale a pena ler sobre o 
    #algoritmo de Nguyen-Widrow pra inicializar os valores
    #provavelmente no experimento do artigo tenha detalhe para isso

    #as listas sao inicializadas usando distribuicao normal entre [-1, 1)
    #cada solucao candidata consiste em uma lista de listas de pesos

    def __init__(self, param=Parameters):
        self.weights = [] 
        for i in (range(0,len(param.dim)-1)):
           self.weights.extend(list(2*np.random.random([param.dim[i] * param.dim[i+1]]) - 1))
        self.objvalue = float("inf")
        self.limit = int(0)
        #if there is  number of bias, initialize it
        self.bias = []
        if(param.isbias == "yes"):
            for _ in range(0,len(param.dim)-1):
                self.bias.append(random.uniform(-1,1))
        self.output = []

        Bee.total +=1
    
    @classmethod
    def howmany(cls):
        print ("currently {:d} bees".format(cls.total))
        

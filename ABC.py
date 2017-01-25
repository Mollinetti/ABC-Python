import Cycles, sys, Parameters, Eval, Bee, random,copy

class ABC(object):
	"""docstring for ABC"""
	def __init__(self, p = Parameters):
		super(ABC, self).__init__()
		self.p = p
		self.bees = []
		#buffer com o melhor de cada geracao
		self.bests = []
		
	def run(self, outname, p = Parameters):
		c = Cycles.Cycles(p)
		#print(p.dim, p.SN, p.MCN, p.limit, p.MCN, p.MCN, p.scoutnum, p.onlnum, p.lowBound, p.uppBound, p.funcName, p.size)
		#inicializar as abelhas
		for i in range(0, p.SN):
			self.bees.append(Bee.Bee(p))
			
		#loop de iteracao
		for i in range(0, p.MCN):
			c.employedCycle(self.bees)
			c.onlookerCycle("std",self.bees)
			c.scoutCycle(self.bees)
			self.bests.append(copy.copy(c.findBest(self.bees)))
			#print("step:"+ str(i))
		#write result File
		c.writeResult("out/"+ outname, self.bests)




    
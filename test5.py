import Parameters, Bee, Cycles, Eval,pandas,numpy,random


print("teste5")
p = Parameters.Params("pima")
#c = Cycles.Cycles(p)
b = Bee.Bee(p)

#for i in range(0,p.SN):
#print(b.weights)

#c.employedCycle(b)
filename = p.filename
data = pandas.read_csv(filename, header=None)
dataset = data.values

testset= pandas.read_csv(p.testfilename, header= None)
tests= testset.values


## Splita variaveis de entrada ##
X= dataset[:,0:8]
X = numpy.array(X).astype(float)  
	## Splita variaveis de Saida ##
Y= dataset[:,8]
Y= numpy.array([Y,]).T
## Test Set ##
Z= tests[:,0:8]
Z= numpy.array(Z).astype(float)
Z2= tests[:,8]
Z2= numpy.array([Z2,]).T

#print(Z[1:4])

#print(Z2)

print (Eval.error2(X,Y, b.weights, b.bias, p.dim))
print(random.sample(range(10),10))
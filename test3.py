import Parameters, Bee, Cycles


print("teste3")
p = Parameters.Params("par")
c = Cycles.Cycles(p)
b = []
#print(p.dim, p.SN, p.MCN, p.limit, p.MCN, p.MCN, p.scoutnum, p.onlnum, p.lowBound, p.uppBound, p.funcName, p.size)
for i in range(0,p.SN):
	b.append(Bee.Bee(p))
	#b[i].limit = 30

#for i in range(0,p.SN):
print(b[0].weights)

c.employedCycle(b)
#c.onlookerCycle(b)
#c.scoutCycle(b)

print(b[0].weights)

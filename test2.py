import Parameters, Bee


print("teste2")
p = Parameters.Params("par")
#print(p.dim, p.SN, p.MCN, p.limit, p.MCN, p.MCN, p.scoutnum, p.onlnum, p.lowBound, p.uppBound, p.funcName, p.size)
b = Bee.Bee(p)
print(b.bias)
print(b.weights)
#criar bottom-top
#exemplo de rede 3-2-1
l3 = Bee.Layer(1)
l2 = Bee.Layer(2,None,l3)
l = Bee.Layer(3,None,l2)
l2.prev = l

print("l3:", l3.weights, l3.bias)
print("l2:", l2.weights, l2.bias)
print("l1:", l.weights, l.bias)

import Parameters, Bee, Cycles, Eval


print("teste4")
p = Parameters.Params("par")
#c = Cycles.Cycles(p)
b = Bee.Bee(p)

#for i in range(0,p.SN):
#print(b.weights)

#c.employedCycle(b)

print (Eval.error([[1,1,1],[1,0,1]], [[1],[0]], b.weights, b.bias, p.dim))

#def error(self, training_inputs, training_outputs, weights, bias, param = Parameters):

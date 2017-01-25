import Parameters, Bee, Cycles,numpy, itertools

#dot(training_inputs, weights[0:(param.dim[0] * param.dim[1])-1]) + bias[0])

a = [1.5, 2.5]
b = [2, 2]

#c = 0.1

#d = numpy.multiply(a,b)

n = 19
n1 = 9
d= []
c = 0
for x in itertools.combinations( range(n), n1 ) :
    if(c >= n):
    	break
    d.append([ 1 if i in x else 0 for i in range(n) ])
    c+= 1

print(d[0])
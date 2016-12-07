import math

def evaluate(function, arg):
    result = function(arg)
    return result

#placeholder
def foo(x):
	sum = 0
	for i in range(0, len(x)):
		sum+= x[i]
	return sum
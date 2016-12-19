import math, numpy


def evaluate(function, arg):
    result = function(arg)
    return result

#placeholder
def foo(x):
	sum = 0
	for i in range(0, len(x)):
		sum+= x[i]
	return sum


# Função de Ativação e Derivada Sigmoid #
def __sigmoid(x):
    return 1 / (1 + numpy.exp(-x))

def __sigmoid_prime(x):
    return __sigmoid(x) * (1 - __sigmoid(x))

#calcula o erro da rede neural toda
def error(training_inputs, training_outputs, weights, bias, dim):
	#lista de lista de outputs
	output = []
	#itera para a primeira hidden layer dim  = 1
	temp = []
	for i in range(0,dim[1]):
		temp.append(__sigmoid(sum(numpy.add(numpy.multiply(weights[i*dim[0]:((i+1)*dim[0])],training_inputs),bias[0]))))
	output.append(temp[:])
	#itera para as outras layers
	for j in range(2,len(dim)):
		temp = []
		for i in range(0,dim[j]):
			ind = numpy.prod(dim[0:j])
			print(ind)
			temp.append(__sigmoid(sum(numpy.add(numpy.multiply(weights[ind+(i*dim[j-1]):ind+((i+1)*dim[j-1])],output[j-2]),bias[j-1]))))
		output.append(temp[:])

	#calcula a funcao erro 1/2n sum(euclid(expected - actual)^2)
	#armazenar a soma do erro
	summation = 0

	for x in output[-1]:
		summation+= math.pow(numpy.linalg.norm(training_outputs[x] - output[-1][x]),2)


	print(output)

	return (1/2len(training_outputs)) * summation





	#output[0] = __sigmoid(numpy.dot(training_inputs, weights[0:(param.dim[0] * param.dim[1])-1]) + bias[0])
	#calcula o resto
	#for i in range(1,len(param.dim)-1):
		#ind = param.dim[i-1] * param.dim[i]
		#output[i] = __sigmoid(numpy.dot(output[i-1], weights[ind : ind + (param.dim[i] * param.dim[i+1])-1]) + bias[i])

	#calcula o erro total
	#total_error = (1/param.dim[-1]) *math.pow(sum(training_set_outputs) - sum(output[-1]),2)  
	#return total_error


	
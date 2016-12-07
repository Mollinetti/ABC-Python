import Cycles, sys, Parameters, Eval, Bee, random, ABC

if __name__ == '__main__':
	try:
		argfile = str(sys.argv[1])
		#init parameters by reading the txt
		p = Parameters.Params(argfile)
		#init mersenne twister seed
		random.seed(None,2)
		print("Initializing ABC")
		for i in range(0,int(sys.argv[2])):
			abc = ABC.ABC(p)
			abc.run(str(i),p)
		print("Finalized with success")
	except IndexError:
		print("\nRight usage: python3 ABC.py [Name of the function] [number of executions]\n")
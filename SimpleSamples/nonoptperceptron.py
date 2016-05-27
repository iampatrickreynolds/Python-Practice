import numpy as np
import sys

N = int(raw_input('How many data points? '))

X = [[1, np.random.uniform(-1, 1), np.random.uniform(-1, 1)] for i in range(N)]

coords = [np.random.uniform(-1, 1) for i in range(4)]

m = (coords[3] - coords[2]) / (coords[1] - coords[0])
def f(x):
	return m * (x - coords[0]) + coords[2]
	
Combined = [[x, np.sign(f(x[1]) - x[2])] for x in X]

# Y = [y for [x, y] in Combined]

def Perceptron():
	w = [0, 0, 0]
	
	for j in range(1000):
		errors = []
		r = range(len(X))
		# np.random.shuffle(r)
		# error = None
	
		for i in r:
			if np.sign(np.dot(Combined[i][0], w)) != Combined[i][1]:
				# error = Combined[i]
				# break
				errors.append(Combined[i])
				
		# if error == None:
		if len(errors) == 0:
			print 'Perceptron converged.'
			return w
			sys.exit()
		
		updateerror = errors[np.random.randint(len(errors))]
		for i in range(3):
			w[i] = w[i] + updateerror[1] * updateerror[0][i]
			
			
	print 'Perceptron did not converge.'	
	return w
	
# iterations = int(raw_input('How many iterations? '))

final = Perceptron()		

print final	
			
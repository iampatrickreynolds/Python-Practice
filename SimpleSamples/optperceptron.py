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

answer = raw_input('Should the data be linearly separable? ')
if 'n' in answer or 'N' in answer:
	for i in range(N // 10):
		Combined[i][1] = -1 * Combined[i][1]

def Perceptron():
	w = [0, 0, 0]
	wbest = w
	
	for j in range(1000):
	
		r = range(len(X))
		np.random.shuffle(r)
		error = None
	
		for i in r:
			if np.sign(np.dot(Combined[i][0], w)) != Combined[i][1]:
				error = Combined[i]
				break
	
		if error == None:
			print 'Perceptron converged after %d iterations.' % j
			return w
			sys.exit()
		
		for i in range(3):
			w[i] = w[i] + error[1] * error[0][i]
	
	print 'Perceptron did not converge after 10000 iterations.'	
	return w
	
# iterations = int(raw_input('How many iterations? '))

final = Perceptron()		

print final	
			
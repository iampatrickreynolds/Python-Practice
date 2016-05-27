from PIL import Image

class CN(object):
    """
    This is a complex number with real part
    self.re and imaginary part self.im. 
    Addition, multiplication, modulus, and
    reasonable looking repr are implemented
    below.
    """
	def __init__(self, re, im):
		self.re = re
		self.im = im
		
	def add(self, cn):
		return CN(self.re + cn.re, self.im + cn.im)
	
	def mul(self, cn):
		return CN(self.re * cn.re - self.im * cn.im, self.re * cn.im + self.im * cn.re)
		
	def mod(self):
		return self.re ** 2 + self.im ** 2
		
	def __repr__(self):
		return str(self.re) + " + " + str(self.im) + "i"
		
def P(a):
    """
    This is the function that gets iterated on 0
    to decide if a is in the Mandelbrot set.
    Check the wiki page for more details.
    """
	def p(z):
		return z.mul(z).add(a)
	return p
	
def checkDiverge(a, iters):
	"""
    Iterates P(a) above on 0 for at most iters times.  
    If modulus exceeds 4, divergence is guaranteed.
    """
    current = CN(0, 0)
	for n in range(iters):
		current = P(a)(current)
		if current.mod() > 4:
			return True
	return False
	
def timeToDiverge(a, maxiters):
	"""
    Better version of checkDiverge that records the 
    time at which modulus exceeds 4.  Used to make a 
    better-looking picture of the set.
    """
    current = CN(0, 0)
	for n in range(maxiters):
		current = P(a)(current)
		if current.mod() > 4:
			return n
	return -1
	
def mandelbrot(res, maxiter):
	"""
    Generates a matrix of times to divergence for 
    a window that contains the Mandelbrot set.
    """
    image = []
	for i in range(res):
		temp = []
		for j in range(res):
			a = CN(-2.2 + (3.0 / res) * j, -1.25 + (2.5 / res) * i)
			if checkDiverge(a, maxiter):
				temp.append(1)
			else:
				temp.append(0)
		image.append(temp)
	return image
	
def mandSet(res, maxiters):
	"""
    Better version of mandelbrot that uses timeToDiverge
    """
    image = []
	for i in range(res):
		temp = []
		for j in range(res):
			a = CN(-2.2 + (3.0 / res) * j, -1.25 + (2.5 / res) * i)
			temp.append(timeToDiverge(a, maxiters))
		image.append(temp)
	return image
	
def convertToDots(image):
	"""
    Super simple conversion for displaying image in 
    terminal.  Res should be 200 or less.
    """
    for row in image:
		string = ''
		for item in row:
			if item == 0:
				string = string + '.'
			else:
				string = string + ' '
		print string
		
def fancyConvert(image):
	"""
    Quite respectable conversion for displaying image
    in terminal.  Better than original rendering of
    the Mandelbrot set.  Keep res small.
    """
    for row in image:
		string = ''
		for item in row:
			if item == -1:
				string = string + '0'
			elif item < 7:
				string = string + ' '
			elif item < 13:
				string = string + '.'
			else:
				string = string + '*'
		print string
		
def convertToHex(num):
	"""
    Name says it all.  I thought I might need this for 
    writing BMPs by hand.
    """
    if num == 0:
		return '00'
	digits = "0123456789ABCDEF"
	out = ''
	while num > 0:
		out = digits[(num % 16)] + out
		num /= 16	
	if len(out) < 2:
		out = '0' + out
	return out		
		
if __name__ == "__main__":
	N = 1000
    image = mandSet(N, N)       # build the image matrix
	#fancyConvert(image)
	
	
	img = Image.new('RGB', (N, N), 'black')     # create blank image
	pixels = img.load()
	
    # use image matrix to build an image that displays reasonably
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			a = image[i][j]
			if a == -1:
				pixels[j, i] = (0, 0, 0)
			else:
				v = max([255 - 2 * a, 0])
				pixels[j, i] = (v, v, v)
			
	img.save('out.bmp')
	img.show()
	

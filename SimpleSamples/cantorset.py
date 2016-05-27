import turtle

def drawSegment(points, color, myTurtle):
	myTurtle.color(color)
	myTurtle.up()
	myTurtle.goto(points[0][0], points[0][1])
	myTurtle.down()
	myTurtle.goto(points[1][0], points[1][1])	
	
def getMiddleThird(p1, p2):
	newp1 = [ 2.0 / 3 * p1[0] + 1.0 / 3 * p2[0], 2.0 / 3 * p1[1] + 1.0 / 3 * p2[1]]
	newp2 = [ 1.0 / 3 * p1[0] + 2.0 / 3 * p2[0], 1.0 / 3 * p1[1] + 2.0 / 3 * p2[1]]
	return [newp1, newp2]
	
def getMiddleFifth(p1, p2):
	newp1 = [ 3.0 / 5 * p1[0] + 2.0 / 5 * p2[0], 3.0 / 5 * p1[1] + 2.0 / 5 * p2[1]]
	newp2 = [ 2.0 / 5 * p1[0] + 3.0 / 5 * p2[0], 2.0 / 5 * p1[1] + 3.0 / 5 * p2[1]]
	return [newp1, newp2]	
	
def getMiddleNinth(p1, p2):
	newp1 = [ 5.0 / 9 * p1[0] + 4.0 / 9 * p2[0], 5.0 / 9 * p1[1] + 4.0 / 9 * p2[1]]
	newp2 = [ 4.0 / 9 * p1[0] + 5.0 / 9 * p2[0], 4.0 / 9 * p1[1] + 5.0 / 9 * p2[1]]
	return [newp1, newp2]	
				
def cantor3(points, degree, myTurtle):
	if degree > 0:
		drawSegment(getMiddleThird(points[0], points[1]), 'white', myTurtle)
		[a, b] = getMiddleThird(points[0], points[1])
		left = [points[0], a]
		right = [b, points[1]]
		cantor3(left, degree - 1, myTurtle)
		cantor3(right, degree - 1, myTurtle)
		
def cantor5(points, degree, myTurtle):
	if degree > 0:
		drawSegment(getMiddleFifth(points[0], points[1]), 'white', myTurtle)
		[a, b] = getMiddleFifth(points[0], points[1])
		left = [points[0], a]
		right = [b, points[1]]
		cantor5(left, degree - 1, myTurtle)
		cantor5(right, degree - 1, myTurtle)	
		
def cantor9(points, degree, myTurtle):
	if degree > 0:
		drawSegment(getMiddleNinth(points[0], points[1]), 'white', myTurtle)
		[a, b] = getMiddleNinth(points[0], points[1])
		left = [points[0], a]
		right = [b, points[1]]
		cantor9(left, degree - 1, myTurtle)
		cantor9(right, degree - 1, myTurtle)	
		
def main():
	t = turtle.Turtle()
	t.speed(0)
	myWin = turtle.Screen()
	myPoints = [[-364.5, 0], [364.5, 0] ]
	drawSegment(myPoints, 'black', t)
	cantor9(myPoints, 8, t)
	myWin.exitonclick()
	
main()			 
		
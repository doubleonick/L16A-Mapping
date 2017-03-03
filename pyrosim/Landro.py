import random, math

import constants as c

from individual import INDIVIDUAL 

def Random_X():

	return random.random()*(c.endX-c.startX) + c.startX

def Random_Y():

	return random.random()*(c.endY-c.startY) + c.startY

def Random_Theta():

	return random.random()*2.0*math.pi

# --------------- Start of the program ---------------

ind = INDIVIDUAL()

initialX = Random_X()

initialY = Random_Y() 

initialTheta = Random_Theta() 

ind.Evaluate(initialX,initialY,initialTheta,pb=False)

print 'total light collected = ' + str(ind.fitness)


import numpy as np

import constants as c

lookupTable = np.zeros([c.ticksX,c.ticksY,c.ticksTheta,19])

f = open('../data.csv','r')

f.readline()

for line in f.readlines():

	line = line.split(',')

	x = float(line[0])
	y = float(line[1])
	theta = float(line[2])

	xIndex = x / c.endX

	print x,y,theta, xIndex

f.close()


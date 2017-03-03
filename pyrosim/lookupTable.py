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

	xIndex = int(x * (c.ticksX-1) / c.endX)

        yIndex = int(y * (c.ticksY-1) / c.endY)

        thetaIndex = int(theta * (c.ticksTheta-1) / c.endTheta)

	lookupTable[xIndex,yIndex,thetaIndex,0] = x
        lookupTable[xIndex,yIndex,thetaIndex,1] = y
        lookupTable[xIndex,yIndex,thetaIndex,2] = theta

	for s in range(3,19):
		lookupTable[xIndex,yIndex,thetaIndex,s] = float(line[s])

f.close()

for x in range(0,13):

	for y in range(0,8):

		for o in range(0,16):

			print lookupTable[x,y,o,:]


from pyrosim import PYROSIM

from arena import ARENA

from robot import ROBOT

import constants as c

import numpy as np

import random

import math

class INDIVIDUAL:

        def __init__(self):

		self.sim = PYROSIM(playPaused=False)

		self.arena = ARENA(self.sim)

		xPosition = random.random()*(c.endX-c.startX) + c.startX

                yPosition = random.random()*(c.endY-c.startY) + c.startY

		randomTheta = 3.0*math.pi/2.0 # random.random()*2.0*math.pi

		self.robot = ROBOT(self.sim, x = xPosition , y = yPosition , theta = randomTheta) 

		self.sim.Start()

		exit()

		self.sim.Wait_To_Finish()

		x = self.sim.Get_Sensor_Data(sensorID=0,s=0)

                y = self.sim.Get_Sensor_Data(sensorID=0,s=1)

		x = x / c.sf

		y = y / c.sf

		theta = self.sim.Get_Sensor_Data(sensorID=0,s=2)

		theta = 180.0 * theta / math.pi

		print x

		print ''

		print y

		print ''

		print theta


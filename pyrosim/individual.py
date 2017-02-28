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

		self.sim.Wait_To_Finish()

		sd = self.sim.Get_Sensor_Data(sensorID=0,s=0)

		print sd


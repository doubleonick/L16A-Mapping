from pyrosim import PYROSIM

from arena import ARENA

from robot import ROBOT

import constants as c

import numpy as np

import random

import math

class INDIVIDUAL:

        def __init__(self):

		self.genome = np.random.random([16,2]) * 2 - 1 

		self.fitness = 0.0

	def Evaluate(self):

		sim = PYROSIM(playPaused=False)

		arena = ARENA(sim)

		xPosition = random.random()*(c.endX-c.startX) + c.startX

                yPosition = random.random()*(c.endY-c.startY) + c.startY

		randomTheta = 3.0*math.pi/2.0 # random.random()*2.0*math.pi

		robot = ROBOT(sim, self.genome, x = xPosition , y = yPosition , theta = randomTheta)

		sim.Start()

		sim.Wait_To_Finish()


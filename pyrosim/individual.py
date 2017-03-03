from pyrosim import PYROSIM

from arena import ARENA

from robot import ROBOT

import constants as c

import numpy as np

import random

import math

class INDIVIDUAL:

        def __init__(self):

		self.genome = np.random.random([c.numSensors,c.numMotors]) * 2 - 1 

		self.fitness = 0.0

	def Compute_Fitness(self,sim):

		totalLight = 0.0

		for i in range(3,19,2):

			totalLight = totalLight + sim.dataFromPython[0,i,-1]

		self.fitness = totalLight
	
	def Evaluate(self,initialX,initialY,initialTheta,pb):

		sim = PYROSIM(playBlind=pb)

		arena = ARENA(sim)

		robot = ROBOT(sim, self.genome, x = initialX , y = initialY , theta = initialTheta)

		sim.Start()

		sim.Wait_To_Finish()

		self.Compute_Fitness(sim)

	def Mutate(self):

		i = np.random.randint(0,c.numSensors)

		j = np.random.randint(0,c.numMotors)

		self.genome[i,j] = self.genome[i,j]

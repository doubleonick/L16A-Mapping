from pyrosim import PYROSIM

from arena import ARENA

from robot import ROBOT

import constants as c

import numpy as np

import random, copy, math

class INDIVIDUAL:

        def __init__(self):

		self.genome = np.random.random([c.numSensors,c.numMotors]) * 2 - 1 

		self.fitness = 0.0

	def Compute_Fitness(self,sim):

		totalLight = 0.0

		for i in range(4,19,2):

			meanOfCurrentLightSensor = np.mean( sim.dataFromPython[0,i,:] )

			totalLight = totalLight + meanOfCurrentLightSensor

		self.fitness = totalLight
	
	def Evaluate(self,initialX,initialY,initialTheta,pb):

		sim = PYROSIM(playBlind=pb)

		robot = ROBOT(sim, self.genome, x = initialX , y = initialY , theta = initialTheta)

		arena = ARENA(sim)

		sim.Start()

		sim.Wait_To_Finish()

		self.Compute_Fitness(sim)

	def Mutate(self):

		i = np.random.randint(0,c.numSensors)

		j = np.random.randint(0,c.numMotors)

		mean = self.genome[i,j]

		std  = math.fabs( self.genome[i,j] )
 
		self.genome[i,j] = np.random.normal( mean , std ) 

	def Spawn_Mutant(self):

                mutant = copy.deepcopy(self)

                mutant.Mutate()

		return mutant

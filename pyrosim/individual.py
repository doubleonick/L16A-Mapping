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

		self.fitness = self.fitness + totalLight

        def End_Evaluation(self,trialIndex):

                self.sims[trialIndex].Wait_To_Finish()

                self.Compute_Fitness(self.sims[trialIndex])

	def Evaluate(self,initialX,initialY,initialTheta,pb):

		self.sims = {}

		self.Start_Evaluation(0,initialX,initialY,initialTheta,pb)

		self.End_Evaluation(0)

		del self.sims

	def Evaluate_Multiple_Times(self,initialXs,initialYs,initialThetas,pb):

		self.sims = {}

		for t in range(0,c.numTrials):

			self.Start_Evaluation(t,initialXs[t],initialYs[t],initialThetas[t],pb)

                for t in range(0,c.numTrials):

                        self.End_Evaluation(t)

		del self.sims

	def Mutate(self):

		i = np.random.randint(0,c.numSensors)

		j = np.random.randint(0,c.numMotors)

		mean = self.genome[i,j]

		std  = math.fabs( self.genome[i,j] )
 
		self.genome[i,j] = np.random.normal( mean , std ) 

	def Reset(self):

		self.fitness = 0.0

	def Spawn_Mutant(self):

                mutant = copy.deepcopy(self)

                mutant.Mutate()

		mutant.Reset()

		return mutant

        def Start_Evaluation(self,trialIndex,initialX,initialY,initialTheta,pb):

                self.sims[trialIndex] = PYROSIM(playBlind=pb)

                self.robot = ROBOT(self.sims[trialIndex], self.genome, x = initialX , y = initialY , theta = initialTheta)

		del self.robot

                self.arena = ARENA(self.sims[trialIndex])

		del self.arena

                self.sims[trialIndex].Start()

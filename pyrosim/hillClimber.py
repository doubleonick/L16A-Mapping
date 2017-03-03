import math

import constants as c

from individual import INDIVIDUAL

class HILLCLIMBER:

        def __init__(self):

                self.parent = INDIVIDUAL()

                self.initialX = self.Fraction_Of_X(0.5)

                self.initialY = self.Fraction_Of_Y(0.5)

                self.initialTheta = self.Fraction_Of_Theta(0.5)

	def Evolve(self):

		self.parent.Evaluate(self.initialX,self.initialY,self.initialTheta)

		for currentGeneration in range(0,c.numGenerations):

			child = copy.deepcopy(parent)

			child.Mutate()

			child.Evaluate()

			if ( child.fitness > parent.fitness ):

				parent = child

	def Fraction_Of_X(self,fraction):

        	return fraction*(c.endX-c.startX) + c.startX

	def Fraction_Of_Y(self,fraction):

        	return fraction*(c.endY-c.startY) + c.startY

	def Fraction_Of_Theta(self,fraction):

        	return fraction*2.0*math.pi

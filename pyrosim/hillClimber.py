import math

import constants as c

from individual import INDIVIDUAL

class HILLCLIMBER:

        def __init__(self):

                self.initialX = self.Fraction_Of_X(0.5)

                self.initialY = self.Fraction_Of_Y(0.5)

                self.initialTheta = self.Fraction_Of_Theta(0.5)

		self.playBlind = True

        def Child_Competes_Against_Parent(self):

                if ( self.child.fitness > self.parent.fitness ):

                        self.parent = self.child

	def Evolve(self):

                self.parent = INDIVIDUAL()

		self.parent.Evaluate(self.initialX,self.initialY,self.initialTheta,self.playBlind)

		for self.currentGeneration in range(0,c.numGenerations):

			self.Perform_One_Generation()

	def Fraction_Of_X(self,fraction):

        	return fraction*(c.endX-c.startX) + c.startX

	def Fraction_Of_Y(self,fraction):

        	return fraction*(c.endY-c.startY) + c.startY

	def Fraction_Of_Theta(self,fraction):

        	return fraction*2.0*math.pi

        def Perform_One_Generation(self):

		self.child = self.parent.Spawn_Mutant()

                self.child.Evaluate(self.initialX,self.initialY,self.initialTheta,self.playBlind)

                self.Print()

		self.Child_Competes_Against_Parent()

	def Print(self):

		print 'Generation ' + str(self.currentGeneration) + ' of ' + str(c.numGenerations) + '. ',

		print 'Parent fitness: ' + str(self.parent.fitness),

		print 'Child fitness: ' + str(self.child.fitness)

	def Show_Best(self):

		self.parent.Evaluate(self.initialX,self.initialY,self.initialTheta,pb=False)	

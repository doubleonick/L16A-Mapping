import math

import numpy as np

import constants as c

from individual import INDIVIDUAL

class HILLCLIMBER:

        def __init__(self):

		self.Create_Trials()

		self.playPaused = False

		self.playBlind = True

        def Child_Competes_Against_Parent(self):

                if ( self.child.fitness > self.parent.fitness ):

                        self.parent = self.child

        def Create_Trials(self):

                self.initialXs = np.random.random(c.numTrials)

                self.initialYs = np.random.random(c.numTrials)

                self.initialThetas = np.random.random(c.numTrials)

		for t in range(0,c.numTrials):

			self.initialXs[t] = self.Fraction_Of_X(self.initialXs[t])

                        self.initialYs[t] = self.Fraction_Of_Y(self.initialYs[t])

                        self.initialThetas[t] = self.Fraction_Of_Theta(self.initialThetas[t])

	def Evolve(self):

                self.parent = INDIVIDUAL()

		self.parent.Evaluate_Multiple_Times(self.initialXs,self.initialYs,self.initialThetas,self.playPaused,self.playBlind)

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

                self.child.Evaluate_Multiple_Times(self.initialXs,self.initialYs,self.initialThetas,self.playPaused,self.playBlind)

                self.Print()

		self.Child_Competes_Against_Parent()

	def Print(self):

		print 'Generation ' + str(self.currentGeneration) + ' of ' + str(c.numGenerations) + '. ',

		print 'Parent fitness: ' + str(self.parent.fitness),

		print 'Child fitness: ' + str(self.child.fitness)

	def Show_Best(self):

		self.parent.Evaluate_Multiple_Times(self.initialXs,self.initialYs,self.initialThetas,pp=True,pb=False)	

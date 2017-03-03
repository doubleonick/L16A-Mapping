from individual import INDIVIDUAL

class HILLCLIMBER:

        def __init__(self):

		self.parent = INDIVIDUAL()

	def Evolve(self):

		self.parent.Evaluate()

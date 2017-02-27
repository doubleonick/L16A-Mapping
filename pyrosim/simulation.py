from pyrosim import PYROSIM

from arena import ARENA

from robot import ROBOT

import constants as c

import numpy as np

class SIMULATION:

        def __init__(self):

		self.sim = PYROSIM(playPaused=False)

		self.arena = ARENA(self.sim)

		self.robot = ROBOT(self.sim)

		# self.Create_Robot(self.sim)

		self.sim.Start()


from pyrosim import PYROSIM

from arena import ARENA

from robot import ROBOT

import constants as c

import numpy as np

import random

class SIMULATION:

        def __init__(self):

		self.sim = PYROSIM(playPaused=False)

		self.arena = ARENA(self.sim)

		xPosition = random.random()*(c.endX-c.startX) + c.startX

                yPosition = random.random()*(c.endY-c.startY) + c.startY

		self.robot = ROBOT(self.sim, x = xPosition , y = yPosition , theta = 0.0 )

		self.sim.Start()


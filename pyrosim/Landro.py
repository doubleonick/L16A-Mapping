from pyrosim import PYROSIM

import constants as c

def Create_Back_Wall(sim):

	sim.Send_Box(objectID=0, x=c.maxX/2, y=0, z=c.wallWidth/2, length=c.maxX, width=c.wallWidth, height=c.wallWidth)

def Create_Front_Wall(sim):

        sim.Send_Box(objectID=1, x=c.maxX/2, y=c.maxY, z=c.wallWidth/2, length=c.maxX, width=c.wallWidth, height=c.wallWidth)

def Create_Left_Wall(sim):

	sim.Send_Box(objectID=2, x=0, y=c.maxY/2, z=c.wallWidth/2, length=c.wallWidth, width=c.maxY, height=c.wallWidth)

def Create_Right_Wall(sim):

        sim.Send_Box(objectID=3, x=c.maxX, y=c.maxY/2, z=c.wallWidth/2, length=c.wallWidth, width=c.maxY, height=c.wallWidth)
	
def Create_Arena(sim):

	Create_Back_Wall(sim)

	Create_Front_Wall(sim)

	Create_Left_Wall(sim)

	Create_Right_Wall(sim)

# ------ Main function ---------

sim = PYROSIM(playPaused=True)

Create_Arena(sim)

sim.Start()

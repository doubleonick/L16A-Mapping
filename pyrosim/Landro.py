from pyrosim import PYROSIM

import constants as c

import numpy as np

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

def Create_Position_Markers(sim):

	currentID = 4

	for x in np.arange( c.startX , c.endX+0.001 , c.spacingX ):

		for y in np.arange( c.startY , c.endY + 0.001 , c.spacingY ):

			sim.Send_Cylinder(objectID=currentID, x=x, y=y, z=c.wallWidth/2, length=0.0, radius=c.wallWidth/2)

			currentID = currentID + 1	

def Create_Robot_At(sim,x,y,theta):

	currentID = 4

	# Main body
	sim.Send_Cylinder(objectID=currentID,x=x,y=y,z=c.bodyRadius,length=0.0, radius = c.bodyRadius)
	currentID = currentID + 1

        # Front wheel 
        sim.Send_Cylinder(objectID=currentID,x=x+c.bodyRadius,y=y,z=c.wheelRadius,length=0.0, radius = c.wheelRadius, r=0, g=1, b=0)
        currentID = currentID + 1

        # Right wheel
        sim.Send_Cylinder(objectID=currentID,x=x,y=y-c.bodyRadius,z=c.wheelRadius,length=0.0, radius = c.wheelRadius, r=0, g=0, b=1)
        currentID = currentID + 1

        # Back wheel
        sim.Send_Cylinder(objectID=currentID,x=x-c.bodyRadius,y=y,z=c.wheelRadius,length=0.0, radius = c.wheelRadius, r=1, g=0, b=1)
        currentID = currentID + 1

        # Left wheel
        sim.Send_Cylinder(objectID=currentID,x=x,y=y+c.bodyRadius,z=c.wheelRadius,length=0.0, radius = c.wheelRadius, r=1, g=0, b=0)
        currentID = currentID + 1

def Create_Robot(sim):

	Create_Robot_At(sim, x = c.startX , y = c.startY , theta = 0.0 )
	
# ------ Main function ---------

sim = PYROSIM(playPaused=True)

Create_Arena(sim)

# Create_Position_Markers(sim)

Create_Robot(sim)

sim.Start()

import constants as c

import numpy as np

class ARENA:

        def __init__(self,sim):

		self.Create_Arena(sim)

		# self.Create_Position_Markers(sim)

        def Create_Arena(self,sim):

                self.Create_Back_Wall(sim)

                self.Create_Front_Wall(sim)

                self.Create_Left_Wall(sim)

                self.Create_Right_Wall(sim)

	def Create_Back_Wall(self,sim):

        	sim.Send_Box(objectID=0, x=c.maxX*c.sf/2, y=0, z=c.wallWidth*c.sf, length=c.maxX*c.sf, width=c.wallWidth*c.sf, height=c.wallWidth*c.sf*2)

	def Create_Front_Wall(self,sim):

        	sim.Send_Box(objectID=1, x=c.maxX*c.sf/2, y=c.maxY*c.sf, z=c.wallWidth*c.sf, length=c.maxX*c.sf, width=c.wallWidth*c.sf, height=c.wallWidth*c.sf*2)

	def Create_Left_Wall(self,sim):

        	sim.Send_Box(objectID=2, x=0, y=c.maxY*c.sf/2, z=c.wallWidth*c.sf, length=c.wallWidth*c.sf, width=c.maxY*c.sf, height=c.wallWidth*c.sf*2)

	def Create_Position_Markers(self,sim):

        	currentID = 4

        	for x in np.arange( c.startX , c.endX+0.001 , c.spacingX ):

                	for y in np.arange( c.startY , c.endY + 0.001 , c.spacingY ):

                        	sim.Send_Cylinder(objectID=currentID, x=x, y=y, z=c.wallWidth/2, length=0.0, radius=c.wallWidth/2)

                        	currentID = currentID + 1

        def Create_Right_Wall(self,sim):

                sim.Send_Box(objectID=3, x=c.maxX*c.sf, y=c.maxY*c.sf/2, z=c.wallWidth*c.sf, length=c.wallWidth*c.sf, width=c.maxY*c.sf, height=c.wallWidth*c.sf*2)

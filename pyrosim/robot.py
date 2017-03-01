import constants as c
import random
import math

class ROBOT:

        def __init__(self,sim,x,y,theta):

		self.Create_Robot(sim,x,y,theta)

	def Create_Joints(self,sim,x,y,theta):

                objX = x + c.bodyRadius * math.sin(theta + math.pi/2)
                objY = y + c.bodyRadius * math.cos(theta + math.pi/2)

		firstN1 = math.sin(theta)
		firstN2 = math.cos(theta)

		# Front joint
		sim.Send_Joint(jointID=0, firstObjectID=4, secondObjectID=5, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=firstN1, n2=firstN2, n3=0, positionControl = False)

                secondN1 = math.sin(theta + math.pi/2)
                secondN2 = math.cos(theta + math.pi/2)

                sim.Send_Joint(jointID=1, firstObjectID=5, secondObjectID=6, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=secondN1, n2=secondN2, n3=0, positionControl = False)

                objX = x + c.bodyRadius * math.sin(theta + math.pi/2 + math.pi/2)
                objY = y + c.bodyRadius * math.cos(theta + math.pi/2 + math.pi/2)

                # Right joint
                sim.Send_Joint(jointID=2, firstObjectID=4, secondObjectID=7, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=firstN1, n2=firstN2, n3=0, lo=-c.speed, hi=+c.speed, positionControl = False)

                objX = x + c.bodyRadius * math.sin(theta + math.pi/2 + math.pi)
                objY = y + c.bodyRadius * math.cos(theta + math.pi/2 + math.pi)

                # Back joint
                sim.Send_Joint(jointID=3, firstObjectID=4, secondObjectID=8, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=firstN1, n2=firstN2, n3=0, positionControl = False)

                sim.Send_Joint(jointID=4, firstObjectID=8, secondObjectID=9, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=secondN1, n2=secondN2, n3=0, positionControl = False)

                objX = x + c.bodyRadius * math.sin(theta + math.pi/2 + 3*math.pi/2)
                objY = y + c.bodyRadius * math.cos(theta + math.pi/2 + 3*math.pi/2)

                # Left joint
                sim.Send_Joint(jointID=5, firstObjectID=4, secondObjectID=10, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=firstN1, n2=firstN2, n3=0, lo=-c.speed, hi=+c.speed, positionControl = False)

		# Make the arena walls immovable. 

		for w in range(0,4):

			sim.Send_Joint(jointID=6+w, firstObjectID=w, secondObjectID=-1)

	def Create_Neurons(self,sim):

		for t in range(0,3):

			sim.Send_Sensor_Neuron(neuronID=t, sensorID=0, sensorValueIndex=t, tau=0.1)

		sim.Send_Motor_Neuron(neuronID=3, jointID=2, tau=0.1)

                sim.Send_Motor_Neuron(neuronID=4, jointID=5, tau=0.1)
	
	def Create_Objects(self,sim,x,y,theta):

        	currentID = 4

        	# Main body
        	sim.Send_Cylinder(objectID=currentID,x=x*c.sf,y=y*c.sf,z=c.bodyRadius*c.sf+0.01,length=0.0, radius = c.bodyRadius*c.sf)
        	currentID = currentID + 1

                objX = x + c.bodyRadius * math.sin(theta + math.pi/2)
                objY = y + c.bodyRadius * math.cos(theta + math.pi/2)

        	# Front wheel (two objects to simulate castor wheel)
        	sim.Send_Cylinder(objectID=currentID,x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf,length=0.0, radius = c.wheelRadius*c.sf, r=0, g=1, b=0)
        	currentID = currentID + 1

                sim.Send_Cylinder(objectID=currentID,x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf,length=0.0, radius = c.wheelRadius*c.sf, r=0, g=.5, b=0)
                currentID = currentID + 1

                objX = x + c.bodyRadius * math.sin(theta + math.pi/2 + math.pi/2)
                objY = y + c.bodyRadius * math.cos(theta + math.pi/2 + math.pi/2)

        	# Right wheel
        	sim.Send_Cylinder(objectID=currentID,x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf,length=0.0, radius = c.wheelRadius*c.sf, r=0, g=0, b=1)
        	currentID = currentID + 1

                objX = x + c.bodyRadius * math.sin(theta + math.pi/2 + math.pi)
                objY = y + c.bodyRadius * math.cos(theta + math.pi/2 + math.pi)

        	# Back wheel (two objects to simulate castor wheel)
        	sim.Send_Cylinder(objectID=currentID,x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf,length=0.0, radius = c.wheelRadius*c.sf, r=1, g=0, b=1)
        	currentID = currentID + 1

                sim.Send_Cylinder(objectID=currentID,x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf,length=0.0, radius = c.wheelRadius*c.sf, r=.5, g=0, b=.5)
                currentID = currentID + 1

                objX = x + c.bodyRadius * math.sin(theta + math.pi/2 + 3*math.pi/2)
                objY = y + c.bodyRadius * math.cos(theta + math.pi/2 + 3*math.pi/2)

        	# Left wheel
        	sim.Send_Cylinder(objectID=currentID,x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf,length=0.0, radius = c.wheelRadius*c.sf, r=1, g=0, b=0)
        	currentID = currentID + 1

        def Create_Robot(self,sim,x,y,theta):

                self.Create_Objects(sim,x,y,theta)

		self.Create_Joints(sim,x,y,theta)

		self.Create_Sensors(sim)

		self.Create_Neurons(sim)

		self.Create_Synapses(sim)

	def Create_Sensors(self,sim):

		sim.Send_Position_Sensor(sensorID = 0 , objectID = 4 )

	def Create_Synapses(self,sim):

		for s in range(0,3):

			for m in range(0,2):

				sim.Send_Synapse(sourceNeuronID = s , targetNeuronID = 3+m , weight = random.random()*2-1 )

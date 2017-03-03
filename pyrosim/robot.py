import constants as c
import random
import math

class ROBOT:

        def __init__(self,sim,x,y,theta):

		self.Create_Robot(sim,x,y,theta)

	def Create_Joints(self,sim,x,y,theta):

		# Front joint
                objX = x + (c.bodyRadius-c.wheelRadius) * math.sin(theta + math.pi/2)
                objY = y + (c.bodyRadius-c.wheelRadius) * math.cos(theta + math.pi/2)
		firstN1 = math.sin(theta)
		firstN2 = math.cos(theta)
		sim.Send_Joint(jointID=0, firstObjectID=4, secondObjectID=5, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=firstN1, n2=firstN2, n3=0, positionControl = False, ballAndSocket=True)

		# Right joint
                objX = x + (c.bodyRadius-c.wheelRadius) * math.sin(theta + math.pi/2 + math.pi/2)
                objY = y + (c.bodyRadius-c.wheelRadius) * math.cos(theta + math.pi/2 + math.pi/2)
                sim.Send_Joint(jointID=1, firstObjectID=4, secondObjectID=6, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=firstN1, n2=firstN2, n3=0, lo=-c.speed, hi=+c.speed, positionControl = False)

		# Back joint
                objX = x + (c.bodyRadius-c.wheelRadius) * math.sin(theta + math.pi/2 + math.pi)
                objY = y + (c.bodyRadius-c.wheelRadius) * math.cos(theta + math.pi/2 + math.pi)
                sim.Send_Joint(jointID=2, firstObjectID=4, secondObjectID=7, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=firstN1, n2=firstN2, n3=0, positionControl = False, ballAndSocket=True)

		# Left joint
                objX = x + (c.bodyRadius-c.wheelRadius) * math.sin(theta + math.pi/2 + 3*math.pi/2)
                objY = y + (c.bodyRadius-c.wheelRadius) * math.cos(theta + math.pi/2 + 3*math.pi/2)
                sim.Send_Joint(jointID=3, firstObjectID=4, secondObjectID=8, x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf, n1=firstN1, n2=firstN2, n3=0, lo=-c.speed, hi=+c.speed, positionControl = False)

		# Make the arena walls immovable. 

		for w in range(0,4):

			sim.Send_Joint(jointID=4+w, firstObjectID=w, secondObjectID=-1)

	def Create_Neurons(self,sim):

		for s in range(0,16):

			sim.Send_Sensor_Neuron(neuronID=s, sensorID=0, sensorValueIndex=s + 3, tau=1.0)

		sim.Send_Motor_Neuron(neuronID=16, jointID=1, tau=1.0)

                sim.Send_Motor_Neuron(neuronID=17, jointID=3, tau=1.0)
	
	def Create_Objects(self,sim,x,y,theta):

        	currentID = 4

        	# Main body
        	sim.Send_Cylinder(objectID=currentID,x=x*c.sf,y=y*c.sf,z=c.bodyRadius*c.sf+0.01,length=0.0, radius = c.bodyRadius*c.sf)
        	currentID = currentID + 1

        	# Front wheel
                objX = x + (c.bodyRadius-c.wheelRadius) * math.sin(theta + math.pi/2)
                objY = y + (c.bodyRadius-c.wheelRadius) * math.cos(theta + math.pi/2)
        	sim.Send_Cylinder(objectID=currentID,x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf,length=0.0, radius = c.wheelRadius*c.sf, r=0, g=1, b=0)
        	currentID = currentID + 1

                # Right wheel
                objX = x + (c.bodyRadius-c.wheelRadius) * math.sin(theta + math.pi/2 + math.pi/2)
                objY = y + (c.bodyRadius-c.wheelRadius) * math.cos(theta + math.pi/2 + math.pi/2)
        	sim.Send_Cylinder(objectID=currentID,x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf,length=0.0, radius = c.wheelRadius*c.sf, r=0, g=0, b=1)
        	currentID = currentID + 1

                # Back wheel 
                objX = x + (c.bodyRadius-c.wheelRadius) * math.sin(theta + math.pi/2 + math.pi)
                objY = y + (c.bodyRadius-c.wheelRadius) * math.cos(theta + math.pi/2 + math.pi)
        	sim.Send_Cylinder(objectID=currentID,x=objX*c.sf,y=objY*c.sf,z=c.wheelRadius*c.sf,length=0.0, radius = c.wheelRadius*c.sf, r=1, g=0, b=1)
        	currentID = currentID + 1

                # Left wheel
                objX = x + (c.bodyRadius-c.wheelRadius) * math.sin(theta + math.pi/2 + 3*math.pi/2)
                objY = y + (c.bodyRadius-c.wheelRadius) * math.cos(theta + math.pi/2 + 3*math.pi/2)
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

		for s in range(0,16):

			for m in range(0,2):

				sim.Send_Synapse(sourceNeuronID = s , targetNeuronID = 16 + m , weight = random.random()*2-1 )

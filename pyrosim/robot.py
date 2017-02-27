import constants as c
import random

class ROBOT:

        def __init__(self,sim):

		self.Create_Robot(sim)

	def Create_Joints(self,sim,x,y,theta):

		# Front joint
		sim.Send_Joint(jointID=0, firstObjectID=4, secondObjectID=5, x=x+c.bodyRadius,y=y,z=c.wheelRadius, n1=0, n2=1, n3=0, positionControl = False)

                # Right joint
                sim.Send_Joint(jointID=1, firstObjectID=4, secondObjectID=6, x=x,y=y-c.bodyRadius,z=c.wheelRadius, n1=0, n2=1, n3=0, positionControl = False)

                # Back joint
                sim.Send_Joint(jointID=2, firstObjectID=4, secondObjectID=7, x=x-c.bodyRadius,y=y,z=c.wheelRadius, n1=0, n2=1, n3=0, positionControl = False)

                # Left joint
                sim.Send_Joint(jointID=3, firstObjectID=4, secondObjectID=8, x=x,y=y+c.bodyRadius,z=c.wheelRadius, n1=0, n2=1, n3=0, positionControl = False)

	def Create_Neurons(self,sim):

		for t in range(0,4):

			sim.Send_Sensor_Neuron(neuronID=t, sensorID=t)

		sim.Send_Motor_Neuron(neuronID=4, jointID=1)

                sim.Send_Motor_Neuron(neuronID=5, jointID=3)
	
	def Create_Objects(self,sim,x,y,theta):

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

	def Create_Robot(self,sim):

       		self.Create_Robot_At(sim, x = c.startX , y = c.startY , theta = 0.0 )

        def Create_Robot_At(self,sim,x,y,theta):

                self.Create_Objects(sim,x,y,theta)

		self.Create_Joints(sim,x,y,theta)

		self.Create_Sensors(sim)

		self.Create_Neurons(sim)

		self.Create_Synapses(sim)

	def Create_Sensors(self,sim):

		for t in range(0,4):

			sim.Send_Touch_Sensor(sensorID=t, objectID=5+t)

	def Create_Synapses(self,sim):

		for s in range(0,4):

			for m in range(0,2):

				sim.Send_Synapse(sourceNeuronID = s , targetNeuronID = 4+m , weight = random.random()*2-1 )

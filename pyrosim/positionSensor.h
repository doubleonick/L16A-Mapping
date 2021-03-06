#ifndef _POSITION_SENSOR_H
#define _POSITION_SENSOR_H

#include <ode/ode.h>

class NEURON;

class POSITION_SENSOR {

private:

	int ID;

	double *vals; 

        NEURON** mySensorNeurons;

public:
	POSITION_SENSOR(int myID, int evalPeriod);

	~POSITION_SENSOR(void);

        void Connect_To_Sensor_Neuron(NEURON *sensorNeuron);

        int  Get_ID(void);

	void Poll(dBodyID body, int t, double x, double y, double theta);

        void Update_Sensor_Neurons(int t);

	void Write_To_Python(int evalPeriod);
};

#endif

#ifndef _POSITION_SENSOR_CPP
#define _POSITION_SENSOR_CPP

#include "iostream"
#include "positionSensor.h"
#include "neuron.h"

POSITION_SENSOR::POSITION_SENSOR(int myID, int evalPeriod) {

	ID = myID;

	vals = new double[16*evalPeriod];

	mySensorNeurons = new NEURON*[16];

	for ( int i = 0 ; i < 16 ; i++)

        	mySensorNeurons[i] = NULL;
}

POSITION_SENSOR::~POSITION_SENSOR(void) {

}

void POSITION_SENSOR::Connect_To_Sensor_Neuron(NEURON *sensorNeuron) {

	mySensorNeurons[ sensorNeuron->Get_Sensor_Value_Index() ] = sensorNeuron;
}

int  POSITION_SENSOR::Get_ID(void) {

        return ID;
}

void POSITION_SENSOR::Poll(dBodyID body, int t, double theta) {

	for (int i = 0 ; i < 16 ; i++ )

		vals[16*t + i] = theta; 
}

void POSITION_SENSOR::Update_Sensor_Neurons(int t) {

	for (int i = 0 ; i < 16 ; i++ )

		if ( mySensorNeurons[i] ) 

			mySensorNeurons[i]->Set( vals[16*t + i] );
}

void POSITION_SENSOR::Write_To_Python(int evalPeriod) {

        char outString[1000000];

        sprintf(outString,"%d %d ",ID,16);

        for ( int  t = 0 ; t < evalPeriod ; t++ ) 

		for ( int i = 0 ; i < 16 ; i++ )

                	sprintf(outString,"%s %f ",outString,vals[16*t + i]);

        sprintf(outString,"%s \n",outString);

        std::cout << outString;
}

#endif

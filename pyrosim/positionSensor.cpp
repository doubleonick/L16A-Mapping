#ifndef _POSITION_SENSOR_CPP
#define _POSITION_SENSOR_CPP

#include "iostream"
#include "positionSensor.h"
#include "neuron.h"
#include "sensorData.h"

POSITION_SENSOR::POSITION_SENSOR(int myID, int evalPeriod) {

	ID = myID;

	vals = new double[19*evalPeriod];

	mySensorNeurons = new NEURON*[19];

	for ( int i = 0 ; i < 19 ; i++)

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

void POSITION_SENSOR::Poll(dBodyID body, int t, double x, double y, double theta) {

	std::cerr << x << " ";
        std::cerr << y << " ";
        std::cerr << theta << "   ";

        int xIndex = int(x * (ticksX-1) / endX);

        int yIndex = int(y * (ticksY-1) / endY);

        int thetaIndex = int(theta * (ticksTheta-1) / endTheta);

        std::cerr << xIndex << " ";
        std::cerr << yIndex << " ";
        std::cerr << thetaIndex << "   ";


	vals[19*t + 0] = x;

	vals[19*t + 1] = y;

	vals[19*t + 2] = theta;

        for (int j = 3 ; j < 19 ; j++ ) {
                
                vals[19*t + j] = sensorData[ xIndex*(8*16*19) + yIndex*(16*19) + thetaIndex*19 + j ]; 

		std::cerr << vals[19*t + j] << " ";
	}
	std::cerr << "\n";
}

void POSITION_SENSOR::Update_Sensor_Neurons(int t) {

	for (int j = 0 ; j < 19 ; j++ )

		if ( mySensorNeurons[j] ) 

			mySensorNeurons[j]->Set( vals[19*t + j] );

			//mySensorNeurons[i]->Set( ((double) rand() / (RAND_MAX))*2.0 - 1.0 );

			// mySensorNeurons[i]->Set( 1.0 );
}

void POSITION_SENSOR::Write_To_Python(int evalPeriod) {

        char outString[1000000];

        sprintf(outString,"%d %d ",ID,19);

        for ( int  t = 0 ; t < evalPeriod ; t++ ) 

		for ( int i = 0 ; i < 19 ; i++ )

                	sprintf(outString,"%s %f ",outString,vals[19*t + i]);

        sprintf(outString,"%s \n",outString);

        std::cout << outString;
}

#endif

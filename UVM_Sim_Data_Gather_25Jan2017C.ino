  /*This is the code for running the robot without learning.
  It is important to remmebr to put in the SD card and uncomment
  the roboNum line to track the test number. After that simply 
  connect to the robot and click upload and disconnect when finished.
  ALSO: This file should be read only so that you need to put in test
  number each time. If it is not make it so.*/

#include <SoftwareSerial.h>
#include <Servo.h>
#include <SPI.h>
#include <SD.h> 

//This includes params.h, so the file MUST be called that
#include "params.h"

#define baudPin  11
#define contPin  2

//This code is designed especially to perform data gathering
//for a simulation of L16A that will be performed by UVM.
//We are going to perform some number of data gathering trials.
//We do not care how many trials are to be performed, but it does
//matter for logging purposes which trial we are on (starting with 0).

//A trial will proceed as follows.  The program will hang until the front
//iRobot Create bumper is pressed (both left AND right).  Upon this cue,
//the robot will read all of its sensors (8 LDR and 8 IR), and store these
//values in one array.  A function will then be called, which will record
//these 16 (numPorts) values in the following way.
//There will be a micro SD card plugged into the Landro.  It can have
//files written to it with the name convention "datalog#.txt", where "#"
//is some number between 0 and, when last checked sometime in 2015, 9.
//The following information must be recorded:
//1. Which trial are we on?
//2. Which sensor are we recording?  What is its type and position relative
//to the front of the robot?  Position can just be 0 through 15 and 
//correspond to port number.
//3. What are the world coordinates (x, y, phi) at which we're recording?
//4. What are the sensor values?
//Once numPorts values have been recorded for a given (x, y, phi), the robot
//should check which phi it is at.  If it is at 360, it should stop.
//Otherwise, if it is at phi = [0:337.5], it should rotate in place 22.5 degrees.
//After rotating, it should repeat the data logging procedure.
//At phi = 360, the robot should stop its motors, play a tune, and wait for
//its Create bumpers to be pressed.
//Pressing these bumpers should increment the trial number, reset phi to 0,
//update x and y (this means there must be a predetermined pattern of
//trials), and start a new sequence of data collection.
//Coordinate axes, x and y shall be enumerated in arrays.  The index of each array
//shall correspond to the trial number (this is why we start with trial 0, not 1).

//Terms:
//numPositions = the number of x, y coordinates
//numOrientations = the number of orientations to visit.
//trailNum = a count of the (x,y) coordinate we're visiting.
//x = current x coordinate
//y = current y coordinate
//phi = robot orientation at (x,y)
//numPorts = the number of ports that have sensors in them.
//sensorValues[] = the values of the numPorts sensors
//senseThinkTime = the amount of time taken to read through sensors and record data
//clockTime = the current time in milliseconds
//actTime = the amount of time spent spinning to the new phi
const int numSensorSamples = 10;
const int numPorts         = 16;
int numPositions           = 84;
int numXs                  = 12;
int numYs                  = 7;
int numOrientations        = 16;
int trialNum               = 0;
//float yIndent              = 18.5;
float xIndent              = 18.7;
//float yCoordinate          = yIndent;//Short axis... 7 points
float xCoordinate          = xIndent;//Long axis... 12 points
float xyIncrement          = 30;
float phi                  = 0;
float phiIncrement         = 22.5;
//int whichTrial             = 0;
int sensorValues[numPorts][numSensorSamples] = {};
int senseThinkTime;
int actTime;
unsigned long clockTime;
int transitionTime;
int motorSpeed = 50;
//For debugging purposes in determing correct spin times for 360 and 22.5 degrees
unsigned long trialTime;
String datalogNames[numSensorSamples] = {"datalog0.txt","datalog1.txt","datalog2.txt","datalog3.txt","datalog4.txt","datalog5.txt","datalog6.txt","datalog7.txt","datalog8.txt","datalog9.txt"};

//iRobot Create left and right bump values
int bumpRight = 0;
int bumpLeft = 0;

//Continue with the experiment?
int contExp;

//NBL: What's this for?
const int chipSelect = 53;

void sense();

void record();

void act();

void transition();

/**********************************************************/
//This simply turns the the motor values into the correct 
// bytes and sends them to the iCreate for basic driving
void driveDirect(int rightValue, int leftValue);
//This is somewhat complicated and I don't know exactly how it all works
// but it does so that's pretty good. It just reads the byte stream basically
// after asking for the info
bool checkBumpSensors();
/********************************************************/
//Just stops the robot and plays and happy tune to let you
// know the test is over
void endTest();
/**************************************************************/
//Limits speed to a range between -400 and 400 by clipping it.
int checkSpeed(int spd);
  

//https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf
/***************************************/
void setup(){
  delay(2000);
  //Open communication with iCreate
  pinMode(baudPin, OUTPUT);
  Serial3.begin(19200);
  //set data rate for the SoftwareSerial port, this is the iRobot's default
  digitalWrite(baudPin, LOW);
  delay(500);
  digitalWrite(baudPin, LOW);
  delay(500);
  digitalWrite(baudPin, LOW);
  delay(500);
  
  //Start robot in safe mode
  Serial3.write(128);
  Serial3.write(131);//Safe = 131, Full = 132
  delay(1000);
  // Open serial communications and wait for port to open:
  Serial.begin(19200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }


  Serial.print("Initializing SD card...");
    
  // see if the card is present and can be initialized:
  while (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    //return;
  }
  Serial.println("card initialized.");

  pinMode(contPin, INPUT);
  contExp = false;

  //Initialize sensor values
  for(int i = 0; i < numPorts; i++){
    for(int j = 0; j < numSensorSamples; j++){
      sensorValues[i][j] = 0;
    }
  }

  //The amount of time that
  //we'll wait for the robot to read its sensors and process data (if ANN is in use)
  senseThinkTime = 500;
  //The amount of time in ms to spin in place to the next
  //data collection orientation (phi)
  actTime        = 830;//12950/16;//For -40, 40 motor speed, works perfectly the first time, then starts to drift when each subsequent loop is triggered by the bumper
  //18Jan2016: 12950 Works for repeated, full 360 rotations.  But doing 16 increments falls short of the 360 trip.  Each successive increment accululates drift.
  //It's almost as though a slight delay has to be added each time, and then a reset done at the end....
  //The amount of time requried to drive foward 30 cm
  transitionTime = 5350;//This isn't 30 cm yet

}

/***************************************************************/
//This is the main loop of arduino code and calls everything else
// if there are issues something may be commented out here

void loop(){
  
    int i;
    
    unsigned long endTime = 0;
    unsigned long startTime = millis();

    //For debugging
    //numOrientations = 0;
    for(i = 0; i < numOrientations; i ++){
      Serial.println("Here we go again");
      act();
      driveDirect(0, 0);
      sense();
      record();
      phi += phiIncrement;
      delay(senseThinkTime);
     //actTime += 10;
    }
    //Reset orientation
    phi = 0;
    //endTime = millis();
    //trialTime = endTime - startTime;
    //actTime = 12950/16;

    //Change and check x, y coordinates
    xCoordinate += xyIncrement;
    if(xCoordinate > xIndent + (numXs * xyIncrement)){
      xCoordinate = xIndent;
      //Leave this out for debugging for now.
      //recordDataSet();
      endTest(1);
    }
    //We have come to the end of the trial.  A song will play on loop until the
    //front bumper is pressed.  You with then have 1 second to get out of the way.
    //After the bumper is pressed, the bot will drive forward 30 cm to the next 
    //trial position.
    //End rotations... signal transition (drive straight to next (x, y)).
    //endTest(0);
    //Drive to next (x, y )
    delay(1000);
    transition();
    //driveDirect(0, 0);
    //delay(5000);
    //Signal end of getting to next (x, y).  Press bumper to start next set of rotations
    endTest(0);
}

void sense(){
  int i, j;
  int samples = 10;
  int analogPorts[numPorts] = {A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15};
  for(i = 0; i < numPorts; i++){
    for(j = 0; j < samples; j++){
      sensorValues[i][j] = analogRead(analogPorts[i]);
      //delay(15);
    }
  }
}

void record(){
  int i, s;
  for(s = 0; s < numSensorSamples; s++){
     // make a string for assembling the data to log:
    String dataString = "";
    
  
    //dataString += String(trialTime);
    
    dataString += String(xCoordinate) + ", " + String(phi);
    // read three sensors and append to the string:
    for (i = 0; i < numPorts; i++) {
      dataString +=  + ", " + String(sensorValues[i][s]);
      
    }
    dataString += "\n";
    // open the file. note that only one file can be open at a time,
    // so you have to close this one before opening another.
    File dataFile = SD.open(datalogNames[s], FILE_WRITE);
  
    // if the file is available, write to it:
    if (dataFile) {
      dataFile.println(dataString);
      dataFile.close();
      // print to the serial port too:
      Serial.println(dataString);
    }
    // if the file isn't open, pop up an error:
    else {
      Serial.print("error opening ");Serial.println(datalogNames[s]);
    }
  }
}

void act(){
  driveDirect(-motorSpeed,motorSpeed);
  delay(actTime);
}

void transition(){
  driveDirect(motorSpeed, motorSpeed);
  delay(transitionTime);
}
/**********************************************************/
//This simply turns the the motor values into the correct 
// bytes and sends them to the iCreate for basic driving
void driveDirect(int rightValue, int leftValue){
  Serial3.write(145);
  Serial3.write(highByte(rightValue));
  Serial3.write(lowByte(rightValue));
  Serial3.write(highByte(leftValue));
  Serial3.write(lowByte(leftValue));
}

//This is somewhat complicated and I don't know exactly how it all works
// but it does so that's pretty good. It just reads the byte stream basically
// after asking for the info
//Originally sourced from http://web.ics.purdue.edu/~fwinkler/AD61600_S14/AD61600_Arduino_iRobot.pdf

/*Bumps and Wheel Drops Packet ID: 7 Data Bytes: 1, unsigned
The state of the bumper (0 = no bump, 1 = bump) and wheel drop sensors (0 = wheel raised, 1 = wheel
dropped) are sent as individual bits. */
bool checkBumpSensors() {
  int* buffer;
  bool ret = false;
  byte msb = 0;
  byte lsb = 0;
  Serial3.write(142);
  Serial3.write(7);

  if(Serial1.available() > 0){
      msb = Serial1.read();
      lsb = Serial1.read();
      *buffer = (msb << 7) | lsb;
      ret = true;
  }
  return ret;
}
/********************************************************/
//Just stops the robot and plays and happy tune to let you
// know the test is over
void endTest(int endLine){
  //while(bumpRight != 1 && bumpLeft != 2){
  if(endLine == 0){
    contExp = 0;
    while(true){
          
          driveDirect(0,0);

          contExp = digitalRead(contPin);
          Serial.print("contExp ? ");
          Serial.println(contExp);
          delay(50);
          //bumpRight = 1;
 //         if(bumpRight <= 700 || bumpLeft <= 700){
          if(contExp == 1){
           
           Serial3.write(140);
            //Number 0
            Serial3.write((byte)1);
            //4 Notes
            Serial3.write((byte)4);
            //C
            Serial3.write((byte)72);
            Serial3.write((byte)24);
            //C
            Serial3.write((byte)72);
            Serial3.write((byte)24);
            //G
            Serial3.write((byte)79);
            Serial3.write((byte)24);
            //G
            Serial3.write((byte)79);
            Serial3.write((byte)24);
            //play the song
            Serial3.write(141);
            Serial3.write((byte)1);
            delay(3000);//Give the experimenter 3 seconds to get out of the way.
             break;
          }
          else if(contExp == 0){
            Serial3.write(140);
            //Number 0
            Serial3.write((byte)1);
            //4 Notes
            Serial3.write((byte)4);
            //C
            Serial3.write((byte)72);
            Serial3.write((byte)24);
            //E
            Serial3.write((byte)76);
            Serial3.write((byte)24);
            //G
            Serial3.write((byte)79);
            Serial3.write((byte)24);
            //E
            Serial3.write((byte)76);
            Serial3.write((byte)24);
            //play the song
            Serial3.write(141);
            Serial3.write((byte)1);
          }
          
          
          
    }
  }
  else{//Stop this trial
    while(true){
        
        driveDirect(0,0);
        Serial3.write(140);
        //Number 0
        Serial3.write((byte)1);
        //4 Notes
        Serial3.write((byte)4);
        //C
        Serial3.write((byte)72);
        Serial3.write((byte)24);
        //C
        Serial3.write((byte)72);
        Serial3.write((byte)24);
        //G
        Serial3.write((byte)79);
        Serial3.write((byte)24);
        //G
        Serial3.write((byte)79);
        Serial3.write((byte)24);
        //play the song
        Serial3.write(141);
        Serial3.write((byte)1);
        
        checkBumpSensors();
        delay(1000);
        //bumpRight = 1;
        if(bumpRight != 0 || bumpLeft != 0){
          break;
        }
        
    }
  }
  //Give the system a chance to flush, and give the human
  //experiment runner time to clear out before continuing.
  delay(1000);
}

/**************************************************************/
//Limits speed to a range between -400 and 400 by clipping it.
int checkSpeed(int spd){
 if(spd > 400){
   spd = 400;
  }
 else if(spd < -400){
  spd = -400;
 }
 return spd;
}
  
    


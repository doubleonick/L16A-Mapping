# L16A-Mapping
All data and documentation associated with mapping the Landro arena with L16A.

## Physical robot notes.

Performed with Create 2 "C".  Performed by Nick L. and Ken L.
y = 18.5, 48.5, 78.5 run on 27 January, 2017 between 16:00 and 17:15 hrs

Performed with Create 2 "C".  Performed by Nick L. and Theresa L. 15 February, 2017
y = 108.5 starting at 14:25 hrs, ending at 14:55 hrs
y = 138.5 starting at 14:57 hrs, ending at 15:20 hrs
y = 168.5 starting at 15:22 hrs, restarting at 15:24 hrs, end at 15:49 hrs
y = 198.5 starting at 15:52 hrs... at x = 168.7, slight increase in light from window through felt... end at 16:18 hrs.
y = 228.5 starting at 16:20 hrs... at 16:44, Create 2 battery death.  x = 318.5... redo row after charge.

Performed with Create 2 "C".  Performed by Nick L. and Theresa L.  16 February, 2017
y = 228.5 starting at 14:38 hrs.  Room darker than at 16:00 previous day

The arena for these Landro experiments is 397.4 cm in the x direction by 247 cm in the y direction.
There is a single white LED lamp located at (198.7, 0).  The light diffuses across a semicircular
area within the rectangular arena.
A grid was marked using straight edges, markers and chalk snaps starting at (18.7, 18.5) and translating
in 30 cm increments in each direction to (378.7, 228.5).  These, and all of the intermediate coordinates
represent where the center of Landro was placed at each of the 104 positions visited.  At each of these
positions, Landro rotated clockwise 22.5 degrees at a time collecting data from its 16 sensors at each
orientation ranging from 0 degrees to 337.5 degrees.  An orientation of 0 degrees was taken to mean that
the center of Landro's front was facing in the positive direction of the y line it was about to traverse.
Thus, at 180 degrees, the Landro faced the x = 0 wall, and at 0 degrees, it faced the x = 397.4 wall.
Likewise, at 90 degrees, Landro faced the y = 0 wall, and at 240 degrees, it faced the y = 247 wall.
At each orientation, Landro took 10 samples from each sensor, and recorded all 10 samples, one sample
per each of 10 datalog text files named DATALOG0.TXT, through DATALOG9.TXT.

The DATALOG#.txt files were imported to an Excel spreadsheet called DATALOGS.TXT for each set of data.  A set includes each of the x coordinates for a given y, and each of the orientations for those x's.  Data sets were stored in separate "Y" folders.  Thus, each Y folder has a DATALOGS spreadsheet.  A MATLAB program called "data_processing.m" was created to parse through these DATALOGS.TXT files, and compile them in a more readable format.  For each Y dataset, the average of the 10 samples was calculated and stored.  For the first three Y datasets, one of the Landro sensors, IR8 was found to behave differently from the rest of the IRs.  It was thus replaced at each position and orientation by the average of the other 7 IR values corresponding to when those IRs were rotated into a given spot.  For example, for IR8 being in orientation 0, the average of when IRs 1 through 7 at orientation 0 was used for a given x location.  These calculations were performed on already averaged data (averaged across the 10 samples).

The program "UVM_Sim_Data_Gather_25Jan2017C.ino" is a C program written for the Arduino Mega 2560, which serves as the brains of L16A.  It spins the Landro in 22.5 degree intervals collecting and recording data as described above at each orientation.  It then translates the Landro as close to 30 cm as it can, and pauses operations to let a human fine tune the Landro's position.  When the human is satisfied that the Landro is in the location and starting orientation for the next round of data collection, s/he presses a button on Landro's breakout board and leaves the arena before Landro starts data collection 3 seconds later.  This is repeated until the last x coordinate of the current y has been surveyed, at which point Landro is paused and plays a tune signifying the end of the dataset.  The experimenter then collects the Landro, disconnects the Arduino from the iRobot Create 2 platform, shuts off the platform, removes the micro SD card from the breakout board, and files the DATALOG#.TXT files contained within to the correct Y folder.  This is repeated for all y coordinates.

A video of a sample of data collection can be seen here: https://www.youtube.com/watch?v=UD6OUbrjroY&feature=youtu.be

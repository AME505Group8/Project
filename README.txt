----------------------------------------------------------------------------------
Updates 4/27/20 - Bruce I. Rivera - GUI Designer and Chief Idiot
----------------------------------------------------------------------------------

Moved old GUI to the archive. Provided commit of the new GUI.

Should work with the new function created by Matt, but I am unable to test due to some issue with the tensorflow plugin.

Matt, Please pull this commit and test it. Let me know if there are any issues. You will need to install the PyQt5 plugin.

Type 'pip install PyQt5' into your Python environment's terminal

----------------------------------------------------------------------------------
Updates 4/26/20 - Matthew Rose
----------------------------------------------------------------------------------

In the GUI folder, created the functions needed to pull out 

****** engine_type is defined as the following list ['Piston', 'Turbojet', 'Turboprop', 'Turbofan', 'Turboshaft'] **********

prediction_name, aircraft_list = gui_predict_function(state, month, time_of_day, airport_id, engine_type, number_of_engines, phase_of_flight)

Inputs:
state is a string with definitions in text_names['STATE'] dictionary
month is a integer
time_of_day is a string with definitions in text_names['TIME_OF_DAY'] dictionary
airport_id is a string with definitions in text_names['AIRPORT_ID'] dictionary
number_of_engines is a string with definitions in text_names['AIRPORT_ID'] dictionary
phase_of_flight is a string with definition in text_names['AIRPORT_ID'] dictionary

Outputs: 
prediction_name - this is a string with the answer
aircraft_list - this is a list with the answer

A working example is the following

state = 'NY'
month = 1
time_of_day = 'Day'
airport_id = 'KLGA'
engine_type = 'Turbofan'
number_of_engines = '2'
phase_of_flight = 'Climb'

Returns prediction_name = 'Airplane'
aircraft_list = ['A-320', 'B-767-300', 'B-737-800', 'A-321', 'EMB-170']

These parameters are from Capt. Sully's flight and the top return is the A-320! (The airplane that landed in the Hudson)

A different example is the following

state = 'CA'
month = 9
time_of_day = 'Day'
airport_id = 'KVNY'
engine_type = 'Turboshaft'
number_of_engines = '1'
phase_of_flight = 'Departure'

Returns prediction_name = 'Helicopter'
aircraft_list = ['HUGHES 269A', 'ROBINSON R22', 'EC135', 'AEROS SA365', 'AEROS 350']

Updated Machine_Learning.py in the main folder, should not effect anyone else's code

----------------------------------------------------------------------------------
Updates 4/19/20 - Bruce I. Rivera - GUI Designer and Chief Idiot
----------------------------------------------------------------------------------

Added dashes to READ ME in order to improve readability.

Submitted initial commits for the GUI; files have been placed in subfolder in order to keep them out of the way.

Updated GUI flow diagram to reflect changes as of today.

To start GUI: Open and run 'GUI_Start.py'

GUI functionality as of today:

 - GUI screens have all been layed out and graphically designed
 - Buttons from each screen have been linked to each other screen
 - Quit button exits the program
 - No link between the GUI and other code exists at this time. We need to coordinate that.

Difficulties and Changes:

 - Gave up on the progress page which allowed for aborting a process in work.
    - This would have been useful but, after spending the majority of the day trying to get multithreading to play nice with PyQT5, I decided the juice was not worth the squeeze.


----------------------------------------------------------------------------------
Updates 4/25/20
----------------------------------------------------------------------------------

Project_Main.py, updated to now include Keras ANN

Machine_Learning.py, new file to handle all machine learning algorithms

In_7_Out_AC_CLASS.hd5, Keras saved ANN model

DataFrame_Loader.py, Minor changes to wording


----------------------------------------------------------------------------------
Updates 4/12/20
----------------------------------------------------------------------------------

Project_Main.py is now the wrapper file that holds all of the variables for Project_Main, DataFrame_Loader, and Query_Database

The 'BIRD_STRIKE.pkl','BIRD_STRIKE_NUM_ONLY.pkl','BIRD_STRIKE_DICTIONARY.pkl' files are on the Google Drive, that needs to be downloaded and placed in your directory that you plan on running Project_Main and DataFrame_Loader.

Project_Main.py should run straight from GitHub without any modification assuming that BIRD_STRIKE.pkl, BIRD_STRIKE_NUM_ONLY.pkl, BIRD_STRIKE_DICTIONARY.pkl are in the correct folder.

Project_Main.py can run Query_Database but that is not necessary at this time.

DataFrame_Loader.py holds all of the functions 


----------------------------------------------------------------------------------
Updates 4/4/20
----------------------------------------------------------------------------------

Project_Main.py is now the wrapper file that holds all of the variables for Project_Main, DataFrame_Loader, and Query_Database

The 'BIRD_STRIKE.pkl' file is on the Google Drive, that needs to be downloaded and placed in your directory that you plan on running Project_Main and DataFrame_Loader.

Project_Main.py should run straight from GitHub without any modification assuming that BIRD_STRIKE.pkl is in the correct folder.

For the report, Project_Main.py will also be able to run Query_Database but that is not necessary at this time.

The DataFrame_Loader.py is now a function file, it holds the function dataframe_loader and handle_non_numerical_data
The second function is from the TA that was modified slightly in order to make it work for this data set 
		
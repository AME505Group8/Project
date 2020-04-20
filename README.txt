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
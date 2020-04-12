Updates 4/4/20

Project_Main.py is now the wrapper file that holds all of the variables for Project_Main, DataFrame_Loader, and Query_Database

The 'BIRD_STRIKE.pkl' file is on the Google Drive, that needs to be downloaded and placed in your directory that you plan on running Project_Main and DataFrame_Loader.

Project_Main.py should run straight from GitHub without any modification assuming that BIRD_STRIKE.pkl is in the correct folder.

For the report, Project_Main.py will also be able to run Query_Database but that is not necessary at this time.

The DataFrame_Loader.py is now a function file, it holds the function dataframe_loader and handle_non_numerical_data
The second function is from the TA that was modified slightly in order to make it work for this data set 

########################################################################################################################################################################

OBSOLETE FILE - Query_Database.py, only use this if you need to recreate the database from scratch

1. Pull the Query_Database.py from the repository

2. Create a folder called Database in the same folder as where your Query_Database.py file is located

3. Download the wildlife.accdb file from Google Drive and place it in the Database folder

4. Try to run the file. If your script prints [] for myDataSources on line 36, then you need to install the ODBC driver for windows. (https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)
	a) If ODBC is installed, you should be able to run ODBC Data Source Administrator
	b) Under the name column, MS Access Database should exist
		i) If not, restart your computer
	c) Under the driver column, Microsoft Access Driver (*.mdb, *.accdb) should be listed

5. Try to run the file. If your script still doesn't work, restart your IDE (ie. PyCharm)

All else fails, contact me and I will help you troubleshoot

Upon successful run, you should see the following statements

<LOCATION_OF_FILE>/Project/Database/wildlife.accdb
{..., 'MS Access Database': 'Microsoft Access Driver (*.mdb, *.accdb)'}
(613189, datetime.datetime(1993, 1, 24, 0, 0), 1, 1993, None, 'Day', 'PHLI', '(PHLI) LIHUE ARPT', 'HI', 'AWP ', None, '21', None, '1AAH', '(1AAH) ALOHA AIRLINES', 'N725AL', 'NULL', 'B-737-200', '148', '13', '34', '10', 'A  ', '4', 'D', '2', '1', '1', 'NULL', 'NULL', 'Approach', 100, 140, 'No Cloud', 'None', None, None, None, None, None, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, None, 'None', None, 'O2212', 'Zebra dove', 'NO DAMAGE OR INJURIES.', False, True, False, 'No', '2-10', '1', 'Small', 'N', None, None, None, 'SOURCE = XXXX-X & ARPT REPT  (X/X/XX UPDATED ID) /Legacy Record=XXXXXX/', 'REDACTED', 'REDACTED', 'Multiple', 'Pilot', datetime.datetime(2012, 7, 2, 0, 0), False)
		
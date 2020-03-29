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
		
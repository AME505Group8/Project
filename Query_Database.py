# Created by Matthew Rose
# AME 505 Project
#
# This file is intended to query the birdstrike
# It will take a while to load the first time, but the second run happens much faster

# This library is used to query Access database
import pyodbc
# This library is used to find the path of your database
import os.path
# This library is used to go from cursor to DataFrame
from pandas import DataFrame

# ## Variables that may need to be changed #############################################################################
# This is the name of the database that needs to be accessed by python
# The database is .accdb
driver = '{Microsoft Access Driver (*.mdb, *.accdb))}'

# Location of your birdstrike database
filepath = os.path.dirname(__file__) + "/Database/wildlife.accdb"
print(filepath)

# The table name is name of the table inside the Access database
table_name = 'STRIKE_REPORTS'

# The query is actually SQL code that is being run by python
# In this query I am creating a string that is asking for
# everything in the database with the database name STRIKE_REPORTS
query = "SELECT * FROM {}".format(table_name)

# This is needed to initialize the dictionary for the dataframe
cursor_dict = []
# ######################################################################################################################

# ## Functions that are being run ######################################################################################

# Access the library and call this function dataSources
# From GitHub Returns a dictionary mapping available DSNs to their descriptions.
# On Windows, these will be the ones defined in the ODBC Data Source Administrator.
myDataSources = pyodbc.dataSources()
print(myDataSources)

# Passing the type of database that we want to access (This may need a driver if your dataSources dictionary is empty)
access_driver = myDataSources['MS Access Database']

# This is using the library and calling the connect function to access the database
# The two imports are the driver (type of file) of the database and where the database is located
connection = pyodbc.connect(driver=access_driver, dbq=filepath)

# Cursor is an object that is created once the connection is successful
# From documentation on SQLite3 A Cursor instance has attributes and methods
cursor = connection.cursor()

# This is a method for the cursor object, you can execute a query which injects the SQL code using python
cursor.execute(query)

# This pulls off the names of from the header
columns = [column[0] for column in cursor.description]

# Show the output of the columns to make sure it looks correct
print(columns)

# Message to user because the conversion is slow
print('Starting Conversion')

# This code turns the columns into the dictionary name, row is the data
for row in cursor.fetchall():
    cursor_dict.append(dict(zip(columns, row)))

# Message to user because this is a slow process
print('Setting dataframe')

# Load the cursor object as a DataFrame object
df = DataFrame(cursor_dict)

# Check that the DataFrame loads correctly
print(df)
# Some analysis of the DataFrame
# # print("dataframe['INDEX_NR'].describe: "+'\n', df['INDEX_NR'].describe())
# print("dataframe['INCIDENT_MONTH'].describe: "+'\n', df['INCIDENT_MONTH'].describe())
# print("dataframe['TIME'].describe: "+'\n', df['TIME'].describe())
# print("dataframe['DISTANCE'].describe: "+'\n', df['DISTANCE'].describe())
# print("dataframe['AMA'].describe: "+'\n', df['AMA'].describe())
# print("dataframe['AMO'].describe: "+'\n', df['AMO'].describe())
# print("dataframe['EMA'].describe: "+'\n', df['EMA'].describe())
# print("dataframe['EMO'].describe: "+'\n', df['EMO'].describe())
# print("dataframe['AC_MASS'].describe: "+'\n', df['AC_MASS'].describe())
# print("dataframe['NUM_ENGS'].describe: "+'\n', df['NUM_ENGS'].describe())
# print("dataframe['ENG_1_POS'].describe: "+'\n', df['ENG_1_POS'].describe())
# print("dataframe['ENG_2_POS'].describe: "+'\n', df['ENG_2_POS'].describe())
# print("dataframe['ENG_3_POS'].describe: "+'\n', df['ENG_3_POS'].describe())
# print("dataframe['ENG_4_POS'].describe: "+'\n', df['ENG_4_POS'].describe())
# print("dataframe['HEIGHT'].describe: "+'\n', df['HEIGHT'].describe())
# print("dataframe['SPEED'].describe: "+'\n', df['SPEED'].describe())
# print("dataframe['AOS'].describe: "+'\n', df['AOS'].describe())
# print("dataframe['COST_REPAIRS'].describe: "+'\n', df['COST_REPAIRS'].describe())
# print("dataframe['OTHER_COST'].describe: "+'\n', df['OTHER_COST'].describe())
# print("dataframe['COST_REPAIRS_INFL_ADJ'].describe: "+'\n', df['COST_REPAIRS_INFL_ADJ'].describe())
# print("dataframe['COST_OTHER_INFL_ADJ'].describe: "+'\n', df['COST_OTHER_INFL_ADJ'].describe())
# print("dataframe['NR_INJURIES'].describe: "+'\n', df['NR_FATALITIES'].describe())

# Save the dataframe as a pickle file (compresses the database to load much faster)
df.to_pickle("BIRD_STRIKE.pkl")
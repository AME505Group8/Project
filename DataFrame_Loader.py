# Created by Matthew Rose
# Function handle_non_numerical_data copied from Zijian (Jamey) Zhang
# AME 505 Project
#
# This file is intended provide all the functionality to load the data into a dataframe
# It should load quickly

# This library is used to query Access database
import pyodbc
# This library is used to find the path of your database
import os.path
# Library for dataframe
import pandas
from pandas import DataFrame
import numpy
import pickle


def query_database(filepath, query, cursor_dict):

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

    # Save the dataframe as a pickle file (compresses the database to load much faster)
    df.to_pickle("BIRD_STRIKE.pkl")


def dataframe_loader(filename):
    # This function is a quick way to load the code from a .pkl file

    # Message for user
    print('Loading data')

    # Function to load the saved dataframe (a compressed version of the database)
    df = pandas.read_pickle(filename)
    # Check that the data loaded properly
    print(df)
    return df


def save_dictionary(obj, name):
    print('Saving the dictionary')
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    print('Dictionary saved')


def load_dictionary(name):
    print('Loading dictionary')
    with open(name, 'rb') as f:
        return pickle.load(f)


def dataframe_saver(dataframe, filename):
    # This is a quick way to save off a new file so that changing the data doesn't permanently change the original data

    # Message for user
    print('Saving the data')
    print(dataframe)

    # Save the dataframe as a pickle file (compresses the database to load much faster)
    dataframe.to_pickle(filename)

    # Message to user
    print('Data saved')


def unique(sequence):
    # Code from Martin Broadhurst (http://www.martinbroadhurst.com/) Date accessed 4/5/2020
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def handle_non_numerical_data(df):
    # This function turns all the non numerical data into numbers for the machine learning code to use

    # This prints a message to the user
    print('Converting Data')

    # Columns grab the header text from the dataframe
    columns = df.columns.values

    # Empty dictionary to initialize variable
    store_dict = {}

    # This for loop goes through each column, one by one
    for column in columns:
        # Empty cells to be filled by the for loop, also resets the cells to empty for each column
        text_digit_vals = {}

        # Function to be called when mapping list to column of dataframe
        def convert_to_int(val):
            # Returns the position in the list text_digit_vals
            return text_digit_vals[val]

        # This if statement checks to see if the column is full of numbers or is a timestamp
        if df[column].dtype != numpy.int64 and df[column].dtype != numpy.float64 and not (
                pandas.core.dtypes.common.is_datetime_or_timedelta_dtype(df[column])):
            # This changes the column to a list to use in a for loop
            column_contents = df[column].values.tolist()
            # This sets the column to a list called unique_elements
            unique_elements = unique(column_contents)
            # This resets the counter x to 0
            x = 0
            # This for loop is used to iterate through the list of unique elements
            for unique1 in unique_elements:
                # This if statement checks to see if the value for unique is in the list text_digit_vals
                if unique1 not in text_digit_vals:
                    # This sets the position in the list text_digit_vals to a new value per the counter
                    text_digit_vals[unique1] = x
                    # This adds another value to the counter
                    x += 1

            # This maps the list convert_to_int to the position in the column and writes over the current column
            df[column] = list(map(convert_to_int, df[column]))
            
        # This else statement was added because datastamps need special treatment in the function and will not work
        # with the strategy above
        elif pandas.core.dtypes.common.is_datetime_or_timedelta_dtype(df[column]):
            # This creates a new list each time this elif is true
            timestamp = list()
            # This for loop, repeat the method used above just using range instead of creating a list
            for y in range(len(df[column])):
                # This creates a list for each time in the dataframe and turns it into a number from DD/MM/YYYY HH:MM:SS
                timestamp.append(df[column][y].timestamp())
            # places the list into the column since each timestamp needs to be recorded
            df[column] = timestamp

        store_dict[column] = text_digit_vals
    print(df)
    return df, store_dict

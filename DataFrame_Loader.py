# Created by Matthew Rose
# Function handle_non_numerical_data copied from Zijian (Jamey) Zhang
# AME 505 Project
#
# This file is intended to load the existing dataframe called BIRD_STRIKE.pkl
# It should load quickly

# Library for dataframe
import pandas
import numpy


def dataframe_loader(filename):
    # This function is a quick way to load the code from a .pkl file

    # Message for user
    print('Loading data')

    # Function to load the saved dataframe (a compressed version of the database)
    df = pandas.read_pickle(filename)
    # Check that the data loaded properly
    print(df)
    return df

def dataframe_saver(dataframe, filename):
    # This is a quick way to save off a new file so that changing the data doesn't permanently change the original data

    # Message for user
    print('Saving the data')
    print(dataframe)

    # Save the dataframe as a pickle file (compresses the database to load much faster)
    dataframe.to_pickle(filename)

    # Message to user
    print('Data saved!')

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
    print(df)
    return df

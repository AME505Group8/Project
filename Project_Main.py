# Created by Matthew Rose
# AME 505 Project
#
# This is the main file to call multiple functions and store variable names

import os.path
from DataFrame_Loader import dataframe_loader, handle_non_numerical_data, dataframe_saver, query_database, \
    save_dictionary, load_dictionary

# ## Variables that may need to be changed #############################################################################

# This only needs to be set to true if the dataframe doesn't exist and needs to be created. This should always be False
# unless the BIRD_STRIKE.pkl file is corrupted on the Google Drive
fresh_load = False

# Load variables only for fresh_load
if fresh_load:
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

# This is only if you need to revert back to the dataframe before it was preconditioned
original_dataframe = False

# Load variables only for original_dataframe
if original_dataframe:
    # The filename where BIRD_STRIKE dataframe is saved. This file has not been preconditioned. If you need the
    # preconditoned file (like running machine learning), recommend using a different file
    original_data_filename = "BIRD_STRIKE.pkl"

    # This is if you want to convert all the non number part of the database into numbers only
    condition_data = False

    # This is if you want to save off the data after it is preconditioned. WARNING, it will overwrite any data saved as
    # conditioned_data_filename
    save_conditioned = False

# The filename where the preconditioned data is saved after the preconditioning is complete. Recommend using for
# machine learning
conditioned_data_filename = "BIRD_STRIKE_NUM_ONLY.pkl"

# The filename where BIRD_STRIKE dictionary is saved. This file is for conditioned data
dictionary_filename = "BIRD_STRIKE_DICTIONARY.pkl"

# This is if you want to only load the dataframe after it has been preconditioned
conditioned_dataframe = True

# ######################################################################################################################

# ## Function Calls ####################################################################################################

# This function is to load the database for the first time
if fresh_load:
    query_database(filepath, query, cursor_dict)

# This is a function call in order to pull the original data
elif original_dataframe:
    df = dataframe_loader(original_data_filename)

    # Correct output looks like this ###########################
    #         INDEX_NR INCIDENT_DATE  ...    LUPDATE  TRANSFER #
    # 0         613189    1993-01-24  ... 2012-07-02     False #
    # 1         613814    1992-05-01  ... 2012-06-11     False #
    # 2         614017    1991-08-16  ... 2016-04-08     False #
    # 3         614185    1991-12-18  ... 2012-06-11     False #
    # 4         614652    1992-02-07  ... 2015-07-31     False #
    # ...          ...           ...  ...        ...       ... #
    # 233667    934325    2019-08-20  ... 2020-02-07     False #
    # 233668    922514    2019-08-08  ... 2020-01-13     False #
    # 233669    909147    2019-06-20  ... 2019-12-04     False #
    # 233670    921636    2019-08-06  ... 2020-01-02     False #
    # 233671    922174    2019-08-07  ... 2020-01-08     False #
    # ##########################################################

    # This replaces blank space with and empty string (helps with machine learning)
    df = df.fillna('')
    df = df.sort_values(by=['INCIDENT_DATE'])
    print(df)

    if condition_data:
        # This converts the dataframe into a numbers only format
        df_numbers, text_values = handle_non_numerical_data(df)

        # Correct output looks like this #######################################################
        #         INDEX_NR  INCIDENT_DATE  INCIDENT_MONTH  ...  PERSON       LUPDATE  TRANSFER #
        # 0         613189   7.278336e+08               1  ...       5  1.341187e+09         0 #
        # 1         613814   7.046784e+08               5  ...       2  1.339373e+09         0 #
        # 2         614017   6.823008e+08               8  ...       4  1.460074e+09         0 #
        # 3         614185   6.930144e+08              12  ...       2  1.339373e+09         0 #
        # 4         614652   6.974208e+08               2  ...       4  1.438301e+09         0 #
        # ...          ...            ...             ...  ...     ...           ...       ... #
        # 233667    934325   1.566259e+09               8  ...       1  1.581034e+09         0 #
        # 233668    922514   1.565222e+09               8  ...       1  1.578874e+09         0 #
        # 233669    909147   1.560989e+09               6  ...       1  1.575418e+09         0 #
        # 233670    921636   1.565050e+09               8  ...       2  1.577923e+09         0 #
        # 233671    922174   1.565136e+09               8  ...       5  1.578442e+09         0 #
        # ######################################################################################

        print(text_values['STATE'])

        # ################################################################################################################
        # {'HI': 0, 'BC': 1, 'CA': 2, 'NV': 3, 'PI': 4, '': 5, 'ON': 6, 'PA': 7, 'LA': 8, 'NY': 9, 'MD': 10, 'SC': 11,   #
        #  'TN': 12, 'OH': 13, 'NC': 14, 'IL': 15, 'TX': 16, 'WV': 17, 'GA': 18, 'NJ': 19, 'IA': 20, 'OK': 21, 'WI': 22, #
        #  'ME': 23, 'IN': 24, 'FL': 25, 'MS': 26, 'VA': 27, 'CT': 28, 'AL': 29, 'KY': 30, 'DC': 31, 'CO': 32, 'MI': 33, #
        #  'AR': 34, 'NH': 35, 'KS': 36, 'MO': 37, 'MN': 38, 'NE': 39, 'MA': 40, 'AB': 41, 'NM': 42, 'AZ': 43, 'UT': 44, #
        #  'RI': 45, 'ID': 46, 'OR': 47, 'WA': 48, 'FN': 49, 'PR': 50, 'VT': 51, 'AK': 52, 'QC': 53, 'MT': 54, 'ND': 55, #
        #  'WY': 56, 'SD': 57, 'VI': 58, 'DE': 59, 'NL': 60, 'MB': 61, 'NS': 62, 'SK': 63}                               #
        # ################################################################################################################

        # This lets you save the df_numbers dataframe to a file, to load the next time skipping the
        # processing part of the script
        if save_conditioned:
            dataframe_saver(df_numbers, conditioned_data_filename)
            # This lets you save the dictionary that goes along with the df_numbers dataframe
            save_dictionary(text_values, dictionary_filename)

# This lets you load only the dataframe that has been conditioned without having to process the
# data on each run
elif conditioned_dataframe:
    # This loads the saved conditioned file
    df = dataframe_loader(conditioned_data_filename)
    # This loads the dictionary file that goes with the conditioned data
    text_names = load_dictionary(dictionary_filename)

    # Correct output looks like this #######################################################
    #         INDEX_NR  INCIDENT_DATE  INCIDENT_MONTH  ...  PERSON       LUPDATE  TRANSFER #
    # 0         613189   7.278336e+08               1  ...       5  1.341187e+09         0 #
    # 1         613814   7.046784e+08               5  ...       2  1.339373e+09         0 #
    # 2         614017   6.823008e+08               8  ...       4  1.460074e+09         0 #
    # 3         614185   6.930144e+08              12  ...       2  1.339373e+09         0 #
    # 4         614652   6.974208e+08               2  ...       4  1.438301e+09         0 #
    # ...          ...            ...             ...  ...     ...           ...       ... #
    # 233667    934325   1.566259e+09               8  ...       1  1.581034e+09         0 #
    # 233668    922514   1.565222e+09               8  ...       1  1.578874e+09         0 #
    # 233669    909147   1.560989e+09               6  ...       1  1.575418e+09         0 #
    # 233670    921636   1.565050e+09               8  ...       2  1.577923e+09         0 #
    # 233671    922174   1.565136e+09               8  ...       5  1.578442e+09         0 #
    # ######################################################################################

    print(df.columns.values)
    print(text_names['STATE'])

    # Correct output looks like this #################################################################################
    # {'HI': 0, 'BC': 1, 'CA': 2, 'NV': 3, 'PI': 4, '': 5, 'ON': 6, 'PA': 7, 'LA': 8, 'NY': 9, 'MD': 10, 'SC': 11,   #
    #  'TN': 12, 'OH': 13, 'NC': 14, 'IL': 15, 'TX': 16, 'WV': 17, 'GA': 18, 'NJ': 19, 'IA': 20, 'OK': 21, 'WI': 22, #
    #  'ME': 23, 'IN': 24, 'FL': 25, 'MS': 26, 'VA': 27, 'CT': 28, 'AL': 29, 'KY': 30, 'DC': 31, 'CO': 32, 'MI': 33, #
    #  'AR': 34, 'NH': 35, 'KS': 36, 'MO': 37, 'MN': 38, 'NE': 39, 'MA': 40, 'AB': 41, 'NM': 42, 'AZ': 43, 'UT': 44, #
    #  'RI': 45, 'ID': 46, 'OR': 47, 'WA': 48, 'FN': 49, 'PR': 50, 'VT': 51, 'AK': 52, 'QC': 53, 'MT': 54, 'ND': 55, #
    #  'WY': 56, 'SD': 57, 'VI': 58, 'DE': 59, 'NL': 60, 'MB': 61, 'NS': 62, 'SK': 63}                               #
    # ################################################################################################################

    print(text_names['TIME_OF_DAY'])

    # Correct output looks like this ######################
    # {'Day': 0, 'Dusk': 1, 'Night': 2, 'Dawn': 3, '': 4} #
    # #####################################################

else:
    print('Check your loading variables, both are currently False')
# Created by Matthew Rose
# AME 505 Project
#
# This is the main file to call multiple functions and store variable names

from DataFrame_Loader import dataframe_loader, handle_non_numerical_data

# ## Variables that may need to be changed #############################################################################

# This only needs to be set to true if the dataframe doesn't exist and needs to be created. This should always be False
# unless the BIRD_STRIKE.pkl file is corrupted on the Google Drive
fresh_load = False

# The filename where BIRD_STRIKE dataframe is saved. This file has not been preconditioned. If you need the
# preconditoned file (like running machine learning), recommend using a different file
raw_data_filename = "BIRD_STRIKE.pkl"

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

# ######################################################################################################################

# ## Function Calls ####################################################################################################

# This is a function call in order to pull the raw data
df = dataframe_loader(raw_data_filename)

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

# This converts the dataframe into a numbers only format
df_numbers = handle_non_numerical_data(df)

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
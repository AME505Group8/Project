# Created by Matthew Rose
# AME 505 Project
#
# This file is intended to load the existing dataframe called BIRD_STRIKE.pkl
# It should load quickly

# Library for dataframe
import pandas

# Message for user
print('Loading data')

# Function to load the saved dataframe (a compressed version of the database)
df = pandas.read_pickle("BIRD_STRIKE.pkl")

# Check that the data loaded properly
print(df)

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
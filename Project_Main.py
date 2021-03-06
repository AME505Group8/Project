# Created by Matthew Rose
# AME 505 Project
#
# This is the main file to call multiple functions and store variable names

import os.path
import DataFrame_Loader as df_loader
import Machine_Learning as ml
from tabulate import tabulate

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
original_dataframe = True

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
conditioned_dataframe = False

train_net = False

load_net = False

# This is the list to input into the keras neural network
input_list = ['STATE', 'INCIDENT_MONTH', 'TIME_OF_DAY', 'AIRPORT_ID', 'TYPE_ENG', 'NUM_ENGS', 'PHASE_OF_FLIGHT']

# This is the output of the keras neural network
output_name = 'AC_CLASS'

# Input Class     Keras_Input(State,Month,Time,Airport,Engine,Num Engs,Phase of Flight)
input_struct = ml.Keras_Input('CA', 11, 'Night', 'KVNY', 'F', '1', 'Approach', input_list, output_name)
# input_struct = ml.Keras_Input(input_list)

input_struct.print_self()

# This is the sample size for the balanced training data
sample_size = 60000

if train_net:
    # This is how many times the training should repeat
    number_of_epochs = 30

    # Decide whether or not the model should be saved
    save_model = False

    # Name to save the model - THIS WILL OVERWRITE MODELS WITH THE SAME NAME
    save_model_name = 'In_Out_Model'

if load_net:
    load_model_name = 'In_7_Out_AC_CLASS'

    evaluate_model = True

ac_class_dict = {'NULL': 'Empty', 'A  ': 'Airplane', 'B  ': 'Helicopter', 'J  ': 'Ultralight',
                 'A/B': 'Airplane or Helicopter', 'C  ': 'Glider', '': 'Empty'}

# ######################################################################################################################

# ## Function Calls ####################################################################################################

# This function is to load the database for the first time
if fresh_load:
    df_loader.query_database(filepath, query, cursor_dict)

# This is a function call in order to pull the original data
elif original_dataframe:
    df = df_loader.dataframe_loader(original_data_filename)

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
    print(tabulate(df.head(), headers='keys', tablefmt='psql', showindex=False))

    if condition_data:
        # This converts the dataframe into a numbers only format
        df_numbers, text_values = df_loader.handle_non_numerical_data(df)

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
            df_loader.dataframe_saver(df_numbers, conditioned_data_filename)
            # This lets you save the dictionary that goes along with the df_numbers dataframe
            df_loader.save_dictionary(text_values, dictionary_filename)

# This lets you load only the dataframe that has been conditioned without having to process the
# data on each run
elif conditioned_dataframe:
    # This loads the saved conditioned file
    df = df_loader.dataframe_loader(conditioned_data_filename)
    # This loads the dictionary file that goes with the conditioned data
    text_names = df_loader.load_dictionary(dictionary_filename)

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
    print(text_names['STATE'].keys())
    print(text_names['TIME_OF_DAY'].keys())
    print(text_names['AIRPORT_ID'].keys())
    print(text_names['TYPE_ENG'].keys())
    print(text_names['NUM_ENGS'].keys())
    print(text_names['PHASE_OF_FLIGHT'].keys())
    print(df['INCIDENT_MONTH'].unique())

    # Correct output looks like this #################################################################################
    # {'OH': 0, 'IL': 1, '': 2, 'TX': 3, 'AL': 4, 'MI': 5, 'VA': 6, 'WV': 7, 'PA': 8, 'CO': 9, 'MO': 10, 'NC': 11,   #
    #  'SC': 12, 'CA': 13, 'NJ': 14, 'TN': 15, 'AR': 16, 'NM': 17, 'WI': 18, 'NY': 19, 'IN': 20, 'AK': 21, 'CT': 22, #
    #  'NH': 23, 'FL': 24, 'WY': 25, 'AZ': 26, 'OR': 27, 'HI': 28, 'KY': 29, 'LA': 30, 'MN': 31, 'MS': 32, 'DC': 33, #
    #  'GA': 34, 'KS': 35, 'MD': 36, 'OK': 37, 'FN': 38, 'WA': 39, 'SD': 40, 'MA': 41, 'MT': 42, 'ME': 43, 'NE': 44, #
    #  'AB': 45, 'UT': 46, 'VT': 47, 'NV': 48, 'ON': 49, 'ID': 50, 'IA': 51, 'PR': 52, 'RI': 53, 'QC': 54, 'VI': 55, #
    #  'ND': 56, 'PI': 57, 'DE': 58, 'BC': 59, 'MB': 60, 'SK': 61, 'NL': 62, 'NS': 63}                               #
    # ################################################################################################################

    print(text_names['TIME_OF_DAY'])

    # Correct output looks like this ######################
    # {'Night': 0, '': 1, 'Dusk': 2, 'Day': 3, 'Dawn': 4} #
    # #####################################################

    check = text_names['TIME_OF_DAY']

    for columns in input_list:
        print(text_names[columns])

    predict_input, predict_in_list = input_struct.find_dict_index(text_names)
    print(predict_input[0].shape)

    X, y, X1, y1, X_train_df, X_test_df, y_train_df, y_test_df, size_of_output = ml.Keras_Training_Data(df, input_list,
                                                                                                     output_name,
                                                                                                     text_names,
                                                                                                     sample_size)

    print('\nPrediction Unbalanced Input: ', X1[0])
    print('\nPrediction Unbalanced Output: ', y1)

    if train_net:
        ml.Keras_NN(X_train_df, X_test_df, y_test_df, y_train_df, X1, y1, input_list, output_name,
                 number_of_epochs, save_model, save_model_name, size_of_output)
    elif load_net:
        prediction = input_struct.predict_KNN(load_model_name, predict_input)

        prediction_string = input_struct.find_dict_string(text_names)

        prediction_name = ac_class_dict[prediction_string[0]]
        print(prediction_name)

        sorted_df = df[df[output_name] == prediction[0]]
        sorted_df = sorted_df[sorted_df[input_list[0]] == predict_in_list[0]]
        sorted_df = sorted_df[sorted_df[input_list[1]] == input_struct.month]
        sorted_df = sorted_df[sorted_df[input_list[2]] == predict_in_list[2]]
        sorted_count = sorted_df.groupby('AIRCRAFT').size().reset_index(name='count').sort_values(['count'],
                                                                                                  ascending=False)
        sorted_index = sorted_count['AIRCRAFT'].tolist()
        print(sorted_count)
        sorted_index = sorted_index[:5]
        print(sorted_index)
        ac_list = []
        for ac_idx in sorted_index:
            ac_name = [k for k, v in text_names['AIRCRAFT'].items() if v == ac_idx]
            ac_str = ''.join(ac_name)
            ac_list.append(ac_str)

        print(text_names['AIRCRAFT'])
        print(ac_list)

        print(text_names['TYPE_ENG'])


        # sorted_df = sorted_df[sorted_df[input_list[3]] == predict_in_list[3]]
        # sorted_df = sorted_df[sorted_df[input_list[4]] == predict_in_list[4]]
        # sorted_df = sorted_df[sorted_df[input_list[5]] == predict_in_list[5]]
        # sorted_df = sorted_df[sorted_df[input_list[6]] == predict_in_list[6]]
        # keras_model = ml.Load_Keras_NN(load_model_name, X1, y1)

        # if evaluate_model:
        #     ml.Evaluate_Keras_NN(keras_model, X_test_df, y_test_df)

else:
    print('Check your loading variables, both are currently False')
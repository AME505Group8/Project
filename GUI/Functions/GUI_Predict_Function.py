# Created by Matthew Rose
# AME 505 Project
#
# This is the main GUI Prediction function to call multiple functions and store variable names

import DataFrame_Loader as df_loader
import Machine_Learning as ml


def gui_predict_function(state, month, time_of_day, airport_id, engine_type, number_of_engines,
                         phase_of_flight):
    # ## Initialization Variables #####################################################################################
    # The filename where the preconditioned data is saved after the preconditioning is complete. Recommend using for
    # machine learning
    conditioned_data_filename = "BIRD_STRIKE_NUM_ONLY.pkl"

    # The filename where BIRD_STRIKE dictionary is saved. This file is for conditioned data
    dictionary_filename = "BIRD_STRIKE_DICTIONARY.pkl"


    # This is the list to input into the keras neural network
    input_list = ['STATE', 'INCIDENT_MONTH', 'TIME_OF_DAY', 'AIRPORT_ID', 'TYPE_ENG', 'NUM_ENGS', 'PHASE_OF_FLIGHT']

    # This is the output of the keras neural network
    output_name = 'AC_CLASS'

    # This is a dictionary to make the drop down list look nicer in the GUI
    engine_type_dict = {'Piston': 'A', 'Turbojet': 'B', 'Turboprop': 'C', 'Turbofan': 'D', 'Turboshaft': 'F'}

    # Saved Keras Model with Training Performed Offline
    load_model_name = 'In_7_Out_AC_CLASS'

    # Dictionary defined by
    ac_class_dict = {'NULL': 'Empty', 'A  ': 'Airplane', 'B  ': 'Helicopter', 'J  ': 'Ultralight',
                     'A/B': 'Airplane or Helicopter', 'C  ': 'Glider', '': 'Empty'}

    # The expectation is to get only one answer from the prediction function
    number_of_predictions = 0

    # This defines the number of aircraft that are selected to show to end user
    rank_index = 5

    # This is the name of the column to select to show to user
    filter_name = 'AIRCRAFT'

    # #################################################################################################################

    # ## Function Calls ###############################################################################################
    # This lets you load only the dataframe that has been conditioned without having to process the
    # data on each run

    engine_type_letter = engine_type_dict[engine_type]

    # Input Class     Keras_Input(State,Month,Time,Airport,Engine,Num Engs,Phase of Flight)
    input_struct = ml.Keras_Input(state, month, time_of_day, airport_id, engine_type_letter, number_of_engines,
                                  phase_of_flight, input_list, output_name)

    # This loads the saved conditioned file
    df = df_loader.dataframe_loader(conditioned_data_filename)

    # This loads the dictionary file that goes with the conditioned data
    text_names = df_loader.load_dictionary(dictionary_filename)

    # This function finds the dictionary and returns it's index in a list
    predict_input, predict_in_list = input_struct.find_dict_index(text_names)

    # This calls the function predict_KNN in the input struct class
    # This predicts the output index with the offline Keras saved model
    prediction = input_struct.predict_KNN(load_model_name, predict_input)

    # This calls the function find_dict_string in the input struct class
    # This finds the string from the dictionary for the prediction index
    prediction_string = input_struct.find_dict_string(text_names)

    # This pulls the aircraft class to tell the user the name of the prediction string
    prediction_name = ac_class_dict[prediction_string[number_of_predictions]]

    # This lists the top five aircraft in the aircraft class
    aircraft_list = ml.top_five_list(df, output_name, prediction[number_of_predictions], predict_in_list,
                                     input_list, input_struct.month, rank_index, text_names, filter_name)

    return prediction_name, aircraft_list

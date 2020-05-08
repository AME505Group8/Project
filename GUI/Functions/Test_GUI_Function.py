# Created by Matthew Rose
# AME 505 Project
#
# This is to test GUI Prediction function

import GUI_Predict_Function

state = 'LA'
month = 1
time_of_day = 'Day'
airport_id = '7LS3'
engine_type = 'Turboshaft'
number_of_engines = '2'
phase_of_flight = 'En Route'

prediction_name, aircraft_list = GUI_Predict_Function.gui_predict_function(state, month, time_of_day, airport_id,
                                                                           engine_type, number_of_engines,
                                                                           phase_of_flight)

print('The predicted Aircraft Class is: ', prediction_name)

print('The top 5 aircraft in this class are: ', aircraft_list)
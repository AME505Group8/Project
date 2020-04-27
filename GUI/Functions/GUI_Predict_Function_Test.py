def gui_predict_function(state, month, time_of_day, airport_id, engine_type, number_of_engines, phase_of_flight):

    prediction_name = 'Test Successful'

    aircraft_list = [state, time_of_day, airport_id, engine_type, number_of_engines, phase_of_flight]

    return prediction_name, aircraft_list
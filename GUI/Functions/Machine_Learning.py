# Created by Matthew Rose
# AME 505 Project
#
# This file is intended provide all the functionality to perform the machine learning
# It should load quickly

from sklearn.model_selection import train_test_split
import numpy
from keras.layers import Dense
import matplotlib.pyplot as plt
import keras.regularizers
from keras.models import load_model
from pandas import DataFrame


# ## Class Definition #################################################################################################

class Keras_Input:
    def __init__(self, state, month, time_of_day, airport_id, type_eng, num_engs, phase_of_flight, input_list,
                 output_list):
        self.state = state
        self.month = month
        self.time = time_of_day
        self.airport = airport_id
        self.engine = type_eng
        self.num_engs = num_engs
        self.phase_flight = phase_of_flight
        self.input_list = input_list
        self.output_list = output_list
        self.output_name = []
        self.dict_keys_list = []
        self.input_index_list = []
        self.predicts_array = []

    def print_self(self):
        print('\nInput State:', self.state)
        print('Input Month:', self.month)
        print('Input Time:', self.time)
        print('Input Airport:', self.airport)
        print('Input Engine:', self.engine)
        print('Input Number of Engines:', self.num_engs)
        print('Input Phase of Flight:', self.phase_flight)

    def find_dict_index(self, dictionary):
        self.dict_keys_list.append(list(dictionary[self.input_list[0]].keys()).index(self.state))
        self.dict_keys_list.append(self.month)
        self.dict_keys_list.append(list(dictionary[self.input_list[2]].keys()).index(self.time))
        self.dict_keys_list.append(list(dictionary[self.input_list[3]].keys()).index(self.airport))
        self.dict_keys_list.append(list(dictionary[self.input_list[4]].keys()).index(self.engine))
        self.dict_keys_list.append(list(dictionary[self.input_list[5]].keys()).index(self.num_engs))
        self.dict_keys_list.append(list(dictionary[self.input_list[6]].keys()).index(self.phase_flight))
        self.input_index_list = self.dict_keys_list
        self.dict_keys_list = numpy.array([self.dict_keys_list, ])
        # print(self.dict_keys_list)
        # print(numpy.shape(self.dict_keys_list))
        return self.dict_keys_list, self.input_index_list

    def predict_KNN(self, model_name, input_array):
        # Load and existing model
        model = load_model(str(model_name + '.hd5'))
        # model.summary()

        # Generate predictions (probabilities -- the output of the last layer)
        # on new data using `predict`
        # print('\n# Generate predictions samples')
        predictions = model.predict(input_array)

        input_size = len(input_array)

        # print('Predictions:')
        for idx in range(input_size):
            # The output of the model predict is an array of length of the output layer
            # This finds the maximum value of the prediction array and saves off the position in the array
            # The position is the answer to which neuron is the best answer, which then tells you which index in the
            # dictionary is the correct value
            predicts = numpy.argmax(predictions[idx])
            self.predicts_array.append(predicts)

        # Print prediction results
        # print(self.predicts_array)

        return self.predicts_array

    def find_dict_string(self, dictionary):
        self.output_name = list(k for k, v in dictionary[self.output_list].items() if v == self.predicts_array[0])
        # print('\nAnswer is:', self.output_name)
        return self.output_name


# ## Function Definitions #############################################################################################


def Keras_Training_Data(dataframe, input_name, output, text_dictionary, sample_size):
    # Double check the output length
    # print('\nOutput Dictionary:', text_dictionary[output])

    # Create a length value
    size_of_output = len(text_dictionary[output])

    # print('\nLength of Output:', size_of_output)

    # Check the distribution of the the output, for each neuron in the output layer
    # print(dataframe[output].value_counts()[:size_of_output])

    # Reorganizes the dataframe and regroups it based on the sample size. The goal is to train the neural network with
    # a balanced output sample
    test = dataframe.groupby(output, group_keys=False).apply(lambda x: x.sample(min(len(x), sample_size)))

    # Check the test dataframe values
    # print('\nTest Dataframe:', test[output])

    # Plot a histogram of the test dataframe
    # hist = test.hist()
    # plt.show()

    # Training Input data values
    X = test[input_name].values

    # Training Output data values
    y = test[output].values

    # Prediction Dataframe, unbalanced
    X1 = dataframe[input_name].values

    # Prediction Dataframe, unbalanced
    y1 = dataframe[output].values

    # Create the test and training data
    X_train_df, X_test_df, y_train_df, y_test_df = train_test_split(X, y, test_size=0.20, random_state=42)

    return X, y, X1, y1, X_train_df, X_test_df, y_train_df, y_test_df, size_of_output


def Keras_NN(X_train_df, X_test_df, y_test_df, y_train_df, X1, y1, input_name, output, number_of_epochs, save_model,
             save_model_name, size_of_output):
    # Size of input
    size_of_input = len(input_name)

    input_list = str(len(input_name))
    input_list = str('In_' + input_list)

    # Define the keras input layer
    inputs = keras.Input(shape=(size_of_input,), name=input_list)

    # Create the first hidden layer, using the relu activation function
    x = Dense(64, activation='relu', name='dense_1')(inputs)

    # Create the second hidden layer, using the relu activation function
    x = Dense(64, activation='relu', name='dense_2')(x)

    # Define the output layer
    outputs = Dense(size_of_output, name=output)(x)

    # Initialize the keras model
    model = keras.Model(inputs=inputs, outputs=outputs)

    # Print the summary of the model
    model.summary()

    # Create the keras model
    model.compile(optimizer=keras.optimizers.RMSprop(),  # Optimizer
                  # Loss function to minimize
                  loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  # List of metrics to monitor
                  metrics=['sparse_categorical_accuracy'])

    # Train the model
    history = model.fit(x=X_train_df, y=y_train_df, batch_size=64, epochs=number_of_epochs, verbose=1,
                        validation_data=(X_test_df, y_test_df))

    # Show the user how the model has done
    print('\nHistory dictionary:', history.history)

    # Show the test data
    print('\nTest data:', X_test_df)

    # Evaluate the model on the test data using evaluate
    print('\nEvaluate on test data')
    results = model.evaluate(X_test_df, y_test_df, batch_size=128)
    print('test loss, test acc:', results)

    # Show the unbalanced results to the user
    results1 = model.evaluate(X1, y1, batch_size=128)
    print('test loss unbalanced, test acc unbalanced:', results1)

    # Show the predictions to see if they match the actual outputs
    print('\n# Generate predictions samples')
    predictions = model.predict(X1[:100])

    # Empty List
    predicts_array = []

    print('Predictions:')
    for idx in range(100):
        # The output of the model predict is an array of length of the output layer
        # This finds the maximum value of the prediction array and saves off the position in the array
        # The position is the answer to which neuron is the best answer, which then tells you which index in the
        # dictionary is the correct value
        predicts = numpy.argmax(predictions[idx])
        predicts_array.append(predicts)

    # Print results
    print(predicts_array)

    print(y1[:idx + 1])

    if save_model:
        model.save(str(save_model_name + '.hd5'))


def Evaluate_Keras_NN(model, X_test_df, y_test_df):
    # Evaluate the model on the test data using `evaluate`
    print('\n# Evaluate on test data')
    results = model.evaluate(X_test_df, y_test_df, batch_size=128)
    print('test loss, test acc:', results)


def Load_Keras_NN(load_model_name, X1, y1):
    # Load and existing model
    model = load_model(str(load_model_name + '.hd5'))
    model.summary()

    # Generate predictions (probabilities -- the output of the last layer)
    # on new data using `predict`
    print('\n# Generate predictions samples')
    predictions = model.predict(X1)

    # Empty List
    predicts_array = []

    print('Predictions:')
    for idx in range(100):
        # The output of the model predict is an array of length of the output layer
        # This finds the maximum value of the prediction array and saves off the position in the array
        # The position is the answer to which neuron is the best answer, which then tells you which index in the
        # dictionary is the correct value
        predicts = numpy.argmax(predictions[idx])
        predicts_array.append(predicts)

    # Print prediction results
    print(predicts_array)

    # Actual Results
    print(y1[:idx + 1])

    return model

def top_five_list(dataframe, output_name, prediction, predict_input_list, input_list, month_number,
                  rank_index, text_dictionary, filter_name):
    aircraft_list = []

    sorted_df = dataframe[dataframe[output_name] == prediction]
    sorted_df = sorted_df[sorted_df[input_list[0]] == predict_input_list[0]]
    sorted_df = sorted_df[sorted_df[input_list[1]] == month_number]
    sorted_df = sorted_df[sorted_df[input_list[2]] == predict_input_list[2]]
    sorted_count = sorted_df.groupby(filter_name).size().reset_index(name='count').sort_values(['count'],
                                                                                              ascending=False)
    sorted_index = sorted_count[filter_name].tolist()
    sorted_index = sorted_index[:rank_index]

    for aircraft_idx in sorted_index:
        aircraft_name = [k for k, v in text_dictionary[filter_name].items() if v == aircraft_idx]
        aircraft_string = ''.join(aircraft_name)
        aircraft_list.append(aircraft_string)

    return aircraft_list

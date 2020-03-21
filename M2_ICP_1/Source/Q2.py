import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#Load Dataset from CSV
dataset = pd.read_csv("breastcancer.csv")

#Replacing M with 0 and B with 1 in the dataset to get train the model as it trains on float value.
dataset['diagnosis'] = dataset['diagnosis'].replace('M', 0)
dataset['diagnosis'] = dataset['diagnosis'].replace('B', 1)
dataset = dataset.values

#Spliting data into value and labels and train test
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,2:32], dataset[:,1], test_size=0.25, random_state=87)
np.random.seed(155)

#Defining Model
my_first_nn = Sequential()  # create model
my_first_nn.add(Dense(20, input_dim=30, activation='relu'))   # First hidden layer
my_first_nn.add(Dense(10, activation='relu'))   # Second hidden layer
my_first_nn.add(Dense(15, activation='relu'))   # Third hidden layer
my_first_nn.add(Dense(7, activation='relu'))    # Forth hidden layer
my_first_nn.add(Dense(1, activation='sigmoid'))     # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])

#Train Model
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, initial_epoch=0)

#Printing Analysis
analysis = my_first_nn.evaluate(X_test, Y_test)
print("Accuracy of the trained model turns out to be", analysis[1], 'with loss of', analysis[0])

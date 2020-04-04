from keras import Sequential
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.utils import to_categorical


# Loading the data using the Keras Library
(train_images,train_labels),(test_images, test_labels) = mnist.load_data()

# Processing Data
# Converting X*28*28 into X*784 Also called Flattening
dimData = np.prod(train_images.shape[1:])
train_data = train_images.reshape(train_images.shape[0],-1)
test_data = test_images.reshape(test_images.shape[0],-1)

#convert data to float and scale values between 0 and 1
train_data = train_data.astype('float')
test_data = test_data.astype('float')
#scale data
train_data /=255.0
test_data /=255.0

#change the labels from class vector to binary matrix
binTrainLabels = to_categorical(train_labels)
binTestLabels = to_categorical(test_labels)

#creating network
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(dimData,)))
model.add(Dense(512, activation='relu'))
model.add(Dense(10, activation='softmax'))


#We define the hyperparameters for the nueral retwork and the run to fit the data
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, binTrainLabels, batch_size=256, epochs=5, verbose=1,
                    validation_data=(test_data, binTestLabels))

#Ploting the loss and accuracy for both training and validation
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Train and validation accuracy')
plt.xlabel('Number of epochs')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.show()


#printing the result of the training and testing
[test_loss, test_acc] = model.evaluate(test_data, binTestLabels)
print("Evaluation result on Test Data : Loss = {}, accuracy = {}".format(test_loss, test_acc))

#making prediction on one image in test data
pred = model.predict(test_data[[5],:], batch_size=1)
print("Predicted Value : ", np.argmax(pred))
plt.imshow(test_images[5], cmap = 'gray')
plt.show()

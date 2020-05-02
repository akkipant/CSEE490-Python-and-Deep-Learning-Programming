from keras.layers import Input, Dense
from keras.models import Model
from keras import backend as K

# this is the size of our encoded representations
encoding_dim = 32  # 32 floats -> compression of factor 24.5, assuming the input is 784 floats

# this is our input placeholder
input_img = Input(shape=(784,))
#added hidden layer in encoder
hidden_1 = Dense(128, activation='relu')(input_img)
# "encoded" is the encoded representation of the input
encoded = Dense(encoding_dim, activation='relu')(hidden_1)
#added hidden layer in decoder
hidden_2 = Dense(128, activation='relu')(encoded)
# "decoded" is the lossy reconstruction of the input
decoded = Dense(784, activation='sigmoid')(hidden_2)
# this model maps an input to its reconstruction
autoencoder = Model(input_img, decoded)
# this model maps an input to its encoded representation

autoencoder.summary()

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy', metrics=['accuracy'])
from keras.datasets import mnist, fashion_mnist
import numpy as np
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

hist = autoencoder.fit(x_train, x_train,
                epochs=10,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))


# Making prediction and saving output for all of the layers
inp = autoencoder.input                                           # input placeholder
outputs = [layer.output for layer in autoencoder.layers]          # all layer outputs
functors = [K.function([inp], [out]) for out in outputs]          # evaluation functions
# Testing
test = x_test[0].reshape(1,784)
encoded_imgs = [func([test]) for func in functors]

from matplotlib import pyplot as plt
fig = plt.figure(figsize=(24,10))
axis = fig.add_subplot(1, 3, 1, xticks=[], yticks=[])
axis.imshow(encoded_imgs[0][0].reshape(28,28), cmap='gray')
plt.title('Original', fontsize=40)
axis = fig.add_subplot(1, 3, 2, xticks=[], yticks=[])
axis.imshow(encoded_imgs[2][0].reshape(16,2), cmap='gray')
plt.title('Compressed', fontsize=40)
axis = fig.add_subplot(1, 3, 3, xticks=[], yticks=[])
axis.imshow(encoded_imgs[4][0].reshape(28,28), cmap='gray')
plt.title('Reconstructed', fontsize=40)
plt.show()


# summarize history for accuracy
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
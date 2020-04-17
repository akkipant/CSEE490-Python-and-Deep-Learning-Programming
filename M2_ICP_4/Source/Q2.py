# Simple CNN model for CIFAR-10
import numpy, keras, tensorflow, pandas
from keras.datasets import cifar10
from keras.models import load_model
from keras.utils import np_utils
from keras import backend as K
from matplotlib import pyplot as plt
K.common.image_dim_ordering()

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
# normalize inputs from 0-255 to 0.0-1.0
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train / 255.0
X_test = X_test / 255.0
# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

labels = {0 : 'airplane',
          1 : 'automobile',
          2 : 'bird',
          3 : 'cat',
          4 : 'deer',
          5 : 'dog',
          6 : 'frog',
          7 : 'horse',
          8 : 'ship',
          9 : 'truck'}

#Loading UseCase Model
model1 = load_model('models/useCase.h5')

predicted = list()
for x in X_test[:4]:
  predicted.append(model1.predict(numpy.expand_dims(x, axis=0)))

pr_use = []
for i in range(4):
  plt.subplot(140+1+i)
  plt.title(labels[numpy.argmax(y_test[i])])
  plt.imshow(X_test[i])
  pr_use.append(labels[numpy.argmax(predicted[i])])
plt.show()
print("UseCase")
print(pr_use)

#Loading icp.h5 model
model = load_model('models/icp.h5')

predicted = list()
for x in X_test[:4]:
  predicted.append(model.predict(numpy.expand_dims(x, axis=0)))

pr_ICP = []
for i in range(4):
  pr_ICP.append(labels[numpy.argmax(predicted[i])])
plt.show()
print("ICP")
print(pr_ICP)
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:01:16 2018

@author: deept
"""

#importing stuff
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten, Dropout
#The different layer functions
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Flatten())
#Taking input
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)))
#The above statement takes an input for images of 224*224*3
model.compile(loss='binary_crossentropy', optimizer='rmsprop')
#This is a method for backpropagation with an optimizer and the loss as well
#wherein the loss mentioned is minimized in each iteration.

#assume a stochastic gradient is to be built, one needs a proper initialization

from keras.optimizers import SGD #stochastic gradient
sgd=SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

#Now we fit the model, and that's done by
model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_val, y_val))
score=model.evaluate(x_test, y_test, batch_size=32)

#example:
import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
trX=np.linspace(-1, 1, 101)
trY= 3* trX + np.random.randn(*trX.shape)*0.33
# The training sets are now made using a bunch of points from numpy
model= Sequential()
model.add(Dense(input_dim=1, output_dim=1, init='uniform', activation='linear'))

#and now for the weights
weights = model.layers[0].get_weights()
w_init = weights[0][0][0]
b_init = weights[1][0]
print('Linear regression model is initialized with weights w: %.2f, b: %.2f' % (w_init, b_init))
# Now we train this linear model with training data of trX and trY where TrY= 3*trX.

model.compile(optimizer='sgd', loss='mse')
#feeding data in using fit function
model.fit(trX, trY, nb_epoch=200, verbose=1)

#Now, printing the weights after training, we do:
weights=model.layers[0].get_weights()
w_final=weights[0][0][0]
b_final=weights[1][0]
print('Linear regression model is trained to have weights w: %.2f, b:%.2f' % (w_final, b_final))

#Now saving weights, in order to use em, we do
model.save_weights("my_model.h5")

#Restoring weights:
model.load_weights("my_model.h5")

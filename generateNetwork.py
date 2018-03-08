# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:54:25 2018

@author: deept
"""
import numpy as np
from keras.callbacks import EarlyStopping,TensorBoard
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D
from keras.optimizers import Adam
from keras.layers import BatchNormalization
from keras.layers.pooling import MaxPooling2D
from keras.utils import to_categorical
from keras import regularizers
def netCreate(genSequence, n_neurons, dropval, dataset):
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:22:37 2019

@author: mancmanomyst
"""

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils, plot_model

with np.load("voxelgrid.npz") as data:
    
    X_test2=data["X_test2"]
    y_test2=data["y_test2"]

model_name="/home/mancmanomyst/modelneth5py/modelnet40_ply_hdf5_2048/3d_vox.h5"
model2 = load_model(model_name)

X_test2 = X_test2.reshape(-1, 16, 16, 16)

predicted_classes=model2.predict_classes(X_test2)
correct_indices=np.nonzero(predicted_classes==y_test2)[0]
wrong_indices=np.nonzero(predicted_classes!=y_test2)[0]

print(len(correct_indices)," classified correctly")
print(len(wrong_indices)," classified incorrectly")
print("predicted class = {} and correct class = {}".format(predicted_classes[wrong_indices[5]],y_test2[wrong_indices[5]]))
#print(model2.summary())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:37:40 2019

@author: mancmanomyst
"""

import h5py
import numpy as np
from voxelgrid import VoxelGrid


f=h5py.File("ply_data_train0.h5","r")
data=f["data"][:]
label=f["label"][:]
size=data.shape[0]

out = (np.zeros((size, 4096), dtype="f"), np.zeros(size, dtype=np.int8))
    
for i in range(size):
        voxelgrid = VoxelGrid(data[i,:], x_y_z=[16, 16, 16])
        # make the vector range 0-1
        out[0][i] = voxelgrid.vector.reshape(-1) / np.max(voxelgrid.vector)
        out[1][i] = label[i]
print("[DONE]")
f.close


f=h5py.File("ply_data_train1.h5","r")
data=f["data"][:]
label=f["label"][:]
size=data.shape[0]

out1 = (np.zeros((size, 4096), dtype="f"), np.zeros(size, dtype=np.int8))
    
for i in range(size):
        voxelgrid = VoxelGrid(data[i,:], x_y_z=[16, 16, 16])
        # make the vector range 0-1
        out1[0][i] = voxelgrid.vector.reshape(-1) / np.max(voxelgrid.vector)
        out1[1][i] = label[i]
print("[DONE]")
f.close

f=h5py.File("ply_data_train2.h5","r")
data=f["data"][:]
label=f["label"][:]
size=data.shape[0]

out2 = (np.zeros((size, 4096), dtype="f"), np.zeros(size, dtype=np.int8))
    
for i in range(size):
        voxelgrid = VoxelGrid(data[i,:], x_y_z=[16, 16, 16])
        # make the vector range 0-1
        out2[0][i] = voxelgrid.vector.reshape(-1) / np.max(voxelgrid.vector)
        out2[1][i] = label[i]
print("[DONE]")
f.close


f=h5py.File("ply_data_train3.h5","r")
data=f["data"][:]
label=f["label"][:]
size=data.shape[0]

out3 = (np.zeros((size, 4096), dtype="f"), np.zeros(size, dtype=np.int8))
    
for i in range(size):
        voxelgrid = VoxelGrid(data[i,:], x_y_z=[16, 16, 16])
        # make the vector range 0-1
        out3[0][i] = voxelgrid.vector.reshape(-1) / np.max(voxelgrid.vector)
        out3[1][i] = label[i]
print("[DONE]")
f.close


f=h5py.File("ply_data_train4.h5","r")
data=f["data"][:]
label=f["label"][:]
size=data.shape[0]

out4 = (np.zeros((size, 4096), dtype="f"), np.zeros(size, dtype=np.int8))
    
for i in range(size):
        voxelgrid = VoxelGrid(data[i,:], x_y_z=[16, 16, 16])
        # make the vector range 0-1
        out4[0][i] = voxelgrid.vector.reshape(-1) / np.max(voxelgrid.vector)
        out4[1][i] = label[i]
print("[DONE]")
f.close


f=h5py.File("ply_data_test0.h5","r")
data=f["data"][:]
label=f["label"][:]
size=data.shape[0]

out_t = (np.zeros((size, 4096), dtype="f"), np.zeros(size, dtype=np.int8))
    
for i in range(size):
        voxelgrid = VoxelGrid(data[i,:], x_y_z=[16, 16, 16])
        # make the vector range 0-1
        out_t[0][i] = voxelgrid.vector.reshape(-1) / np.max(voxelgrid.vector)
        out_t[1][i] = label[i]
print("[DONE]")
f.close

f=h5py.File("ply_data_test1.h5","r")
data=f["data"][:]
label=f["label"][:]
size=data.shape[0]

out_t2 = (np.zeros((size, 4096), dtype="f"), np.zeros(size, dtype=np.int8))
    
for i in range(size):
        voxelgrid = VoxelGrid(data[i,:], x_y_z=[16, 16, 16])
        # make the vector range 0-1
        out_t2[0][i] = voxelgrid.vector.reshape(-1) / np.max(voxelgrid.vector)
        out_t2[1][i] = label[i]
print("[DONE]")
f.close

X_train=np.concatenate((out[0],out1[0],out2[0],out3[0],out4[0]))
X_test=np.array(out_t[0])
y_train=np.concatenate((out[1],out1[1],out2[1],out3[1],out4[1]))
y_test=np.array(out_t[1])
X_test2=np.array(out_t2[0])
y_test2=np.array(out_t2[1])

np.savez("voxelgrid.npz",X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,X_test2=X_test2,y_test2=y_test2)











#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:46:23 2019

@author: mancmanomyst
"""

import h5py
import numpy as np
from IPython.display import Image
from voxelgrid import VoxelGrid
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from math import cos,sin

plt.rcParams['image.interpolation'] = None
plt.rcParams['image.cmap'] = 'gray'

f=h5py.File("ply_data_test0.h5","r")
data=f["data"][:]
label=f["label"][:]

d=data[28,:]
l=label[2]

print(l)

a_voxelgrid = VoxelGrid(d, x_y_z=[40, 40, 40])

h=a_voxelgrid.vector
x,y,z=h.nonzero()
xyz=np.vstack((x,y,z))
xyz=xyz.T
rot=np.array([[1,0,0],[0,cos(0.523),-sin(0.523)],[0,sin(0.523),cos(0.523)]])
rotx=np.dot(xyz,rot)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(rotx[:,0],rotx[:,1],rotx[:,2],zdir='z', c='red')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
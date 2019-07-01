#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:38:10 2019

@author: mancmanomyst
"""

import open3d as o3d
import numpy as np
import h5py
from voxelgrid import VoxelGrid
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

f=h5py.File("ply_data_test0.h5","r")
data=f["data"][:]
label=f["label"][:]
d=data[28,:]
l=label[0]
print(l)

a_voxelgrid = VoxelGrid(d, x_y_z=[16, 16, 16])

h=a_voxelgrid.vector
xyz=h.nonzero()
xyz=np.asarray(xyz)
xy=xyz.T


pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xy)

o3d.io.write_point_cloud("sync.ply", pcd)

 # Load saved point cloud and visualize it
pcd_load = o3d.io.read_point_cloud("sync.ply")
pcd_load.paint_uniform_color([0, 0, 0])
o3d.visualization.draw_geometries([pcd_load])
#22,46,84,116
